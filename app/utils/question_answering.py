from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the T5-base model and tokenizer
tokenizer_base = T5Tokenizer.from_pretrained('t5-base')
model_base = T5ForConditionalGeneration.from_pretrained('t5-base')

def answer_question(context, question, model_type='base'):
    if model_type == 'base':
        tokenizer, model = tokenizer_base, model_base
    else:
        raise ValueError("Unsupported model type")

    input_text = "question: {} context: {}".format(question, context)
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=150, num_beams=4, early_stopping=True)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer
