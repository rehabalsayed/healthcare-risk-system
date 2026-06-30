from sqlalchemy.orm import Session

from database.models import Prediction


def save_prediction(
    db: Session,
    request_data,
    result
):

    record = Prediction(
        
        full_name=request_data.full_name,
        national_id=request_data.national_id,
        gender=request_data.gender,
        age=request_data.age,
        hypertension=request_data.hypertension,
        heart_disease=request_data.heart_disease,
        smoking_history=request_data.smoking_history,
        bmi=request_data.bmi,
        hba1c_level=request_data.hba1c_level,
        blood_glucose_level=request_data.blood_glucose_level,

        prediction=result["prediction"],
        prediction_label=result["prediction_label"],
        risk_level=result["risk_level"],
        probability=result["probability"],
        confidence=result["confidence"],
        explanation=result["explanation"]
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record



def get_predictions(db):
    return db.query(Prediction).all()


def get_prediction_by_id(db, prediction_id):
    return (
        db.query(Prediction)
        .filter(Prediction.id == prediction_id)
        .first()
    )