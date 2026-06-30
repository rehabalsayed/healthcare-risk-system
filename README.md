🧠 Healthcare Risk Prediction System

A production-ready Machine Learning API built with FastAPI, CatBoost, and PostgreSQL, fully containerized using Docker Compose.
The system predicts diabetes risk based on patient health features and stores predictions in a database for tracking and analysis.

🚀 Features
📊 MLflow experiment tracking for model training, comparison, and selection
🔮 Real-time diabetes risk prediction using trained ML model (CatBoost)
⚡ FastAPI backend with automatic Swagger documentation
🗄️ PostgreSQL database for storing predictions
🐳 Fully containerized with Docker & Docker Compose
📊 ML pipeline with preprocessing + thresholding
🧾 Persistent prediction history API
🔐 Environment-based configuration (.env support)

🏗️ Tech Stack

📊 MLflow Experiment Tracking

This project integrates MLflow for end-to-end experiment tracking and model management.

It is used to:

🧪 Track multiple machine learning experiments (CatBoost, baseline models, etc.)
📈 Log and compare evaluation metrics (Accuracy, F1-score, ROC-AUC)
⚙️ Track hyperparameters for each run
💾 Store trained models 
🏆 Select and promote the best-performing model for deployment
🚀 MLflow UI

To launch the MLflow tracking UI locally:

mlflow ui

Then open:

http://127.0.0.1:5000
📁 Experiment Storage

All experiments are stored in:

experiments/mlruns/
🧠 MLflow Workflow
Train multiple models (e.g., Logistic Regression, Random Forest, CatBoost, xgboost)
Log parameters and metrics using MLflow
Compare runs visually using MLflow UI
Select the best model
Export best model artifact → used by FastAPI for inference

Backend: FastAPI, Python 3.10

ML Model: CatBoost / Scikit-learn pipeline

Database: PostgreSQL

ORM: SQLAlchemy

Containerization: Docker, Docker Compose

Others: Pydantic, Joblib, Uvicorn


📁 Project Structure
Healthcare-Risk-System/
│
├── src/
│   ├── app.py
│   ├── schemas/
│   ├── database/
│   ├── services/
│   ├── config.py
│   └── prediction_service.py
│   └── artifacts/
│       ├── model.pkl
│       ├── preprocessor.pkl
│       └── threshold.pkl

├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .env
└── README.md
⚙️ Environment Variables

Create a .env file in the root directory:

DATABASE_URL=postgresql://postgres:password@postgres:5432/healthcare_db


🐳 Run with Docker
1. Build & Start Containers
docker compose up --build

2. Run in background
docker compose up -d

3. Stop system
docker compose down

📡 API Endpoints
🔹 Health Check
GET /
🔹 Predict Diabetes Risk
POST /predict

Request Example
{
  "full_name": "Omar Ibrahim",
  "national_id": "30104051234567",
  "gender": "male",
  "age": 47,
  "hypertension": 1,
  "heart_disease": 0,
  "smoking_history": "former",
  "bmi": 29.4,
  "hba1c_level": 6.3,
  "blood_glucose_level": 155
}

Response Example
{
  "prediction": 0,
  "prediction_label": "Diabetes Unlikely",
  "risk_level": "Low Risk",
  "probability": 0.0959,
  "confidence": 90.41,
  "explanation": "The estimated risk remains relatively low..."
}

🔹 Get All Predictions
GET /predictions

🔹 Get Prediction by ID
GET /predictions/{id}


🗄️ Database
Automatically stores all predictions in PostgreSQL
Uses SQLAlchemy ORM

Tables are created using:
Base.metadata.create_all(bind=engine)
🧪 Testing the API

Open Swagger UI:

http://localhost:8000/docs
🐳 Docker Architecture
FastAPI Container  --->  PostgreSQL Container
        │                     │
        └──── Docker Network ─┘


🚀 Deployment (Render)

This project is production-ready and can be deployed on:

Render
Railway
AWS EC2
DigitalOcean


📌 Future Improvements
Add authentication (JWT)
Add monitoring (Prometheus + Grafana)
Expand MLflow tracking with model registry and production staging (Staging → Production)
Add CI/CD pipeline (GitHub Actions)
Add data validation layer
👩‍💻 Author

Built as a Machine Learning Portfolio Project demonstrating:

End-to-end ML pipeline
API development
Database integration
Containerization