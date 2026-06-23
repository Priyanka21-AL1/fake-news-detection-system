import pandas as pd
import re
import nltk
import joblib
import os

from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Download stopwords
nltk.download("stopwords")

# Load datasets
fake_df = pd.read_csv("dataset/Fake.csv")
true_df = pd.read_csv("dataset/True.csv")

# Add labels
fake_df["label"] = 0
true_df["label"] = 1

# Merge datasets
df = pd.concat([fake_df, true_df], axis=0)

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Keep required columns
df = df[["title", "text", "label"]]

# Remove missing values
df = df.dropna().reset_index(drop=True)

# Combine title and text
df["content"] = df["title"] + " " + df["text"]

# Load stopwords
stop_words = set(stopwords.words("english"))

# Text cleaning function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    words = text.split()
    words = [word for word in words if word not in stop_words]

    return " ".join(words)

# Clean text
df["clean_text"] = df["content"].apply(clean_text)

print("Dataset Loaded Successfully")
print("Total Records:", len(df))

# Features and Labels
X = df["clean_text"]
y = df["label"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_df=0.7
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print("Training TF-IDF Shape:", X_train_tfidf.shape)
print("Testing TF-IDF Shape:", X_test_tfidf.shape)

# -----------------------------
# Logistic Regression
# -----------------------------
lr = LogisticRegression(max_iter=1000)

print("Training Logistic Regression Model...")
lr.fit(X_train_tfidf, y_train)

lr_pred = lr.predict(X_test_tfidf)

lr_acc = accuracy_score(y_test, lr_pred)

print("Logistic Accuracy:", lr_acc)
print(f"Logistic Accuracy Percentage: {lr_acc * 100:.2f}%")

# -----------------------------
# Naive Bayes
# -----------------------------
nb = MultinomialNB()

print("Training Naive Bayes Model...")
nb.fit(X_train_tfidf, y_train)

nb_pred = nb.predict(X_test_tfidf)

nb_acc = accuracy_score(y_test, nb_pred)

print("Naive Bayes Accuracy:", nb_acc)
print(f"Naive Bayes Accuracy Percentage: {nb_acc * 100:.2f}%")

# -----------------------------
# Random Forest
# -----------------------------
rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

print("Training Random Forest Model...")
rf.fit(X_train_tfidf, y_train)

rf_pred = rf.predict(X_test_tfidf)

rf_acc = accuracy_score(y_test, rf_pred)

print("Random Forest Accuracy:", rf_acc)
print(f"Random Forest Accuracy Percentage: {rf_acc * 100:.2f}%")

# -----------------------------
# Model Comparison
# -----------------------------
print("\nMODEL COMPARISON")
print("-" * 35)

print(f"Logistic Regression : {lr_acc * 100:.2f}%")
print(f"Naive Bayes         : {nb_acc * 100:.2f}%")
print(f"Random Forest       : {rf_acc * 100:.2f}%")

scores = {
    "Logistic Regression": lr_acc,
    "Naive Bayes": nb_acc,
    "Random Forest": rf_acc
}

best_name = max(scores, key=scores.get)

if best_name == "Logistic Regression":
    best_model = lr
elif best_name == "Naive Bayes":
    best_model = nb
else:
    best_model = rf

print(f"\nBest Model: {best_name}")
print(f"Best Accuracy: {scores[best_name] * 100:.2f}%")

# Save cleaned dataset
df.to_csv("dataset/cleaned_news.csv", index=False)

# Create model directory
os.makedirs("model", exist_ok=True)

# Save best model and vectorizer
joblib.dump(best_model, "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")


print("\nTesting Saved Model...")

loaded_model = joblib.load("model/model.pkl")
loaded_vectorizer = joblib.load("model/vectorizer.pkl")

sample = [
    "Government launches new education policy."
]

sample_vector = loaded_vectorizer.transform(sample)

prediction = loaded_model.predict(sample_vector)

print("Prediction:", prediction)

print("\ncleaned_news.csv saved")
print("model/model.pkl saved")
print("model/vectorizer.pkl saved")
print("Training Completed Successfully!")