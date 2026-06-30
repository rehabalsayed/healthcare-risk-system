from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime



# ==========================
# Enums (Dropdown lists)
# ==========================

class GenderEnum(str, Enum):
    male = "male"
    female = "female"


class SmokingHistoryEnum(str, Enum):
    never = "never"
    former = "former"
    current = "current"
    not_current = "not_current"
    ever = "ever"
    no_info = "no_info"


# ==========================
# Request Schema
# ==========================

class DiabetesRequest(BaseModel):
    
    full_name: str = Field(
    ...,
    min_length=3,
    max_length=100,
    description="Patient Full Name"
)

    national_id: str = Field(
        ...,
        min_length=10,
        max_length=20,
        description="National ID"
    )

    gender: GenderEnum

    age: float = Field(
        ...,
        ge=0,
        le=120,
        description="Age in years"
    )

    hypertension: int = Field(
        ...,
        ge=0,
        le=1,
        description="0 = No, 1 = Yes"
    )

    heart_disease: int = Field(
        ...,
        ge=0,
        le=1,
        description="0 = No, 1 = Yes"
    )

    smoking_history: SmokingHistoryEnum

    bmi: float = Field(
        ...,
        ge=10,
        le=80,
        description="Body Mass Index"
    )

    hba1c_level: float = Field(
        ...,
        ge=3,
        le=20,
        description="HbA1c percentage"
    )

    blood_glucose_level: int = Field(
        ...,
        ge=50,
        le=400,
        description="Blood glucose level"
    )
    
    
# ==========================
# Response Schema
# ==========================
class DiabetesResponse(BaseModel):

    prediction: int

    prediction_label: str

    risk_level: str

    probability: float

    confidence: float

    explanation: str
    
    


class PredictionRecord(BaseModel):

    id: int
    
    full_name: str

    national_id: str

    gender: str
    age: float

    hypertension: int
    heart_disease: int

    smoking_history: str

    bmi: float
    hba1c_level: float
    blood_glucose_level: int

    prediction: int
    prediction_label: str

    risk_level: str

    probability: float
    confidence: float

    explanation: str

    created_at: datetime

    class Config:
        from_attributes = True