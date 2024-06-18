from flask import render_template, request, jsonify
from app import app
from app.utils.summarization import summarize_text
from app.utils.question_answering import answer_question


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    input_text = request.form['input_text']
    summary = summarize_text(input_text)
    return render_template('result.html', result=summary, task="Summarization")


@app.route('/answer', methods=['POST'])
def answer():
    input_text = request.form['input_text']
    question = request.form['question']
    answer = answer_question(input_text, question)
    return render_template('result.html', result=answer, task="Question Answering")
