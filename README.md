# RNN-NLP Customer Support (Flask) - Project Skeleton

This repository is a minimal skeleton for a Flask-based project that will implement
an RNN-based NLP system for automating customer support (sentiment analysis,
intent recognition, response generation). All code is intentionally simple/placeholder
so you can expand later.

## Structure
- app.py - Flask app (simple routes)
- requirements.txt - Python deps
- nlp/ - placeholder NLP modules (sentiment, intent, response generation)
- models/ - placeholder for trained models
- templates/ - Flask HTML templates
- static/ - static assets (CSS/JS)
- utils/ - helper utilities
- tests/ - basic test skeleton
- Dockerfile - optional containerization

# 🧠 NLP Customer Support System — Libraries & Concepts

## 📌 1. Programming Language
- **Python 3.x**

---

# 📚 2. Libraries Used

## 🔧 Backend Framework
### **Flask**
Used to create the REST API and web interface.
- `Flask`
- `render_template`
- `request`
- `jsonify`

---

## 🤖 Machine Learning / Deep Learning
### **PyTorch**
Used to build and train the RNN model.
- `torch`
- `torch.nn`
- `torch.optim`
- `torch.utils.data`

---

## 🔤 NLP Processing
### **NLTK**
Used for tokenization and basic preprocessing.
- `nltk.tokenize.word_tokenize`

### Collections
- `Counter` (building vocabulary)

---

## 📁 Utility Libraries
- `os` — file handling
- `pickle` — saving/loading vocabulary

---

# 🧩 3. Core Concepts Used

## **1. Natural Language Processing (NLP)**
Steps included:
- Tokenization  
- Vocabulary building  
- Text-to-sequence conversion  
- Padding sequences  

---

## **2. Recurrent Neural Networks (RNNs)**
Model components:
- **Embedding Layer** — converts word indices to dense vectors  
- **RNN Layer** — learns sequential patterns from text  
- **Linear Layer** — predicts final sentiment class  

---

## **3. Intent Recognition (Rule-Based)**
Keyword matching to detect:
- Greeting  
- Tracking / Order Status  
- Refund  
- Goodbye  
- Unknown  

---

## **4. Sentiment Analysis**
RNN model predicts:
- Positive  
- Neutral  
- Negative  

---

## **5. Response Generation (Template-Based)**
Static responses based on detected intent.
Examples:
- Refund → “Please share your order ID…”  
- Greeting → “Hello! How can I assist you today?”  

---

## **6. REST API + Web Interface**
Flask routes:
- **GET /** → loads home page  
- **POST /predict** → returns sentiment, intent, response  

---

## **7. Model Persistence**
Saving/loading:
- `.pt` (model weights)  
- `.pkl` (vocabulary file)

---

# 🧪 8. Training Concepts
Used in `train_rnn.py`:
- Dataset + DataLoader  
- Loss: **CrossEntropyLoss**  
- Optimizer: **Adam**  
- Training loop  
- Saving trained model  

