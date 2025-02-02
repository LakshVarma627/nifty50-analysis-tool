from transformers import pipeline

def analyze_sentiment(text):
    sentiment_pipeline = pipeline("sentiment-analysis")
    return sentiment_pipeline(text)
