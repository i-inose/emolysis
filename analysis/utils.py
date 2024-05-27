from transformers import pipeline

# 感情分析モデルのロード
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
  result = sentiment_pipeline(text)
  return result[0]["label"], result[0]["score"]