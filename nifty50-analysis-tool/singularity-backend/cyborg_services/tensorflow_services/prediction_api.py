import tensorflow as tf
from tensorflow.keras.models import load_model
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np

app = FastAPI()

class PredictionRequest(BaseModel):
    data: list

class PredictionResponse(BaseModel):
    prediction: float

model = load_model('path_to_your_model.h5')

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    try:
        data = np.array(request.data).reshape(1, -1)
        prediction = model.predict(data)
        return PredictionResponse(prediction=prediction[0][0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
