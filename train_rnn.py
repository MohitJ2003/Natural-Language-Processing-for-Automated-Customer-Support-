# Simple RNN training skeleton (PyTorch)
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

class SimpleTextDataset(Dataset):
    def __init__(self, samples):
        self.samples = samples

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        return self.samples[idx]

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

def train_model():
    model = RNNClassifier()
    optim = torch.optim.Adam(model.parameters(), lr=0.001)
    loss_fn = nn.CrossEntropyLoss()

    samples = []  # TODO: Replace



    samples = [
    (torch.randint(0, 1000, (5,)), torch.tensor(0)),  # greeting
    (torch.randint(0, 1000, (5,)), torch.tensor(1)),  # goodbye
    (torch.randint(0, 1000, (5,)), torch.tensor(2)),  # order_status
    (torch.randint(0, 1000, (5,)), torch.tensor(3)),  # refund
    (torch.randint(0, 1000, (5,)), torch.tensor(4)),  # unknown
        ]

    dataset = SimpleTextDataset(samples)
    loader = DataLoader(dataset, batch_size=4, shuffle=True)

    for epoch in range(3):
        for X, y in loader:
            optim.zero_grad()
            logits = model(X)
            loss = loss_fn(logits, y)
            loss.backward()
            optim.step()
        print(f"Epoch {epoch} completed")

    torch.save(model.state_dict(), "models/rnn_intent_model.pth")
    print("Model saved to models/rnn_intent_model.pth")

if __name__ == "__main__":
    train_model()
