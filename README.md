# Abstractive-Summarization-and-Question-Answering-of-Medical-Texts-using-T5
## Overview
This project utilizes the T5 (Text-To-Text Transfer Transformer) model from Hugging Face Transformers to perform abstractive summarization and question answering on medical texts. The T5 model is fine-tuned on medical domain-specific data to generate concise summaries.

## Directory Structure

- `Datasets/`: Contains the datasets used for training and evaluation.
- `Scripts/`: Contains Jupyter notebooks and scripts for dataset creation and processing.

## Scripts

### Dataset Creation

#### `Dataset_Creation_Pubmed_Subset.ipynb`

This Jupyter notebook contains code for creating a dataset from PubMed XML files. The steps involved are:

1. **Setup**:
   - Import necessary libraries and set up the environment.
   - Mount Google Drive if running in Google Colab.

2. **Parsing XML Files**:
   - Functions to parse PubMed XML files and extract titles, abstracts, and body text.
   - Example usage to parse a single XML file and print the extracted data.

3. **Full Script to Parse All XML Files**:
   - Parse all XML files in a directory and store the extracted data in a DataFrame.
   - Save the parsed data to a CSV file.

4. **Simplifying Medical Terms**:
   - Load Consumer Health Vocabulary (CHV) dataset.
   - Replace complex medical terms in abstracts with simpler terms using CHV.
   - Save the simplified abstracts to a new CSV file.

5. **Cleaning Data**:
   - Drop rows where both the original and simplified abstracts are missing.
   - Save the cleaned data to a CSV file.

6. **Preparation for Training**:
   - Combine title, abstract, and body text into a single input string for T5 model training.
   - Save the prepared training data to a CSV file.