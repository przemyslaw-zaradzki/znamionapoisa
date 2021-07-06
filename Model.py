import torch
import torch.nn as nn
import torchvision
from torchvision import transforms
import numpy as np
from PIL import Image

FILE = "model_16_2021_05_19__10_26_59.pth"
device = torch.device("cpu")

height = 224
width = 224

model = torchvision.models.resnet18(pretrained=True)
for param in model.parameters():
    param.required_grad = False
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 7)

model.load_state_dict(torch.load(FILE, map_location=device))
model.eval()

def transforms_array(image_array):
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])

    transformer = transforms.Compose([
        transforms.Resize((height, width)),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)]
    )

    image = Image.open(image_array)
    return transformer(image).unsqueeze(0)

def get_prediction(image_tensor):
    images = image_tensor
    outputs = model(images)
    probabilities = nn.Softmax(1)(outputs)
    _, predictions = torch.max(outputs, 1)
    return predictions, probabilities.tolist()[0]