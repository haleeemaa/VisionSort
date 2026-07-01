# ♻️ VisionSort – AI-Based Waste Classification System

VisionSort is an AI-powered waste classification system that uses Deep Learning and Computer Vision to classify waste images into six categories: **Cardboard, Glass, Metal, Paper, Plastic, and Trash**. The application provides real-time predictions, confidence scores, and disposal suggestions through a simple web interface while storing prediction history in MongoDB Atlas.

---

## 📌 Project Description

Proper waste segregation is essential for effective recycling and environmental sustainability. Manual waste classification is time-consuming and prone to human error. VisionSort automates this process using a fine-tuned **ResNet18** deep learning model that accurately identifies waste categories from uploaded images.

The project integrates a machine learning model with a FastAPI backend, a responsive HTML/CSS/JavaScript frontend, and MongoDB Atlas for storing prediction history.

---

## ❗ Problem Statement

Manual waste segregation is inefficient, inconsistent, and difficult to scale. Incorrect disposal of recyclable materials contributes to environmental pollution and reduces recycling efficiency. An intelligent system is required to automatically classify waste and assist users in proper disposal.

---

## 🎯 Objectives

- Develop an AI model to classify waste images.
- Identify six categories of waste.
- Provide recycling and disposal suggestions.
- Store prediction history in MongoDB Atlas.
- Build a simple and user-friendly web application.

---

## ✨ Features

- Upload waste images through a web interface.
- AI-powered image classification using ResNet18.
- Displays prediction confidence score.
- Provides recycling/disposal suggestions.
- Stores prediction history in MongoDB Atlas.
- Interactive dashboard displaying prediction history.
- Pie chart visualization showing the distribution of classified waste categories.
- View historical predictions for analysis and monitoring.
- REST API developed using FastAPI.
- API testing using Swagger UI and Postman.

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- PyTorch
- TorchVision
- ResNet18 (Transfer Learning)

### Backend
- FastAPI
- Uvicorn

### Frontend
- HTML
- CSS
- JavaScript

### Database
- MongoDB Atlas
- PyMongo

### Tools
- Visual Studio Code
- Swagger UI
- Postman
- Git

---

## 📂 Dataset

The model is trained on a garbage classification dataset containing six waste categories:

- Cardboard
- Glass
- Metal
- Paper
- Plastic
- Trash

All images are preprocessed and resized to **224 × 224** pixels before training.

---

## ⚙️ Implementation

1. Collect and preprocess the waste image dataset.
2. Fine-tune a pre-trained ResNet18 model for six waste categories.
3. Save the trained model (`waste_model.pth`).
4. Develop a FastAPI backend to process uploaded images.
5. Predict the waste category using the trained model.
6. Return the prediction, confidence score, and disposal suggestion.
7. Store prediction details in MongoDB Atlas.
8. Retrieve prediction history using the `/history` API.

---

## 🔌 API Endpoints

### `POST /predict`

Uploads an image and returns:

- Predicted waste category
- Confidence score
- Recycling suggestion

### `GET /history`

Returns the history of all predictions stored in MongoDB Atlas.

---

## 🔄 Project Workflow

```text
User Uploads Image
        │
        ▼
Frontend (HTML/CSS/JavaScript)
        │
        ▼
FastAPI Backend
        │
        ▼
Image Preprocessing
        │
        ▼
ResNet18 Model
        │
        ▼
Prediction + Confidence + Suggestion
        │
        ├────────► Display Results
        │
        ▼
Store Prediction in MongoDB Atlas
```

---

## 🚀 Future Enhancements

- Real-time webcam-based waste detection.
- Mobile application support.
- Additional waste categories.
- Cloud deployment.
- User authentication.
- Analytics dashboard for prediction history.

---

## 📚 Conclusion

VisionSort demonstrates how Artificial Intelligence can be applied to automate waste classification and improve recycling practices. By integrating Deep Learning, FastAPI, MongoDB Atlas, and modern web technologies, the project provides an efficient, scalable, and user-friendly solution for smart waste management.

---

## 👩‍💻 Author

**Haleema**

AI & Machine Learning Project – VisionSort
