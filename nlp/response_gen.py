# Placeholder response generation
# Replace with seq2seq / transformer or RNN generation later

def generate_response(text, intent, sentiment):
    intent_name = intent.get('intent') if isinstance(intent, dict) else intent
    if intent_name == 'greeting':
        return 'Hello! How can I help you today?'
    if intent_name == 'order_status':
        return 'I can help track your order. Please provide your order ID.'
    if intent_name == 'refund':
        return 'I\'m sorry to hear that. Please share your order ID and reason for refund.'
    if intent_name == 'goodbye':
        return 'Goodbye! Have a great day.'
    # fallback
    if sentiment.get('label') == 'negative':
        return 'I\'m sorry you had a bad experience. Could you share more details?'
    return 'Thanks for reaching out — can you give more details so I can assist?'
