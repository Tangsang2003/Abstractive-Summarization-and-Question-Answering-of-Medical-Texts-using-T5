from flask import render_template, request, Blueprint, current_app, flash, redirect, url_for
from app.utils.summarization import summarize_text, google_summary, extract_text_from_pdf, allowed_file
from app.utils.question_answering import answer_question, google_qna
# from flask_wtf import FlaskForm
# from wtforms import SelectField, FileField, TextAreaField, SubmitField
# from wtforms.validators import DataRequired
import markdown2

from .forms import SummarizeForm, QaForm, ContactForm


bp = Blueprint('main', __name__)


@bp.route('/')
@bp.route('/home')
def home():
    return render_template('home.html', active_page='home')


# @bp.route('/summarize', methods=['POST'])
# def summarize():
#     input_text = request.form['input_text']
#     summarization_model = current_app.summarization_model
#     summary = summarize_text(input_text, summarization_model)
#     return render_template('result.html', result=summary, task="Summarization")


# @bp.route('/answer', methods=['POST'])
# def answer():
#     input_text = request.form['input_text']
#     qa_model = current_app.qa_model
#     question = request.form['question']
#     answer = answer_question(input_text, question, qa_model)
#     return render_template('result.html', result=answer, task="Question Answering")


@bp.route('/summarize', methods=['GET', 'POST'])
def summarize():
    form = SummarizeForm()
    if form.validate_on_submit():
        model = form.model_choice.data
        if form.file_upload.data:
            # Check if the file is a PDF
            file = form.file_upload.data
            if allowed_file(file.filename):
                file_contents = extract_text_from_pdf(file)
                if model == 'google-gemini':
                    level = form.gemini_option.data
                    if level == 'professional':
                        summary = google_summary(file_contents, level).text
                    elif level == 'intermediate':
                        summary = google_summary(file_contents, level).text
                    else:
                        summary = google_summary(file_contents, level).text

                    # Convert Markdown to HTML
                    html_content = markdown2.markdown(summary)
                    # Render the results template with the HTML content
                    return render_template('result.html', html_content=html_content, task="Summarization")
                else:
                    summarization_model = current_app.summarization_model
                    summary = summarize_text(file_contents, summarization_model)
                    return render_template('result.html', result=summary, task='Summarization')

            else:
                flash('Only PDF files are allowed!', 'danger')
                return redirect(url_for('main.summarize'))

        elif form.input_text.data:
            if model == 'google-gemini':
                level = form.gemini_option.data
                if level == 'professional':
                    summary = google_summary(form.input_text.data, level).text
                elif level == 'intermediate':
                    summary = google_summary(form.input_text.data, level).text
                else:
                    summary = google_summary(form.input_text.data, level).text
                # Convert Markdown to HTML
                html_content = markdown2.markdown(summary)

                # Render the results template with the HTML content
                return render_template('result.html', html_content=html_content, task="Summarization")
            # Logic to summarize from input text using selected model
            else:
                summarization_model = current_app.summarization_model
                summary = summarize_text(form.input_text.data, summarization_model)
                return render_template('result.html', result=summary, task="Summarization")
        else:
            summary = "No input provided"

        return render_template('result.html', result=summary, task="Summarization")

    return render_template('summarize.html', form=form, active_page="summarize")


# Route for Question-Answering
@bp.route('/qna', methods=['GET', 'POST'])
def qna():
    form = QaForm()
    answer = None

    if form.validate_on_submit():
        model = form.model_choice.data

        # Handle file upload
        if form.file_upload.data:
            if form.question_input.data:
                question = form.question_input.data
            else:
                flash('Please, provide the question!', 'danger')
            file = form.file_upload.data
            if allowed_file(file.filename):
                file_contents = extract_text_from_pdf(file)
                if model == 'google-gemini':
                    level = form.gemini_option.data

                    answer = google_qna(file_contents, question, level).text
                    # Convert Markdown to HTML
                    html_content = markdown2.markdown(answer)
                    return render_template('qna.html', question=question, form=form, answer=html_content, active_page='question-answer')
                else:
                    qa_model = current_app.qa_model
                    answer = answer_question(form.input_text.data, question, qa_model)
                    return render_template('qna.html', question=question, form=form, answer=answer, active_page='question-answer')
            else:
                flash('Only PDF files are allowed!', 'danger')
        elif form.input_text.data:
            question = form.question_input.data
            if model == 'google-gemini':
                level = form.gemini_option.data
                if level == 'professional':
                    answer = google_qna(form.input_text.data, question, level).text
                elif level == 'intermediate':
                    answer = google_qna(form.input_text.data, question, level).text
                else:
                    answer = google_qna(form.input_text.data, question, level).text
                # Convert Markdown to HTML
                html_content = markdown2.markdown(answer)

                # Render the results template with the HTML content
                return render_template('qna.html', question=question, form=form, answer=html_content, active_page='question-answer')
            else:
                qa_model = current_app.qa_model
                answer = answer_question(form.input_text.data, question, qa_model)

                return render_template('result.html', answer=answer, task="Question Answering")
        else:
            answer = "No input provided"

    # return render_template('result.html', result=answer, task="Question Answering')
    return render_template('qna.html', form=form, answer=answer, active_page="question-answer")


# Route for About Us Page
@bp.route('/about')
def about():
    return render_template('about_us.html', active_page='about')


# Route for Contact Us Page
@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        # email = form.email.data
        # subject = form.subject.data
        # message = form.message.data

        # Process the form data (e.g., send email, save to database, etc.)
        # For now, we'll just flash a message
        flash(f'Thank you, {name}. Your message has been received', 'success')

        return redirect(url_for('main.contact'))

    return render_template('contact_us.html', form=form, active_page="contact")
