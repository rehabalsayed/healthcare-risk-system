import joblib
import pandas as pd

from schemas import DiabetesRequest
from config import (
    MODEL_PATH,
    PREPROCESSOR_PATH,
    THRESHOLD_PATH
)


# ======================
# Load artifacts
# ======================
model = joblib.load(MODEL_PATH)

preprocessor = joblib.load(PREPROCESSOR_PATH)

threshold = joblib.load(THRESHOLD_PATH)


# ======================
# Prediction function
# ======================
def predict_diabetes(data: DiabetesRequest):

    input_df = pd.DataFrame(
        [{
            "gender": data.gender,
            "age": data.age,
            "hypertension": data.hypertension,
            "heart_disease": data.heart_disease,
            "smoking_history": data.smoking_history,
            "bmi": data.bmi,
            "HbA1c_level": data.hba1c_level,
            "blood_glucose_level": data.blood_glucose_level
        }]
    )

    # preprocessing
    X = preprocessor.transform(input_df)

    probability = float(model.predict_proba(X)[:, 1][0])

    confidence = float(
    max(probability, 1 - probability) * 100
    )

    # prediction
    prediction = int(probability >= threshold)

    # risk level
    if probability < 0.30:
        risk_level = "Low Risk"

    elif probability < 0.60:
        risk_level = "Moderate Risk"

    else:
        risk_level = "High Risk"

    # -------------------------
    # Build explanation
    # -------------------------
    reasons = []

    if data.blood_glucose_level >= 140:
        reasons.append("elevated blood glucose")

    if data.hba1c_level >= 6.5:
        reasons.append("high HbA1c level")

    if data.bmi >= 30:
        reasons.append("high BMI")

    if data.hypertension == 1:
        reasons.append("history of hypertension")

    if data.heart_disease == 1:
        reasons.append("history of heart disease")

    if data.age >= 50:
        reasons.append("older age")

    # explanation
    if prediction == 1:

        if reasons:

            explanation = (
                "The estimated risk is elevated, mainly due to "
                + ", ".join(reasons)
                + "."
            )

        else:

            explanation = (
                "The model estimates an elevated probability of diabetes "
                "based on the overall pattern of the provided measurements."
            )

    else:

        if reasons:

            explanation = (
                "The estimated risk remains relatively low, although factors such as "
                + ", ".join(reasons)
                + " are present."
            )

        else:

            explanation = (
                "The provided measurements are generally associated with a lower probability of diabetes."
            )
            
    prediction_label = (
    "Diabetes Likely"
    if prediction == 1
    else "Diabetes Unlikely"
) 
    
    response = {
    "prediction": prediction,
    "prediction_label": prediction_label,
    "risk_level": risk_level,
    "probability": round(probability, 4),
    "confidence": round(max(probability, 1 - probability) * 100, 2),
    "explanation": explanation
}

    return response