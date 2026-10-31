import os
import joblib
import mlflow
import mlflow.xgboost
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, root_mean_squared_error
from xgboost import XGBRegressor


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """Engineers lag and rolling window features for temporal tabular prediction."""
    data = df.copy()
    data["date"] = pd.to_datetime(data["date"])
    data = data.sort_values("date").reset_index(drop=True)

    # Time Features
    data["day_of_year"] = data["date"].dt.dayofyear
    data["quarter"] = data["date"].dt.quarter

    # Lag Features (Sales from previous days)
    data["sales_lag_1"] = data["daily_sales"].shift(1)
    data["sales_lag_7"] = data["daily_sales"].shift(7)
    data["sales_lag_14"] = data["daily_sales"].shift(14)

    # Rolling Statistics
    data["rolling_mean_7"] = data["daily_sales"].shift(1).rolling(window=7).mean()
    data["rolling_std_7"] = data["daily_sales"].shift(1).rolling(window=7).std()

    return data.dropna().reset_index(drop=True)


def train_and_log_model(csv_path: str = "restaurant_sales.csv"):
    """Trains XGBoost Regressor and logs metrics, parameters, and artifacts to MLflow."""
    df = pd.read_csv(csv_path)
    featured_data = create_features(df)

    feature_cols = [
        "day_of_week",
        "month",
        "is_weekend",
        "promotion",
        "average_order_value",
        "day_of_year",
        "quarter",
        "sales_lag_1",
        "sales_lag_7",
        "sales_lag_14",
        "rolling_mean_7",
        "rolling_std_7",
    ]
    target_col = "daily_sales"

    X = featured_data[feature_cols]
    y = featured_data[target_col]

    # Time-based split (80% Train, 20% Test)
    split_idx = int(len(featured_data) * 0.8)
    X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
    y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

    mlflow.set_experiment("Restaurant_Sales_Forecasting")

    with mlflow.start_run():
        params = {
            "n_estimators": 250,
            "max_depth": 5,
            "learning_rate": 0.03,
            "subsample": 0.8,
            "random_state": 42,
        }

        model = XGBRegressor(**params)
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        rmse = root_mean_squared_error(y_test, predictions)
        mae = mean_absolute_error(y_test, predictions)

        # Log parameters & metrics
        mlflow.log_params(params)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)

        # Log model artifact
        mlflow.xgboost.log_model(model, "xgboost_restaurant_model")

        # Save local inference artifacts
        os.makedirs("model_artifacts", exist_ok=True)
        joblib.dump(model, "model_artifacts/model.pkl")
        joblib.dump(feature_cols, "model_artifacts/feature_cols.pkl")

        print(
            f"✅ Training completed. Test RMSE: ${rmse:.2f} | Test MAE: ${mae:.2f}"
        )
        return model, feature_cols


if __name__ == "__main__":
    train_and_log_model()