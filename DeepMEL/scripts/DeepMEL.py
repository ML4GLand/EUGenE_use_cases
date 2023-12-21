import torch
import torch.nn as nn
import torch.nn.functional as F

class BiDirectionalModel(nn.Module):
    def __init__(self, seq_shape, num_classes):
        super(BiDirectionalModel, self).__init__()
        self.conv1 = nn.Conv1d(seq_shape[0], 128, kernel_size=20)
        self.pool = nn.MaxPool1d(10, 10)
        self.dropout1 = nn.Dropout(0.2)
        # TimeDistributed layer is not directly available in PyTorch
        self.dense1 = nn.Linear(??? , 128) # You need to calculate the input size here
        self.lstm = nn.LSTM(128, 128, batch_first=True, bidirectional=True, dropout=0.1)
        self.dropout2 = nn.Dropout(0.2)
        self.flatten = nn.Flatten()
        self.dense2 = nn.Linear(??? , 256) # You need to calculate the input size here
        self.dropout3 = nn.Dropout(0.4)
        self.output_layer = nn.Linear(256, num_classes)
    
    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.pool(x)
        x = self.dropout1(x)
        x = x.permute(0, 2, 1) # Reshape for TimeDistributed
        # Apply TimeDistributed
        batch_size, seq_len, _ = x.size()
        x = x.contiguous().view(batch_size * seq_len, -1)
        x = F.relu(self.dense1(x))
        x = x.view(batch_size, seq_len, -1)
        x, _ = self.lstm(x)
        x = self.dropout2(x)
        x = self.flatten(x)
        x = F.relu(self.dense2(x))
        x = self.dropout3(x)
        x = self.output_layer(x)
        return x

# Instantiate the model
seq_shape = [???] # Fill in sequence shape
num_classes = len(selected_classes)
model = BiDirectionalModel(seq_shape, num_classes)