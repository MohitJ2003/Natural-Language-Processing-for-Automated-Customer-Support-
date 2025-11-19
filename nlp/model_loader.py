import torch
import torch.nn as nn

class RNNClassifier(nn.Module):
    def __init__(self, vocab_size=1000, embed_dim=64, hidden_dim=128, num_classes=5):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.rnn = nn.RNN(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, num_classes)

    def forward(self, x):
        emb = self.embedding(x)
        out, _ = self.rnn(emb)
        last = out[:, -1, :]
        return self.fc(last)

def load_intent_model(path="models/rnn_intent_model.pth"):
    model = RNNClassifier()
    try:
        model.load_state_dict(torch.load(path, map_location="cpu"))
        model.eval()
        print("Model loaded successfully.")
        return model
    except:
        print("Could not load trained model. Using untrained model instead.")
        return model
