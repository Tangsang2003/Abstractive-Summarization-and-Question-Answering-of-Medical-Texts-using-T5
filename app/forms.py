# forms.py
from flask_wtf import FlaskForm
from wtforms import SelectField, FileField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


# Form for summary generation
class SummarizeForm(FlaskForm):
    model_choice = SelectField('Choose Model', choices=[('t5-pubmed', 'T5 fine-tuned on PubMed'
                                                         ), ('google-gemini', 'Gemini')],
                               validators=[DataRequired()])
    gemini_option = SelectField('Audience Level', choices=[('professional', 'Professional (Healthcare Professional)'),
                                                          ('intermediate', 'Intermediate (Informed Individual)'),
                                                          ('layman', 'Layman (General Public)')], validators=[])
    file_upload = FileField('Upload File')
    input_text = TextAreaField('Input Text')
    submit = SubmitField('Summarize')


# Form for Question Answering
class QaForm(FlaskForm):
    model_choice = SelectField('Choose Model', choices=[
        ('t5-pubmed', 'T5 fine-tuned on PubMed'),
        ('google-gemini', 'Gemini')
    ], validators=[DataRequired()])

    gemini_option = SelectField('Audience Level', choices=[
        ('professional', 'Professional (Healthcare Professional)'),
        ('intermediate', 'Intermediate (Informed Individual)'),
        ('layman', 'Layman (General Public)')
    ], validators=[])

    file_upload = FileField('Upload File')
    input_text = TextAreaField('Input Text')
    question_input = TextAreaField('Question')
    submit = SubmitField('Answer')
