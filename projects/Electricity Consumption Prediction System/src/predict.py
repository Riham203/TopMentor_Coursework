import joblib
import pandas as pd


class ConsumptionPredictor:

  def __init__(self, model_path: str = "model.joblib"):
    artifact = joblib.load(model_path)
    self.model = artifact["model"]
    self.feature_names = artifact["feature_names"]

  def predict_single(self, input_data: dict) -> float:
    """Accepts a dictionary of raw features and predicts MW consumption."""
    df_input = pd.DataFrame([input_data])
    df_input = df_input[self.feature_names]
    prediction = self.model.predict(df_input)[0]
    return float(prediction)