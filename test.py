import joblib

# Cargar el modelo
model = joblib.load("trip_price_model.pkl")

# Ver coeficientes y intercept
print("Coeficientes:", model.coef_)
print("Intercept:", model.intercept_)
print("Número de features:", model.n_features_in_)