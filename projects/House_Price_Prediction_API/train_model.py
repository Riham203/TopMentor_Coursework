import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Create a dummy dataset
# Features: [Square Feet, Bedrooms, Age of House]
X = np.array(
    [
        [1500, 3, 10],
        [1800, 4, 15],
        [2400, 4, 5],
        [3000, 5, 2],
        [1200, 2, 20],
        [850, 1, 30],
    ]
)

# Target: House Price ($)
y = np.array([300000, 350000, 500000, 650000, 220000, 150000])

# 2. Train a Linear Regression model
model = LinearRegression()
model.fit(X, y)

# 3. Save the trained model to a file
joblib.dump(model, "model.pkl")
print("✅ Model trained and saved as 'model.pkl'")