import os
import torch
from PIL import Image

from models import create_model
from utils import transform, classes

# Get the absolute path of the project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to the trained model
MODEL_PATH = os.path.join(BASE_DIR, "waste_model.pth")

# Load the trained model
model = create_model()
model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device("cpu")))
model.eval()


def predict_image(image_path):
    """
    Predict the waste category of an image.

    Args:
        image_path (str): Path to the uploaded image.

    Returns:
        tuple: (prediction, confidence)
    """

    # Open image
    image = Image.open(image_path).convert("RGB")

    # Apply the same preprocessing used during training
    image = transform(image)

    # Add batch dimension
    image = image.unsqueeze(0)

    # Disable gradient calculation for inference
    with torch.no_grad():
        outputs = model(image)

        probabilities = torch.softmax(outputs, dim=1)

        confidence, predicted = torch.max(probabilities, 1)

    prediction = classes[predicted.item()]

    return prediction, confidence.item()