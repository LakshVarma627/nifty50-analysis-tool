from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tensorflow as tf
import numpy as np

app = FastAPI()

class PredictionRequest(BaseModel):
    data: list

class PredictionResponse(BaseModel):
    prediction: float

model = tf.keras.models.load_model('path_to_your_model.h5')

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    try:
        input_data = np.array(request.data).reshape(1, -1)
        prediction = model.predict(input_data)
        return PredictionResponse(prediction=prediction[0][0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
