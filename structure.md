Sure, here's a structured way to organize your Flask application for medical summarization and question answering using T5-small and T5-base models.

### Project Structure

```
MedSummarizerQA/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── result.html
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── script.js
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── summarization.py
│   │   ├── question_answering.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── t5_small.py
│   │   ├── t5_base.py
├── instance/
│   ├── config.py
├── tests/
│   ├── test_routes.py
│   ├── test_utils.py
├── venv/
├── .env
├── .gitignore
├── config.py
├── run.py
├── requirements.txt
├── README.md
```

### Description of Files and Directories

- `app/`: Main application directory.
  - `__init__.py`: Initializes the Flask app and extensions.
  - `routes.py`: Contains the routes/endpoints for the application.
  - `models.py`: Defines database models (if needed).
  - `forms.py`: Contains form classes for handling user input (if needed).
  - `templates/`: Directory for HTML templates.
    - `base.html`: Base template for extending other templates.
    - `home.html`: Home page template.
    - `result.html`: Template for displaying results.
  - `static/`: Directory for static files (CSS, JavaScript, images).
    - `css/style.css`: Custom CSS styles.
    - `js/script.js`: Custom JavaScript scripts.
  - `utils/`: Directory for utility scripts and functions.
    - `summarization.py`: Functions for handling summarization using T5 models.
    - `question_answering.py`: Functions for handling question answering using T5 models.
  - `models/`: Directory for loading models.
    - `t5_small.py`: Script for loading and handling the T5-small model.
    - `t5_base.py`: Script for loading and handling the T5-base model.
- `instance/`: Configuration files that should not be in version control.
  - `config.py`: Instance-specific configuration (e.g., secret keys).
- `tests/`: Directory for test cases.
  - `test_routes.py`: Test cases for routes.
  - `test_utils.py`: Test cases for utility functions.
- `venv/`: Virtual environment directory.
- `.env`: Environment variables (e.g., API keys, configuration settings).
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `config.py`: Main configuration file.
- `run.py`: Script to run the Flask application.
- `requirements.txt`: Lists the dependencies and packages needed.
- `README.md`: Project documentation.

### Sample Code Snippets

#### `run.py`
```python
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

#### `app/__init__.py`
```python
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    with app.app_context():
        from . import routes
        return app
```

#### `app/routes.py`
```python
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
```

#### `app/utils/summarization.py`
```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the T5-small model and tokenizer
tokenizer_small = T5Tokenizer.from_pretrained('t5-small')
model_small = T5ForConditionalGeneration.from_pretrained('t5-small')

def summarize_text(text, model_type='small'):
    if model_type == 'small':
        tokenizer, model = tokenizer_small, model_small
    else:
        raise ValueError("Unsupported model type")

    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=150, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary
```

#### `app/utils/question_answering.py`
```python
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
```

### Running the Application

1. **Create a Virtual Environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file and add necessary environment variables.

4. **Run the Application**:
   ```sh
   python run.py
   ```

This structure organizes your application into manageable and modular components, making it easier to maintain and extend. It allows you to add additional models or functionalities without disrupting the existing codebase.