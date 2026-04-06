import torch
import torchvision.transforms as transforms
from PIL import Image
import torch.nn as nn

# Same model architecture
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 3)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 64, 3)
        self.fc1 = nn.Linear(64 * 6 * 6, 64)
        self.fc2 = nn.Linear(64, 10)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 64 * 6 * 6)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Load model
model = Net()
model.load_state_dict(torch.load("model/model.pth"))
model.eval()

classes = [
    "airplane","car","bird","cat","deer",
    "dog","frog","horse","ship","truck"
]

transform = transforms.Compose([
    transforms.Resize((32,32)),
    transforms.ToTensor()
])

def predict_image(img_path):
    img = Image.open(img_path).convert("RGB")
    img = transform(img).unsqueeze(0)

    with torch.no_grad():
        outputs = model(img)
        _, predicted = torch.max(outputs, 1)

    return classes[predicted.item()]