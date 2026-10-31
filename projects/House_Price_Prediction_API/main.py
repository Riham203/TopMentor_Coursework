import joblib
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize API
app = FastAPI(title="House Price Predictor API")

# Load saved model
model = joblib.load("model.pkl")


# Define expected input schema
class HouseFeatures(BaseModel):
    sqft: float
    bedrooms: int
    age: int


@app.get("/")
def home():
    return {"message": "Model API is running!"}


@app.post("/predict")
def predict_price(features: HouseFeatures):
    # Convert incoming data to array format expected by scikit-learn
    data = [[features.sqft, features.bedrooms, features.age]]
    prediction = model.predict(data)[0]

    return {
        "input": features.dict(),
        "estimated_price": round(float(prediction), 2),
    }