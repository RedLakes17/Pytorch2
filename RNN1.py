import torch.nn as nn
import torch

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.rnn=nn.RNN(
            input_size=1,
            hidden_size=32,
            num_layers=2,
            batch_first=True,
        )
        self.fc=nn.Linear(32,1)
    def forward(self, x):
        h0 = torch.zeros(2, x.size(0), 32)
        out, _=self.rnn(x, h0)
        out=self.fc(out[:,-1,:])
        return out
