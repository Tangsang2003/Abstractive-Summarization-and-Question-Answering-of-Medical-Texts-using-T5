# MedEaseIne: Simplifying Medical Info
## Overview 🧐
**MedEaseIne**  ⭐ is a project aimed at summarizing medical texts and documents into patient-friendly summaries. It also facilitates question-answering based on medical context using state-of-the-art models. We have utilized the T5 (Text-To-Text Transfer Transformer) model from Hugging Face Transformers library to perform abstractive summarization and question answering on medical texts. The T5 model is fine-tuned on medical domain-specific data (the PubMed Subset Bulk and SumPubMed) to generate concise summaries. Likewise, we have also utilized Google Gemini API to extract information from texts or documents and summarize them into patient-friendly language as well as facilitate question-answering.

## Demo Video 📹
- The demo video can be found [here.](https://drive.google.com/drive/folders/1zFes1W1IBU5s50MBliVtcKaEum_ApEbZ?usp=drive_link)
- The slides can be found [here.](https://drive.google.com/drive/folders/1bAvogrEJLA1fIjyC_fcBPlkRimPSnN_B?usp=drive_link)

## Directory Structure 🗂️
```
.
├── app/
│   └── models/
│       ├── question_answering/
│       │   └── checkpoint-1500/
│       └── summarization/
│           └── summarization_final_trained_model
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── images/
│   └── js/
│       └── script.js
├── templates/
│   ├── about_us.html
│   ├── contact_us.html
│   ├── home.html
│   ├── layout.html
│   ├── qna.html
│   ├── result.html
│   └── summarize.html
├── utils/
│   ├── question_answering.py
│   └── summarization.py
├── __init__.py
├── forms.py
├── routes.py
├── scripts/
│   ├── dataset_creation_pubmed_subset.ipynb
│   ├── fine_tune_question_answer.ipynb
│   ├── finetuning_T5_for_summarization.ipynb
│   ├── subset_sumpubmed.py
│   └── sumpubmed_dataset_script.py
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── run.py
```


## Datasets and Fine-Tuning 🗄️
- All the datasets that were used to fine-tune our models can be found [here.](https://drive.google.com/drive/u/0/folders/1qLl840KFRAxMOW9BiVonUMCvYrl4yiED)
- All the scripts that were used to train our models can be found [here.](./scripts/)
- [This script](./scripts/dataset_creation_pubmed_subset.ipynb) was used to extract abstracts, and the whole content from PubMed articles and then the [CHV dataset](https://drive.google.com/file/d/1Og-Z7tRlRPppavl5JfBRd_pDuyOjEM9U/view?usp=drive_link) was used to replace complex terms with Consumer Vocabulary to simplify the abstracts. The simplified abstracts were used as target text to our T5-small model and the content were used as source.
- [This script](./scripts/subset_sumpubmed.py) and [this script](./scripts/sumpubmed_dataset_script.py) were used to create a subset of SumPubMed dataset.
- [This script](./scripts/finetuning_T5_for_summarization.ipynb) was used to fine-tune our T5-small model for summarization task in CoLab environment.
- [This script](./scripts/fine_tune_question_answer.ipynb) was used to fine-tune our T5-base model for the task of question-answering. [SQuAD](https://huggingface.co/datasets/rajpurkar/squad) dataset was used for the fine-tuning process.
  
## Features ⚙️
- **Medical Documents and Texts Summarization 📝:**
  - T5 for medical articles summarization.
  - Gemini for summary generation in patient-friendly language.
  - Gemini for summarization of medical documents like Discharge Summaries, Medical Histories, Diagnostic Reports, Clinical Notes, Treatment Plans, etc.
- **Question Answering ❓:**
  - Provides accurate answers to medical questions based on given medical contexts.
  - Provides user the flexibility to ask any question related to the context or some common Health queries.

## Tools and Technologies Used 🤖
- Python
- Flask
- HTML/CSS/JavaScript
- Pandas
- NumPy
- Tensorflow
- PyTorch
- Transformers
- Google Gemini API
- Google CoLab

## Installation 🛠️
#### 1. Clone the Repository:
 ```commandline
 git clone https://github.com/Tangsang2003/Abstractive-Summarization-and-Question-Answering-of-Medical-Texts-using-T5.git
 ```
 #### 2. Create Virtual Environment:
 - For Windows:
 ```commandline
 python -m venv venv
 ```
 -  For Linux and MacOS:
```commandline
python3 -m venv venv
```
- Activating the virtual environment
For Windows:
```commandline
venv\Scripts\activate
```
- For Linux and MacOS:
```commandline
source venv/bin/activate
```
#### 3. Install Dependencies
```commandline
pip install -r "requirements.txt"
```
#### 4. Download and configure ML models
- Go to app and create directories:
```
.
├── app/
│   └── models/
│       ├── question_answering/
│       │   └── checkpoint-1500/
│       └── summarization/
│           └── summarization_final_trained_model
```
```bash
$ cd app
$ mkdir models
$ cd models
$ mkdir question_answering
$ cd question_answering
$ mkdir checkpoint-1500
$ cd ..
$ mkdir summarization
$ cd summrization
$ mkdir summarization_final_trained_model
```
- Download T5 model for Summarization from [here.](https://drive.google.com/drive/folders/1R1o_CvddE3WdGy4YfpyWmT-4ZbiX5SwM?usp=drive_link)
- Copy all the files to the `summarization_final_trained_model` directory.
- Download T5 model for Question Answering from [here.](https://drive.google.com/drive/folders/1Clnbx3-xiX4M5VeOfi9lg5jl3r7SB8vL?usp=drive_link)
- Copy all the files to the `checkpoint-1500` directory.
- Obtain `GOOGLE_API_KEY` from [here.](https://aistudio.google.com/app/u/1/apikey)
- Setup the ` SECRET_KEY` and `GOOGLE_API_KEY` in your system's `Environment Variables`.
- You can set your `SECRET_KEY` to be anything. 

#### 5. Run Application
```console
python run.py
```
## Contributing 🤝
If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## Future Works? 🔜
- Development of a user feedback mechanism to improve our T5 model for summarization and question-answering.
- Creation of further-refined datasets.
- Deployment of the web application on AWS, Azure or Google Cloud.
- Explore partnerships with healthcare institutions, research organizations, or educational platforms to integrate MedEaseIne into clinical workflows, medical education, or research activities.

## Thank You 🙏
