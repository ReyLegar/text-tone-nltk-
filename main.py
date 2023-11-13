from fastapi import FastAPI
from pydantic import BaseModel
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    probabilities: list

sia = SentimentIntensityAnalyzer()

app = FastAPI()

@app.post('/sentiment')
def classify_sentiment(request: SentimentRequest):

    sentiment_score = sia.polarity_scores(request.text)

    print("Тональность текста:", sentiment_score)

    compound_score = sentiment_score['compound']

    if compound_score >= 0.05:
        emotion = "Положительная"
    elif compound_score <= -0.05:
        emotion = "Отрицательная"
    else:
        emotion = "Нейтральная"

    result = {"Emotion": emotion}
    return result