# Restaurant Sales Analysis & MLOps Platform

## Project Overview

This project is an end-to-end **Restaurant Sales Forecasting and MLOps Platform** built using Python, Streamlit, XGBoost, and MLflow.

It generates synthetic restaurant sales data, trains a machine learning model to forecast daily revenue, tracks model performance using MLflow, and provides an interactive dashboard for historical sales analysis, real-time inference, and model retraining.

The application demonstrates an end-to-end machine learning workflow, from data generation and feature engineering to model training, evaluation, experiment tracking, and deployment for inference.

## Features

### 1. Synthetic Restaurant Data Generation

The `data_generator.py` module generates 730 days of synthetic restaurant sales data.

The generated dataset includes:
- Date
- Day of week
- Month
- Weekend indicator
- Promotions
- Seating capacity
- Average order value
- Daily sales

The data generator incorporates seasonal patterns, weekend sales boosts, promotional effects, and random noise.

### 2. Machine Learning Pipeline

The `ml_pipeline.py` module handles feature engineering and model training.

**Algorithm:** XGBoost Regressor

#### Feature Engineering

The pipeline creates the following features:

- `day_of_week`
- `month`
- `is_weekend`
- `promotion`
- `average_order_value`
- `day_of_year`
- `quarter`
- `sales_lag_1`
- `sales_lag_7`
- `sales_lag_14`
- `rolling_mean_7`
- `rolling_std_7`

#### Model Configuration

- Number of estimators: 250
- Maximum depth: 5
- Learning rate: 0.03
- Subsample: 0.8
- Random state: 42

The dataset is divided sequentially into 80% training data and 20% testing data to preserve chronological order.

### 3. Model Evaluation

The model is evaluated using:

- **RMSE (Root Mean Squared Error):** Measures the magnitude of prediction errors.
- **MAE (Mean Absolute Error):** Measures average absolute prediction error.

### 4. MLflow Experiment Tracking

The project integrates MLflow to track machine learning experiments.

It logs:
- Model hyperparameters.
- RMSE evaluation metric.
- MAE evaluation metric.
- Trained XGBoost model artifact.

The experiment is registered under:

`Restaurant_Sales_Forecasting`

### 5. Interactive Streamlit Dashboard

The application provides three operating modes.

**Sales Dashboard**
- Displays total recorded days.
- Calculates average daily revenue.
- Displays peak daily revenue.
- Visualizes historical daily revenue trends.

**Real-time Inference**
- Predicts tomorrow's estimated restaurant sales.
- Accepts weekend and promotion selections.
- Allows users to specify expected average order value.
- Uses historical sales and rolling statistics as model inputs.
- Displays the predicted revenue.

**Model Retraining**
- Generates refreshed synthetic restaurant sales data.
- Rebuilds the feature dataset.
- Trains a new XGBoost model.
- Logs the new experiment in MLflow.
- Saves updated model artifacts.

## Tools & Technologies

- **Python** – Core programming language
- **Pandas** – Data manipulation and preprocessing
- **NumPy** – Numerical operations and synthetic data generation
- **Scikit-learn** – Model evaluation metrics
- **XGBoost** – Sales forecasting model
- **MLflow** – Experiment tracking and model logging
- **Joblib** – Model serialization
- **Streamlit** – Interactive dashboard
- **Matplotlib** – Data visualization library

## Project Structure

```text
restaurant_mlops/
│
├── app.py
├── data_generator.py
├── ml_pipeline.py
└── requirements.txt
└── README.md
```

> `restaurant_sales.csv`, `model_artifacts/`, and `mlruns/` are generated when the application or training pipeline runs. They do not need to be manually created beforehand.

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
```

### 2. Navigate to the Project Folder

```bash
cd TopMentor_Coursework/projects/Restaurant_Sales_MLOps
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

### Step 1: Launch the Streamlit Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

### Step 2: Explore the Dashboard

Select one of the three modes from the sidebar:

1. **Sales Dashboard:** Explore historical restaurant sales performance.
2. **Real-time Inference:** Generate a sales forecast using the available inputs.
3. **Model Retraining:** Generate refreshed data and retrain the XGBoost model.

### Step 3: View MLflow Experiments

In a separate terminal, run:

```bash
mlflow ui
```

Open:

```text
http://127.0.0.1:5000
```

Explore the `Restaurant_Sales_Forecasting` experiment to review logged parameters, evaluation metrics, and model artifacts.

## Key Learning Outcomes

- Building an end-to-end machine learning pipeline.
- Generating synthetic datasets using Python.
- Performing time-series feature engineering.
- Training XGBoost regression models.
- Evaluating forecasting models using RMSE and MAE.
- Tracking experiments with MLflow.
- Saving and loading trained model artifacts.
- Building interactive dashboards using Streamlit.
- Implementing model retraining workflows.
- Integrating machine learning inference into an application.

## Limitations

- The project uses synthetic restaurant sales data rather than real business transactions.
- Forecasting performance on real restaurant data has not been established.
- The inference interface uses a hardcoded day-of-year value and manually selected inputs.
- The retraining workflow demonstrates automated retraining locally; it does not implement a production deployment pipeline or automated monitoring.

## Author

**Riham**

GitHub: [Riham](https://github.com/Riham203)
