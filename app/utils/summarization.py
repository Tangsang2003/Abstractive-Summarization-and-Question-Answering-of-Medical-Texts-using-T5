from transformers import T5Tokenizer, T5ForConditionalGeneration, pipeline
from tqdm import tqdm
import re
import google.generativeai as genai
import os
import fitz

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')


# This function cleans the text by getting rid of special characters.
def clean_text(text):
    cleaned_text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    return cleaned_text


# This function counts words from the text.
def count_words(text):
    """
    Counts the number of words in a given text after removing special characters.

    Parameters:
    text (str): The input text.

    Returns:
    int: The number of words in the text.
    """
    # Using regex to remove special characters and keep only alphanumeric characters and spaces
    cleaned_text = clean_text(text)

    # Split the cleaned text by whitespace to get the words
    words = cleaned_text.split()

    # Return the length of the list of words
    return len(words)


# This function is used to load the model during app startup
def load_summarization_model():
    print("Loading Summarization Model...")
    with tqdm(total=2, desc="Summarization Model", bar_format="{l_bar}{bar} [ time left: {remaining} ]") as pbar:
        tokenizer = T5Tokenizer.from_pretrained(
            './app/models/summarization/summarization_final_trained_model/tokenizer')
        pbar.update(1)
        model = T5ForConditionalGeneration.from_pretrained(
            './app/models/summarization/summarization_final_trained_model')
        pbar.update(1)
    print("Summarization Model Loaded Successfully")
    return pipeline("summarization", model=model, tokenizer=tokenizer)


# Function to summarize the given medical text, Further implementation required to handle longer than max_length
# articles
# Not using because of unknown bug
def summarize_text_long(text, summarization_pipeline):
    tokenizer = summarization_pipeline.tokenizer
    summaries = []
    chunk_size = 512
    overlap_size = 50
    tokens = tokenizer.encode(text, return_tensors='pt', truncation=False)
    input_length = tokens.size(1)

    for start in range(0, input_length, chunk_size - overlap_size):
        end = min(start + chunk_size, input_length)
        chunk_text = tokenizer.decode(tokens[0, start:end], skip_special_tokens=True)

        # Generate summary for the current chunk
        summary = summarization_pipeline(chunk_text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
        summaries.append(summary)

        if end == input_length:
            break

        # Combine all summaries
    combined_summary = " ".join(summaries)
    return combined_summary


# Function to Normalize input texts
def normalize_text(text):
    # Remove newlines, extra whitespace, and replace bullet points with spaces
    text = re.sub(r'\n+', ' ', text)  # Replace multiple newlines with a single space
    text = re.sub(r'\r+', ' ', text)  # Replace carriage returns with a space
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = re.sub(r'\*+', ' ', text)  # Replace asterisks with a space (if used as bullets)
    text = re.sub(r'\-+', ' ', text)  # Replace dashes with a space (if used as bullets)
    text = re.sub(r'\n', ' ', text)
    return text.strip()  # Strip leading and trailing spaces


# Fix summarize function
def summarize_text(text, summarization_pipeline):

    # Generate summary for the current chunk
    length = count_words(text)
    input_text = normalize_text(text)
    summary = summarization_pipeline(input_text, max_length=round(0.7 * length), min_length=round(0.35 * length),
                                     do_sample=False)[0]['summary_text']
    # Split the summary into sentences
    sentences = summary.split('. ')
    # The code below is to ensure proper capitalization of first words of sentences in the summary to be capital.
    # This was done because the summary contained all words in small because of pre-processing during input.
    # Capitalize the first letter of each sentence
    capitalized_sentences = '. '.join(sentence.capitalize() for sentence in sentences)

    # Capitalize the very first letter of the entire summary
    capitalized_summary = capitalized_sentences[0].capitalize() + capitalized_sentences[1:]
    return capitalized_summary


# This function ensures that uploaded file is in pdf
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'


# This function is used to extract text from the uploaded pdf
def extract_text_from_pdf(file):
    text = ''
    pdf_document = fitz.open(stream=file.read(), filetype="pdf")
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text


# This function uses Google Gemini to generate summaries
def google_summary(text, level):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    output_level = level
    if level == 'professional':
        input_prompt = 'Summarize the whole text suitable for Healthcare Professional ' \
                       '(It is not necessary to simplify terms)'
    elif level == 'intermediate':
        input_prompt = 'Summarize the whole text suitable for intermediate (Informed Individual): '
    else:
        input_prompt = 'Summarize the whole text suitable for Layman person: '
    response = model.generate_content(input_prompt + text)
    return response

# Test
# Ignore below. Use for testing only
# context = '''
#
#
# Title: Impact of Genetic Variations on Drug Metabolism Pathways
#
# Abstract:
# Genetic polymorphisms can significantly influence drug metabolism pathways, affecting drug efficacy and toxicity. Understanding these variations is crucial for personalized medicine initiatives. This study investigates the impact of cytochrome P450 (CYP) genetic variants on the metabolism of commonly prescribed medications. The findings highlight the importance of genotype-guided dosing strategies to optimize therapeutic outcomes and minimize adverse effects in clinical practice.
#
# Introduction:
# The cytochrome P450 enzymes, particularly CYP2D6 and CYP3A4, play pivotal roles in the biotransformation of numerous drugs. Genetic polymorphisms in these enzymes can lead to poor metabolizer phenotypes, where individuals may experience higher drug concentrations and increased risk of adverse effects. Conversely, ultra-rapid metabolizers may require higher doses for therapeutic efficacy. This variability underscores the need for pharmacogenetic testing to individualize drug therapy.
#
# Methods:
# A systematic review of literature was conducted to identify studies reporting associations between CYP genetic polymorphisms and drug metabolism. Studies encompassing diverse populations and therapeutic classes were included. Data synthesis involved meta-analysis where appropriate to assess the strength of associations and clinical implications.
#
# Results:
# Several CYP genetic variants, such as CYP2D64 and CYP3A422, were found to significantly alter drug metabolism rates. Patients carrying these variants may require dose adjustments to achieve optimal drug concentrations in plasma. The variability observed underscores the complexity of pharmacogenetic interactions and the necessity for comprehensive genetic testing in clinical settings.
#
# Discussion:
# The implications of genetic variations on drug metabolism are multifaceted, affecting drug efficacy, safety, and healthcare costs. Genotype-guided dosing strategies have the potential to improve therapeutic outcomes by minimizing adverse reactions and enhancing treatment adherence. Challenges remain in implementing pharmacogenetic testing universally, including cost-effectiveness and physician awareness.
#
# Conclusion:
# Incorporating pharmacogenetic information into clinical decision-making can enhance precision medicine initiatives. Future research should focus on elucidating additional genetic markers and refining dosing algorithms to optimize drug therapy outcomes across diverse patient populations.
# '''
#
# summary = summarize_text(context)
# print(summary)

