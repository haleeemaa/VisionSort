from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from datetime import datetime

import shutil
import os
import sys

# Allow backend to import files from the project root
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from predict import predict_image

app = FastAPI()

MONGO_URI = "mongodb+srv://visionsort_user:CPuXDU44HZVdVt6o@cluster0.dpoh6ul.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client["visionsort_db"]
predictions_collection = db["predictions"]

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "VisionSort Backend Running"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    prediction, confidence = predict_image(file_path)

    suggestions = {
        "plastic": "Place in recycling bin.",
        "paper": "Recycle with paper waste.",
        "glass": "Dispose in glass recycling.",
        "metal": "Recycle as scrap metal.",
        "cardboard": "Flatten and recycle.",
        "trash": "Dispose in general waste."
    }

    predictions_collection.insert_one({
        "filename": file.filename,
        "prediction": prediction,
        "confidence": round(confidence * 100, 2),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    return {
        "prediction": prediction,
        "confidence": round(confidence * 100, 2),
        "suggestion": suggestions[prediction]
    }


@app.get("/history")
def get_history():
    records = list(predictions_collection.find({}, {"_id": 0}))
    return {"history": records}