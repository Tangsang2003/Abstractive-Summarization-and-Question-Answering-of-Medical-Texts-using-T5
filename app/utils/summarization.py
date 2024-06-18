from transformers import T5Tokenizer, T5ForConditionalGeneration, pipeline

# Load the T5-small model and tokenizer from local directory
tokenizer_small = T5Tokenizer.from_pretrained('t5-small')
model_summarization = T5ForConditionalGeneration.from_pretrained('./../models/summarization')

# Initialize the summarization pipeline with the local model and tokenizer
summarization_pipeline = pipeline("summarization", model=model_summarization, tokenizer=tokenizer_small)


def summarize_text(text, max_chunk_length=512):
    # Split text into chunks
    text_chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]

    # Summarize each chunk
    summaries = [summarization_pipeline(chunk, max_length=150, min_length=30, do_sample=False)[0]['summary_text'] for
                 chunk in text_chunks]

    # Combine summaries
    combined_summary = ' '.join(summaries)
    return combined_summary


# Test
context = '''


Title: Impact of Genetic Variations on Drug Metabolism Pathways

Abstract:
Genetic polymorphisms can significantly influence drug metabolism pathways, affecting drug efficacy and toxicity. Understanding these variations is crucial for personalized medicine initiatives. This study investigates the impact of cytochrome P450 (CYP) genetic variants on the metabolism of commonly prescribed medications. The findings highlight the importance of genotype-guided dosing strategies to optimize therapeutic outcomes and minimize adverse effects in clinical practice.

Introduction:
The cytochrome P450 enzymes, particularly CYP2D6 and CYP3A4, play pivotal roles in the biotransformation of numerous drugs. Genetic polymorphisms in these enzymes can lead to poor metabolizer phenotypes, where individuals may experience higher drug concentrations and increased risk of adverse effects. Conversely, ultra-rapid metabolizers may require higher doses for therapeutic efficacy. This variability underscores the need for pharmacogenetic testing to individualize drug therapy.

Methods:
A systematic review of literature was conducted to identify studies reporting associations between CYP genetic polymorphisms and drug metabolism. Studies encompassing diverse populations and therapeutic classes were included. Data synthesis involved meta-analysis where appropriate to assess the strength of associations and clinical implications.

Results:
Several CYP genetic variants, such as CYP2D64 and CYP3A422, were found to significantly alter drug metabolism rates. Patients carrying these variants may require dose adjustments to achieve optimal drug concentrations in plasma. The variability observed underscores the complexity of pharmacogenetic interactions and the necessity for comprehensive genetic testing in clinical settings.

Discussion:
The implications of genetic variations on drug metabolism are multifaceted, affecting drug efficacy, safety, and healthcare costs. Genotype-guided dosing strategies have the potential to improve therapeutic outcomes by minimizing adverse reactions and enhancing treatment adherence. Challenges remain in implementing pharmacogenetic testing universally, including cost-effectiveness and physician awareness.

Conclusion:
Incorporating pharmacogenetic information into clinical decision-making can enhance precision medicine initiatives. Future research should focus on elucidating additional genetic markers and refining dosing algorithms to optimize drug therapy outcomes across diverse patient populations.
'''

summary = summarize_text(context)
print(summary)

