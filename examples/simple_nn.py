import torch
from hof_cognition import CognitiveAgent

# Initialize the cognitive agent
agent = CognitiveAgent()

# Define a simple neural network
class SimpleNN(torch.nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = torch.nn.Linear(10, 50)
        self.fc2 = torch.nn.Linear(50, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Instantiate the neural network
model = SimpleNN()

# Perform a cognitive task
input_data = torch.randn(1, 10)
result = agent.perform_task(model, input_data)
print(result)
