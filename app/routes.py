from flask import render_template, request, Blueprint, current_app
from app.utils.summarization import summarize_text
from app.utils.question_answering import answer_question


bp = Blueprint('main', __name__)


@bp.route('/')
@bp.route('/home')
def home():
    return render_template('home.html')


@bp.route('/summarize', methods=['POST'])
def summarize():
    input_text = request.form['input_text']
    summarization_model = current_app.summarization_model
    summary = summarize_text(input_text, summarization_model)
    return render_template('result.html', result=summary, task="Summarization")


@bp.route('/answer', methods=['POST'])
def answer():
    input_text = request.form['input_text']
    qa_model = current_app.qa_model
    question = request.form['question']
    answer = answer_question(input_text, question, qa_model)
    return render_template('result.html', result=answer, task="Question Answering")
