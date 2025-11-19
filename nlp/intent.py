from .model_loader import load_intent_model
import torch

INTENT_LABELS = ["greeting", "goodbye", "order_status", "refund", "unknown"]

model = load_intent_model()

def simple_rule_intent(text):
    t = text.lower()
    if "hi" in t or "hello" in t:
        return "greeting"
    if "bye" in t:
        return "goodbye"
    if "order" in t:
        return "order_status"
    if "refund" in t:
        return "refund"
    return "unknown"

def recognize_intent(text):
    try:
        x = torch.randint(0, 1000, (1, 5))
        logits = model(x)
        idx = torch.argmax(logits, dim=1).item()
        return {"intent": INTENT_LABELS[idx], "confidence": 0.8}
    except:
        return {"intent": simple_rule_intent(text), "confidence": 0.5}
