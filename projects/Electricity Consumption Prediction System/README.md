# Electricity Consumption Prediction System

## Project Overview

This project is a machine learning-based **Electricity Consumption Prediction System** that predicts electricity consumption in megawatts (MW) using historical hourly energy data.

It uses an **XGBoost Regressor** to learn consumption patterns from time-based features, previous consumption values, and rolling statistics. A Flask web application provides an interface where users can enter these features and receive a consumption prediction.

## Project Features

- Historical electricity consumption data processing.
- Time-based feature extraction.
- Lag feature engineering using previous consumption values.
- Rolling mean and standard deviation calculations.
- XGBoost regression model training.
- Model evaluation using RMSE, MAE, and R² score.
- Single-record electricity consumption prediction.
- Flask-based web interface for making predictions.

## Dataset Overview

The project uses `hourly_energy.csv`, containing **8,760 hourly records and 2 columns**.

| Column | Description |
|---|---|
| Datetime | Date and time of electricity consumption |
| Consumption | Recorded electricity consumption in MW |

The dataset contains hourly observations for 2025.

## Feature Engineering

The data pipeline extracts the following features:

### Time-Based Features
- `hour` – Hour of the day.
- `dayofweek` – Day of the week (0 = Monday, 6 = Sunday).
- `quarter` – Calendar quarter.
- `month` – Month of the year.
- `dayofyear` – Day number of the year.
- `is_weekend` – Indicates whether the day is a weekend.

### Lag Features
- `lag_1h` – Consumption one hour earlier.
- `lag_24h` – Consumption 24 hours earlier.
- `lag_168h` – Consumption 168 hours earlier (7 days).

### Rolling Statistics
- `rolling_mean_24h` – Mean consumption over the previous 24 hours.
- `rolling_std_24h` – Standard deviation of consumption over the previous 24 hours.

## Machine Learning Model

**Algorithm:** XGBoost Regressor

The model is configured with:
- 1,000 estimators
- Learning rate: 0.01
- Maximum tree depth: 6
- Subsample: 0.8
- Column sampling: 0.8
- Early stopping rounds: 50

### Model Evaluation

The model is evaluated using:

- **RMSE (Root Mean Squared Error):** Measures prediction error while penalizing larger errors.
- **MAE (Mean Absolute Error):** Measures average absolute prediction error.
- **R² Score:** Measures how well the model explains variation in the target values.

The dataset is split sequentially into 80% training data and 20% testing data to preserve time order.

## Tools & Technologies

- **Python** – Programming language
- **Pandas** – Data manipulation and preprocessing
- **NumPy** – Numerical operations
- **Scikit-learn** – Model evaluation metrics
- **XGBoost** – Machine learning model
- **Joblib** – Model serialization
- **Flask** – Backend web framework
- **HTML & CSS** – Web interface

## Project Structure

```text
Electricity_Consumption_Prediction/
│
├── data/
│   └── hourly_energy.csv
│
├── src/
│   ├── __init__.py
│   ├── data_pipeline.py
│   ├── predict.py
│   └── train.py
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── model.joblib          # Generated after model training
└── README.md
```

> The `venv/` and `__pycache__/` directories are excluded because they are local environment and cache files. The trained `model.joblib` file is generated when the training pipeline runs.

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
```

### 2. Navigate to the Project Folder

```bash
cd TopMentor_Coursework/projects/Electricity_Consumption_Prediction
```

Adjust the folder name if your actual GitHub project folder uses a different name.

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## How to Run

### Step 1: Train the Model

Run the training pipeline from the project root:

```bash
python -m src.train
```

This will:
- Load and preprocess the hourly energy dataset.
- Generate time-based, lag, and rolling features.
- Split the data into training and testing sets.
- Train the XGBoost model.
- Display RMSE, MAE, and R² evaluation metrics.
- Save the trained model as `model.joblib`.

### Step 2: Start the Flask Application

```bash
python app.py
```

### Step 3: Open the Application

Visit:

```text
http://127.0.0.1:5000
```

Enter the required time-based and historical consumption features, then click **Predict Consumption** to view the predicted electricity consumption in MW.

## Key Learning Outcomes

- Building an end-to-end machine learning project.
- Preparing time-series data for supervised learning.
- Creating lag and rolling statistical features.
- Training and evaluating an XGBoost regression model.
- Saving and loading trained models using Joblib.
- Integrating machine learning predictions into a Flask application.
- Building a simple HTML-based prediction interface.

## Important Note

The web application requires the trained `model.joblib` file. Run the training pipeline before starting Flask.

The prediction interface expects users to provide the lag and rolling-statistic values manually. Prediction quality depends on providing meaningful and correctly calculated input features.

## Author

**Riham**

GitHub: [Riham](https://github.com/Riham203)
