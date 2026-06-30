from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from database.database import Base


class Prediction(Base):

    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    
    full_name = Column(String)

    national_id = Column(String, unique=True)

    gender = Column(String)

    age = Column(Float)

    hypertension = Column(Integer)

    heart_disease = Column(Integer)

    smoking_history = Column(String)

    bmi = Column(Float)

    hba1c_level = Column(Float)

    blood_glucose_level = Column(Integer)

    prediction = Column(Integer)

    prediction_label = Column(String)

    risk_level = Column(String)

    probability = Column(Float)

    confidence = Column(Float)

    explanation = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )