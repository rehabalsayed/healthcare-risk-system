from fastapi import FastAPI , Depends

from prediction_service import predict_diabetes

from sqlalchemy.orm import Session

from database.database import get_db


from typing import List

from database.crud import (
    save_prediction,
    get_predictions,
    get_prediction_by_id
)

from schemas import (
    DiabetesRequest,
    DiabetesResponse,
    PredictionRecord
)

from database.database import Base, engine

from fastapi import HTTPException

app = FastAPI(
    title="Diabetes Risk Prediction API",
    description="Predict diabetes risk using CatBoost model",
    version="1.0"
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.post(
    "/predict",
    response_model=DiabetesResponse
)
def predict(
    data: DiabetesRequest,
    db: Session = Depends(get_db)
):

    result = predict_diabetes(data)

    save_prediction(
        db=db,
        request_data=data,
        result=result
    )

    return result

@app.get(
    "/predictions",
    response_model=List[PredictionRecord]
)
def read_predictions(
    db: Session = Depends(get_db)
):

    return get_predictions(db)

@app.get(
    "/predictions/{prediction_id}",
    response_model=PredictionRecord
)
def read_prediction(
    prediction_id: int,
    db: Session = Depends(get_db)
):

    prediction = get_prediction_by_id(
        db,
        prediction_id
    )

    if prediction is None:

        raise HTTPException(
            status_code=404,
            detail="Prediction not found"
        )

    return prediction