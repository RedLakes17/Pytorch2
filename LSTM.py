#Creemos una Long Short Term Memory
import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.lstm=nn.LSTM(
            input_size=1,
            hidden_size=32,
            num_layers=2,
            batch_first=True,
        )
        self,fc=nn.Linear(32,1)
    def forward(self,x):
        h0 = torch.zeros(2, x.size(0), 32)
        c0 = torch.zeros(2, x.size(0), 32)
        out,_ = self.lstm(x, (h0, c0))
        out = self.fc(out[:,-1,:])
        return out