from textblob import TextBlob

def analyze_mood(text, image=None):
    if text:
        sentiment = TextBlob(text).sentiment.polarity
        if sentiment > 0.1:
            return "happy"
        elif sentiment < -0.1:
            return "sad"
    return "neutral"
