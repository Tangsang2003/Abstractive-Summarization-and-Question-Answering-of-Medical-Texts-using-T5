from app import create_app
from app.utils.summarization import load_summarization_model
from app.utils.question_answering import load_qa_model


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
