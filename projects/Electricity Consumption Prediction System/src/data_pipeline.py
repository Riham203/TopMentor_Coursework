import numpy as np
import pandas as pd


def load_and_preprocess_data(filepath: str) -> pd.DataFrame:
  """Loads CSV data and formats the datetime index."""
  df = pd.read_csv(filepath)
  df["Datetime"] = pd.to_datetime(df["Datetime"])
  df = df.sort_values("Datetime").set_index("Datetime")
  return df


def build_time_features(df: pd.DataFrame) -> pd.DataFrame:
  """Extracts temporal features, lag variables, and rolling statistics."""
  df = df.copy()

  # Temporal features
  df["hour"] = df.index.hour
  df["dayofweek"] = df.index.dayofweek
  df["quarter"] = df.index.quarter
  df["month"] = df.index.month
  df["dayofyear"] = df.index.dayofyear
  df["is_weekend"] = (df["dayofweek"] >= 5).astype(int)

  # Lag features
  df["lag_1h"] = df["Consumption"].shift(1)
  df["lag_24h"] = df["Consumption"].shift(24)
  df["lag_168h"] = df["Consumption"].shift(168)

  # Rolling statistics
  df["rolling_mean_24h"] = df["Consumption"].shift(1).rolling(window=24).mean()
  df["rolling_std_24h"] = df["Consumption"].shift(1).rolling(window=24).std()

  return df.dropna()