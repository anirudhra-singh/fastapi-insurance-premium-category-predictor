#  Insurance Premium Category Predictor

A **Machine Learning + FastAPI + Streamlit** application that predicts an insurance premium category — **Low, Medium, or High** — based on a user's personal, lifestyle, and professional information.

This is a **learning project** I built to understand how a trained Machine Learning model can be integrated into a backend API, connected to a frontend, and containerized using Docker.

---

## 🛠️ Tech Stack

### Backend
- **FastAPI** — REST API and ML model serving
- **Pydantic** — Input validation and feature calculation
- **Uvicorn** — ASGI server for running the FastAPI application

### Frontend
- **Streamlit** — Interactive web interface
- **Requests** — Communication between Streamlit and FastAPI

### Machine Learning
- **Scikit-learn** — Machine Learning model
- **Pandas** — Data processing and preparing model input
- **NumPy** — Numerical operations
- **Pickle** — Saving and loading the trained ML model
- **Jupyter Notebook** — Model development and experimentation

### DevOps
- **Docker** — Containerization
- **Docker Compose** — Running the FastAPI backend and Streamlit frontend together

### Tools
- **Git & GitHub** — Version control
- **Swagger UI** — Testing and exploring FastAPI endpoints

##  Project Overview

The application takes user information such as:

- Age
- Weight
- Height
- Annual Income
- Smoking status
- City
- Occupation

The backend validates the input and automatically derives additional features such as:

- **BMI**
- **Age Group**
- **Lifestyle Risk**
- **City Tier**

These features are passed to the trained Machine Learning model, which predicts the user's **premium category**.

The application also displays:

- **Predicted category**
- **Confidence score**
- **Class probabilities**

---

##  How It Works

```text
User enters details
        │
        ▼
Streamlit Frontend
        │
        │ HTTP POST /predict
        ▼
FastAPI Backend
        │
        ▼
Pydantic Validation
        │
        ▼
Feature Calculation
        │
        ├── BMI
        ├── Age Group
        ├── Lifestyle Risk
        └── City Tier
        │
        ▼
Trained ML Model
        │
        ▼
Prediction Result
        │
        ├── Premium Category
        ├── Confidence Score
        └── Class Probabilities
        │
        ▼
Streamlit Dashboard