from transformers import T5Tokenizer, T5ForConditionalGeneration, pipeline
from tqdm import tqdm


# This function loads the question-answering model during app startup
def load_qa_model():
    print("Loading QA Model...")
    with tqdm(total=2, desc="QA Model", bar_format="{l_bar}{bar} [ time left: {remaining} ]") as pbar:
        tokenizer = T5Tokenizer.from_pretrained('./app/models/question_answering/checkpoint-1500/tokenizer')
        pbar.update(1)
        model = T5ForConditionalGeneration.from_pretrained('./app/models/question_answering/checkpoint-1500')
        pbar.update(1)
    print("QA Model Loaded Successfully")

    return pipeline("text2text-generation", model=model, tokenizer=tokenizer)


# Function to generate answer based on Context and question
def answer_question(context, question, qa_pipeline):
    # Prepare the input for the model
    input_text = f"question: {question} context: {context}"
    # Perform text generation (which in this case will answer the question)
    generated_text = qa_pipeline(input_text, max_length=150)

    # Extract the generated answer from the output
    answer = generated_text[0]['generated_text'].strip()
    return answer


# Example usage
# context = '''
# Medical Text: Diabetes Mellitus
# Diabetes mellitus is a chronic condition characterized by high levels of glucose in the blood due to the body's inability to produce enough insulin or effectively use the insulin it produces. There are two primary types of diabetes:
#
# Type 1 Diabetes: An autoimmune condition where the immune system attacks insulin-producing beta cells in the pancreas. This type often manifests in childhood or adolescence and requires lifelong insulin therapy.
#
# Type 2 Diabetes: A metabolic disorder that results from the body's ineffective use of insulin. It is more common in adults and is often associated with obesity, physical inactivity, and genetic predisposition. Management includes lifestyle changes, oral medications, and sometimes insulin.
#
# Common symptoms of diabetes include frequent urination, excessive thirst, unexplained weight loss, extreme hunger, fatigue, blurred vision, and slow-healing sores. Long-term complications can affect the heart, blood vessels, eyes, kidneys, and nerves.
#
# Diagnosis of diabetes is typically based on blood tests, such as the fasting plasma glucose test, oral glucose tolerance test, or the hemoglobin A1c test.
#
# Management strategies for diabetes focus on controlling blood sugar levels, maintaining a healthy diet, engaging in regular physical activity, monitoring blood glucose, and adhering to medication regimens. Education and regular follow-up are critical components of effective diabetes management.
#
# '''
# question = "How is Type 2 diabetes commonly managed?"
#
# answer = answer_question(context, question)
# print("Answer:", answer)


