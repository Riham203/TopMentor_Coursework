# House Price Prediction API

## Project Overview

This project is a machine learning-based **House Price Prediction API** built using Python, Scikit-learn, and FastAPI.

It uses a Linear Regression model to estimate house prices based on three input features: square footage, number of bedrooms, and age of the house.

The trained model is saved using Joblib and deployed as a REST API, allowing users to send house details through an HTTP POST request and receive an estimated price in response.

## Features

- **Machine Learning Model:** Uses Linear Regression to predict house prices.
- **Model Serialization:** Saves and loads the trained model using Joblib.
- **REST API:** Exposes prediction functionality through FastAPI.
- **Input Validation:** Uses Pydantic to validate incoming house features.
- **Prediction Endpoint:** Accepts house details and returns an estimated price.
- **API Testing:** Includes a Python script to test the deployed API.

## Input Features

| Feature | Description | Data Type |
|---|---|---|
| `sqft` | Square footage of the house | Float |
| `bedrooms` | Number of bedrooms | Integer |
| `age` | Age of the house | Integer |

## Machine Learning Model

**Algorithm:** Linear Regression

The model is trained using a small sample dataset containing six house records.

### Training Features
- Square Feet
- Number of Bedrooms
- Age of House

### Target Variable
- House Price (USD)

The trained model is saved as `model.pkl` using Joblib and loaded by the FastAPI application for predictions.

## API Endpoints

### 1. Home Endpoint

**Method:** GET

```text
/
```

Returns a message confirming that the API is running.

Example response:

```json
{
  "message": "Model API is running!"
}
```

### 2. House Price Prediction

**Method:** POST

```text
/predict
```

Example request:

```json
{
  "sqft": 1500,
  "bedrooms": 2,
  "age": 2
}
```

Example response structure:

```json
{
  "input": {
    "sqft": 1500,
    "bedrooms": 2,
    "age": 2
  },
  "estimated_price": 000000.00
}
```

The actual estimated price is calculated by the trained model.

## Tools & Technologies

- **Python** – Programming language
- **NumPy** – Numerical operations
- **Pandas** – Data manipulation
- **Scikit-learn** – Linear Regression model
- **Joblib** – Model serialization
- **FastAPI** – REST API development
- **Uvicorn** – ASGI server
- **Requests** – API testing

## Project Structure

```text
House_Price_Prediction_API/
│
├── main.py
├── train_model.py
├── test_api.py
├── requirements.txt
├── model.pkl              # Generated after model training
└── README.md
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
```

### 2. Navigate to the Project Folder

```bash
cd TopMentor_Coursework/projects/House_Price_Prediction_API
```

Adjust the folder name if your actual GitHub project folder uses a different name.

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**macOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## How to Run

### Step 1: Train the Model

```bash
python train_model.py
```

This trains the Linear Regression model and generates `model.pkl`.

### Step 2: Start the FastAPI Server

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### Step 3: Explore API Documentation

Open the interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

You can test the `/predict` endpoint directly from the browser.

### Step 4: Test the API

Run:

```bash
python test_api.py
```

The test script sends a POST request to the configured API URL and prints the JSON response.

## Deployment

The API test script is configured to send requests to a deployed Render endpoint:

`https://house-price-ml-api-c9ho.onrender.com/predict`

This allows the API to be tested remotely, provided the deployment is active.

## Key Learning Outcomes

- Training a Linear Regression model using Scikit-learn.
- Saving and loading machine learning models using Joblib.
- Building REST APIs using FastAPI.
- Validating API inputs using Pydantic.
- Creating prediction endpoints.
- Testing APIs using Python Requests.
- Understanding how machine learning models can be integrated into backend applications.

## Limitations

- The model is trained on only six sample records.
- Predictions are intended for demonstration and learning purposes, not real estate valuation.
- The training dataset is synthetic and does not represent actual housing market conditions.
- Model accuracy and generalization have not been established through a separate test dataset.

## Author

**Riham**

GitHub: [Riham](https://github.com/Riham203)
