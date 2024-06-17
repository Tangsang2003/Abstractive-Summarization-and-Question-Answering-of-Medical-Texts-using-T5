# This script combines the articles body, and their corresponding abstracts/summaries
import os
import pandas as pd

# Directory paths for text and abstract folders
text_folder = 'D:\Projects\VivekaHack1\Datasets\sumpubmed//text'
abstract_folder = 'D:\Projects\VivekaHack1\Datasets\sumpubmed//shorter_abstract'

# List all files in text and abstract folders
text_files = sorted(os.listdir(text_folder))
abstract_files = sorted(os.listdir(abstract_folder))

# Initialize lists to store data
articles = []
abstracts = []

# Read each file from text folder and abstract folder
for text_file, abstract_file in zip(text_files, abstract_files):
    text_file_path = os.path.join(text_folder, text_file)
    abstract_file_path = os.path.join(abstract_folder, abstract_file)

    # Read text file (article)
    with open(text_file_path, 'r', encoding='utf-8') as file:
        article_content = file.read()

    # Read abstract file
    with open(abstract_file_path, 'r', encoding='utf-8') as file:
        abstract_content = file.read()

    # Append to lists
    articles.append(article_content)
    abstracts.append(abstract_content)

# Create DataFrame
df = pd.DataFrame({
    'article': articles,
    'abstract': abstracts
})

# Save DataFrame to CSV
csv_path = 'D:/Projects/VivekaHack1/training_dataset.csv'
df.to_csv(csv_path, index=False)

print(f"Dataset created with {len(df)} examples.")
print(df.head())
