import joblib

loaded_model = joblib.load("model/model.pkl")
loaded_vectorizer = joblib.load("model/vectorizer.pkl")

sample_news = [
    "Government launches new education policy."
]

sample_vector = loaded_vectorizer.transform(sample_news)

prediction = loaded_model.predict(sample_vector)

print("Prediction:", prediction[0])