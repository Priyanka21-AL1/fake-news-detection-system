import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

# Load datasets
fake_df = pd.read_csv("dataset/Fake.csv")
true_df = pd.read_csv("dataset/True.csv")

# Add labels
fake_df["label"] = 0
true_df["label"] = 1

# Merge datasets
df = pd.concat([fake_df, true_df], axis=0)

# Shuffle data and reset index
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Keep only required columns
df = df[["title", "text", "label"]]

# Check missing values
print(df.isnull().sum())

# Remove missing values
df = df.dropna().reset_index(drop=True)

# Combine title and text
df["content"] = df["title"] + " " + df["text"]

print(df[["content", "label"]].head())


# Load stopwords
stop_words = set(stopwords.words("english"))

# Text cleaning function
def clean_text(text):
    text = text.lower()                          # lowercase
    text = re.sub(r"http\S+", "", text)          # remove URLs
    text = re.sub(r"[^a-zA-Z\s]", " ", text)     # remove punctuation/numbers
    text = text.split()                          # split into words
    text = [word for word in text if word not in stop_words]
    return " ".join(text)

# Apply cleaning
df["content"] = df["content"].apply(clean_text)

# Check cleaned text
print(df[["content", "label"]].head())

# Apply cleaning to the text column
df["clean_text"] = df["text"].apply(clean_text)

# Check results
print(df[["text", "clean_text"]].head())



# Save cleaned dataset
df.to_csv(
    "dataset/cleaned_news.csv",
    index=False
)

print("Dataset cleaned successfully")