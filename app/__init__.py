# app/__init__.py
import os
from flask import Flask


def create_app():
    app = Flask(__name__)

    # Configuration settings and other setups can go here
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['DEBUG'] = True  # Enable debug mode
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    # Load models during app startup
    from app.utils.summarization import load_summarization_model
    from app.utils.question_answering import load_qa_model

    with app.app_context():
        app.summarization_model = load_summarization_model()
        app.qa_model = load_qa_model()

    return app
