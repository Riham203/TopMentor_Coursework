from flask import Flask, render_template, request #type: ignore
from src.predict import ConsumptionPredictor

app = Flask(__name__)
predictor = ConsumptionPredictor("model.joblib")


@app.route("/", methods=["GET", "POST"])
def index():
  prediction = None
  if request.method == "POST":
    try:
      # Extract inputs from HTML form
      input_data = {
          "hour": int(request.form["hour"]),
          "dayofweek": int(request.form["dayofweek"]),
          "quarter": int(request.form["quarter"]),
          "month": int(request.form["month"]),
          "dayofyear": int(request.form["dayofyear"]),
          "is_weekend": int(request.form["is_weekend"]),
          "lag_1h": float(request.form["lag_1h"]),
          "lag_24h": float(request.form["lag_24h"]),
          "lag_168h": float(request.form["lag_168h"]),
          "rolling_mean_24h": float(request.form["rolling_mean_24h"]),
          "rolling_std_24h": float(request.form["rolling_std_24h"]),
      }
      prediction = round(predictor.predict_single(input_data), 2)
    except Exception as e:
      prediction = f"Error: {str(e)}"

  return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
  app.run(debug=True, port=5000)