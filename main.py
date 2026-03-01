# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np  # <-- necesario para usar arrays correctamente

app = FastAPI()

# Cargar modelo entrenado
model = joblib.load("trip_price_model.pkl")

class TripRequest(BaseModel):
    distance_km: float
    duration_min: float

@app.get("/")
def root():
    return {"message": "Taxi ML Service is running"}

@app.post("/predict")
def predict_price(trip: TripRequest):
    # Predecir usando ML real (usar np.array con shape correcto)
    features = np.array([[trip.distance_km, trip.duration_min]])
    estimated_price = model.predict(features)[0]
    return {"estimated_price": round(estimated_price, 2)}