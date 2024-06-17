# This script extracts only 5000 of the SumPubMed dataset
import pandas as pd

# Load the entire dataset from training_data.csv
df = pd.read_csv('D:/Projects/VivekaHack1/training_dataset.csv')

# Select approximately 5000 examples
num_examples = 5000
df_sampled = df.sample(n=num_examples, random_state=1)  # Use random_state for reproducibility

# Save the sampled dataset to a new CSV file
df_sampled.to_csv('training_data_5000.csv', index=False)

print(f"Successfully sampled {num_examples} examples and saved to training_data_5000.csv.")
