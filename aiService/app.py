# app.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load trained model
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

app = FastAPI()

# Request Body
class NewsRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Fake News Detection API Running"}

@app.post("/predict")
def predict(news: NewsRequest):

    text_vector = vectorizer.transform([news.text])

    prediction = model.predict(text_vector)[0]

    probability = model.predict_proba(text_vector)

    confidence = round(
        max(probability[0]) * 100,
        2
    )

    result = "Fake" if prediction == 0 else "Real"

    return {
        "prediction": result,
        "confidence": f"{confidence}%"
    }