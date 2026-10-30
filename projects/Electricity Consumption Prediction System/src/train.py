import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import xgboost as xgb #type: ignore

from src.data_pipeline import build_time_features, load_and_preprocess_data

FEATURE_COLUMNS = [
    "hour",
    "dayofweek",
    "quarter",
    "month",
    "dayofyear",
    "is_weekend",
    "lag_1h",
    "lag_24h",
    "lag_168h",
    "rolling_mean_24h",
    "rolling_std_24h",
]
TARGET_COLUMN = "Consumption"


def train_pipeline(data_path: str, model_save_path: str = "model.joblib"):
  df = load_and_preprocess_data(data_path)
  df_features = build_time_features(df)
  # Sequential train/test split (80/20) for time-series data
  train_size = int(len(df_features) * 0.8)
  train_df = df_features.iloc[:train_size]
  test_df = df_features.iloc[train_size:]

  X_train, y_train = train_df[FEATURE_COLUMNS], train_df[TARGET_COLUMN]
  X_test, y_test = test_df[FEATURE_COLUMNS], test_df[TARGET_COLUMN]

  model = xgb.XGBRegressor(
      n_estimators=1000,
      learning_rate=0.01,
      max_depth=6,
      subsample=0.8,
      colsample_bytree=0.8,
      early_stopping_rounds=50,
      random_state=42,
  )

  model.fit(
      X_train,
      y_train,
      eval_set=[(X_train, y_train), (X_test, y_test)],
      verbose=100,
  )

  # Evaluation metrics
  predictions = model.predict(X_test)
  rmse = np.sqrt(mean_squared_error(y_test, predictions))
  mae = mean_absolute_error(y_test, predictions)
  r2 = r2_score(y_test, predictions)

  print("\n--- Model Performance ---")
  print(f"RMSE: {rmse:.2f} MW")
  print(f"MAE:  {mae:.2f} MW")
  print(f"R² Score: {r2:.4f}\n")

  # Save trained model pipeline artifact
  artifact = {"model": model, "feature_names": FEATURE_COLUMNS}
  joblib.dump(artifact, model_save_path)
  print(f"Model successfully saved to {model_save_path}")


if __name__ == "__main__":
  train_pipeline("data/hourly_energy.csv")