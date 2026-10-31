import requests

url = "https://house-price-ml-api-c9ho.onrender.com/predict"
data = {"sqft": 1500, "bedrooms": 2, "age": 2}

response = requests.post(url, json=data)
print("API Response:", response.json())