# 💻 Laptop Price Predictor & AI Advisor

Hi, I'm **Riham Hussain**, an AI & Data Science Enthusiast! 👋

An interactive Machine Learning web application and AI assistant built with **Python**, **Streamlit**, and **Scikit-Learn** that estimates laptop valuations for both new and used inventory while providing real-time hardware recommendations.

---

## 📌 Features

* **Multi-Page Web Dashboard:** Includes a secure portal sign-in, valuation engine, and interactive chat interface[cite: 9].
* **Dual Market Pipelines:** Separate synthetic data generation and Machine Learning pipelines for pristine new laptops and depreciating used inventory (accounting for hardware age)[cite: 9].
* **Real-Time Machine Learning Inferences:** Uses Scikit-Learn **Linear Regression** with live UI responsiveness via Streamlit sliders[cite: 9].
* **Integrated AI Advisory Chatbot:** Rule-based conversational assistant offering hardware advice regarding RAM, SSD storage, thermal care, and purchasing trade-offs[cite: 9].

---

## 🛠️ Tech Stack

* **Language:** Python 3.x[cite: 9]
* **Web Framework:** Streamlit[cite: 9]
* **Machine Learning:** Scikit-Learn (Linear Regression)[cite: 9]
* **Data Manipulation:** Pandas, NumPy[cite: 9]

---

## 📂 Repository Structure

├── app.py                # Main Streamlit application file (UI, Auth, ML models, & Chatbot)
├── requirements.txt      # Project dependencies
├── .gitignore            # Git ignore file
├── LICENSE               # MIT License
└── README.md             # Project documentation

---

## 📊 Feature & Model Overview

The model estimates market valuation based on four key hardware specifications[cite: 9]:

| Feature Name | Type | Description |
| :--- | :--- | :--- |
| `RAM_GB` | Categorical / Slider | System memory (`8GB`, `16GB`, `32GB`)[cite: 9] |
| `Storage_GB` | Categorical / Slider | Solid State Drive storage (`256GB`, `512GB`, `1024GB`)[cite: 9] |
| `Screen_Size` | Categorical / Select | Display size in inches (`13.3"`, `14.0"`, `15.6"`, `17.3"`)[cite: 9] |
| `Age_Years` | Numerical / Slider | Age of the device in years (`1` to `5` years, used laptops only)[cite: 9] |

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed on your machine.

### 1. Clone the Repository

```bash
git clone [https://github.com/Riham203/laptop-price-predictor.git](https://github.com/Riham203/laptop-price-predictor.git)
cd laptop-price-predictor
```

### 2. Set Up a Virtual Environment
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## ⚙️ Running the Project
Start the Streamlit application:
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501` to view the portal. You can sign in using any username and password credentials[cite: 9].
## 📜 License
Distributed under the MIT License. See LICENSE for details.
