# train_model.py
import pandas as pd
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
import joblib

# 1. Conectar a Postgres
engine = create_engine("postgresql://postgres:admin@localhost:5432/taxi_db")

# 2. Leer datos históricos de la tabla de predicciones
df = pd.read_sql("SELECT distance_km, duration_min, estimated_price FROM trips", engine)

# 3. Separar features y target
X = df[["distance_km", "duration_min"]]
y = df["estimated_price"]

# 4. Entrenar modelo
model = LinearRegression()
model.fit(X, y)

# 5. Guardar modelo entrenado a disco
joblib.dump(model, "trip_price_model.pkl")

print("Modelo entrenado y guardado ✅")