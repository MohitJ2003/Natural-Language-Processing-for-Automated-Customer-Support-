# Placeholder sentiment analysis
# Replace with RNN/LSTM model inference later

def analyze_sentiment(text):
    text = (text or '').lower()
    # naive rule-based placeholder
    if any(w in text for w in ['bad', 'terrible', 'hate', 'angry', 'upset']):
        return {'label': 'negative', 'score': 0.9}
    if any(w in text for w in ['great', 'good', 'love', 'happy', 'excellent']):
        return {'label': 'positive', 'score': 0.9}
    return {'label': 'neutral', 'score': 0.6}
