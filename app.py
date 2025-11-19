from flask import Flask, render_template, request, jsonify
from nlp.sentiment import analyze_sentiment
from nlp.intent import recognize_intent
from nlp.response_gen import generate_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def api_query():
    data = request.json or {}
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided.'}), 400

    sentiment = analyze_sentiment(text)
    intent = recognize_intent(text)
    response = generate_response(text, intent, sentiment)

    return jsonify({
        'text': text,
        'sentiment': sentiment,
        'intent': intent,
        'response': response
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
