import re

POSITIVE_WORDS = {
    "shiny", "elegant", "premium", "beautiful", "comfortable",
    "perfect", "amazing", "love", "great", "excellent"
}

NEGATIVE_WORDS = {
    "tarnish", "dull", "heavy", "broke", "uncomfortable",
    "bad", "poor", "cheap", "worst", "disappointed"
}

def analyze_sentiment(review_text: str):
    words = re.findall(r'\b\w+\b', review_text.lower())

    positive_count = sum(1 for w in words if w in POSITIVE_WORDS)
    negative_count = sum(1 for w in words if w in NEGATIVE_WORDS)

    if positive_count > negative_count:
        sentiment = "Positive"
    elif negative_count > positive_count:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, positive_count, negative_count
