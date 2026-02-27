# Taxi ML Service

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

Servicio de Machine Learning para la predicción de precios de taxis, construido con FastAPI y Scikit-Learn.

## 📋 Descripción

Este proyecto permite entrenar un modelo de predicción de precios basado en datos históricos y exponerlo a través de una API REST.

Los componentes principales son:
- **`train_model.py`**: Script de entrenamiento. Conecta a una base de datos PostgreSQL, lee la tabla `trips` y entrena un modelo de Regresión Lineal.
- **`main.py`**: API REST. Carga el modelo serializado y ofrece un endpoint para realizar predicciones.

## 🚀 Instalación

1. Clona el repositorio.
2. Instala las dependencias necesarias:

```bash
pip install pandas sqlalchemy scikit-learn joblib fastapi uvicorn psycopg2-binary
```

## ⚙️ Uso

### 1. Entrenar el Modelo

Asegúrate de tener una base de datos PostgreSQL corriendo en `localhost:5432` con el nombre `taxi_db` y las credenciales configuradas en `train_model.py`.

```bash
python train_model.py
```

Al finalizar, se creará el archivo `trip_price_model.pkl`.

### 2. Iniciar la API

```bash
uvicorn main:app --reload
```

El servidor se iniciará en `http://127.0.0.1:8000`.

## 📡 Endpoints

- **GET /**: Comprobación de estado.
- **POST /predict**: Predicción de precio.

  **Body:**
  ```json
  {
    "distance_km": 5.2,
    "duration_min": 15.0
  }
  ```