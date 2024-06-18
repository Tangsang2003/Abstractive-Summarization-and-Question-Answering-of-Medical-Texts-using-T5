from app import create_app
import os
import warnings
from transformers import logging as transformers_logging


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow warnings
warnings.filterwarnings("ignore")  # Ignore all warnings
transformers_logging.set_verbosity_error()  # Set transformers verbosity to error only


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
