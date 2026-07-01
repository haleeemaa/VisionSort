import torch

from torchvision import datasets
from torch.utils.data import DataLoader

from models import create_model
from utils import transform

dataset = datasets.ImageFolder(
    "dataset",
    transform=transform
)

loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True
)

model = create_model()

criterion = torch.nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.0001
)

epochs = 5

for epoch in range(epochs):

    running_loss = 0

    for images, labels in loader:

        outputs = model(images)

        loss = criterion(outputs, labels)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

    print(
        f"Epoch {epoch+1}/{epochs} Loss: {running_loss:.4f}"
    )

torch.save(
    model.state_dict(),
    "waste_model.pth"
)

print("Training Complete!")