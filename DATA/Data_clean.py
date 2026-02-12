import numpy as np
import pandas as pd
import kagglehub
import os

# Download dataset
path = kagglehub.dataset_download("jawadaahmed/business-intelligence-chatbot-interaction-dataset")

print("Dataset downloaded to:", path)


files = os.listdir(path)
print("Files in folder:", files)


csv_files = [f for f in files if f.endswith(".csv")]


df = pd.read_csv(os.path.join(path,csv_files[0]))
print(df.head())
    
print("Missing values in each column:")
print(df.isnull().sum())

df['user_feedback_rating'].fillna(df['user_feedback_rating'].mean(),inplace=True)

# df['user_feedback_rating'].fillna