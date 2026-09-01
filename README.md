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

### DevOps & Cloud
- **Docker** — Containerization
- **Docker Compose** — Running frontend and backend as separate services
- **AWS EC2** — Cloud deployment
- **Ubuntu** — Operating system used on the EC2 instance
- **SSH** — Secure connection to the EC2 server

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

##  Deployment 

The FastAPI backend and trained Machine Learning model were containerized using Docker and deployed on an AWS EC2 instance.

### Deployment Flow

```text
Local Development
       │
       ▼
Docker Image
       │
       ▼
Docker Hub
       │
       ▼
AWS EC2
       │
       ▼
Docker Container
       │
       ▼
FastAPI + ML Model
       │
       ▼
Streamlit Frontend
```

### Steps

1. Built separate Docker images for the FastAPI backend and Streamlit frontend
2. Pushed the images to Docker Hub
3. Launched an AWS EC2 (Ubuntu) instance
4. Connected to the instance via SSH
5. Pulled the Docker images onto the EC2 instance
6. Ran the containers using Docker Compose
7. Exposed the required ports to access the app publicly

---