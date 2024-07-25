import torch
import torch.optim as optim
from hof_cognition import CognitiveAgent

# Initialize the cognitive agent
agent = CognitiveAgent()

# Define a neural network
class AdvancedNN(torch.nn.Module):
    def __init__(self):
        super(AdvancedNN, self).__init__()
        self.fc1 = torch.nn.Linear(10, 100)
        self.fc2 = torch.nn.Linear(100, 50)
        self.fc3 = torch.nn.Linear(50, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Instantiate the neural network
model = AdvancedNN()

# Define loss function and optimizer
criterion = torch.nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
for epoch in range(100):
    optimizer.zero_grad()
    input_data = torch.randn(10)
    target = torch.randn(1)
    output = model(input_data)
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')
      
