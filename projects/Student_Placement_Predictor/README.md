# 🎓 Student Placement Predictor

Hi, I'm **Riham Hussain**, an AI & Data Science Enthusiast! 👋

An end-to-end Machine Learning web application built using **Python, Scikit-learn, and Streamlit** to predict student campus placement outcomes based on academic performance, internships, projects, aptitude scores, soft skills, academic stream, and work experience.

The application allows users to enter student details and receive a predicted placement status along with a probability estimate.

---

## ✨ Features

- **Synthetic Dataset Generation:** Generates 500 student records using NumPy and a weighted scoring formula.
- **Data Preprocessing:** Handles categorical variables using binary mapping and one-hot encoding.
- **Feature Scaling:** Uses `StandardScaler` to standardize input features.
- **Model Training & Comparison:** Trains and compares Logistic Regression and Random Forest classifiers.
- **Model Selection:** Selects the model with the highest test accuracy.
- **Model Evaluation:** Displays accuracy and a classification report.
- **Interactive Web Interface:** Provides a Streamlit interface for entering student details and predicting placement outcomes.
- **Prediction Probability:** Displays the model's estimated placement probability.

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Web Framework | Streamlit |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Model Serialization | Joblib |
| Dataset Format | CSV |

---

## 📂 Project Structure

```text
Student-Placement-Predictor/
│
├── app.py                  # Streamlit prediction interface
├── generate.py             # Generates synthetic student dataset
├── train_model.py          # Preprocessing, training and evaluation
├── placement_data.csv      # Generated dataset (500 records)
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
│
├── placement_model.pkl     # Generated trained model
├── scaler.pkl              # Generated fitted scaler
└── feature_columns.pkl     # Generated feature column list
```

**Note:** The three `.pkl` files are generated automatically when you run `train_model.py`. They do not need to be committed to GitHub.

---

## 📊 Dataset Overview

The project uses a synthetic dataset containing **500 student records**.

| Feature | Description |
|---|---|
| `Student_ID` | Unique student identifier |
| `CGPA` | Student's CGPA |
| `Internships` | Number of completed internships |
| `Projects` | Number of completed projects |
| `Aptitude_Score` | Aptitude test score |
| `Soft_Skills_Score` | Soft skills rating |
| `Stream` | Student's academic stream |
| `Work_Experience` | Previous work experience (Yes/No) |
| `Placed` | Target variable: 1 = Placed, 0 = Not Placed |

### Academic Streams

- Computer Science
- Information Technology
- Electronics
- Mechanical
- Civil

### Dataset Generation Logic

The synthetic placement dataset is generated using a weighted scoring formula:

- CGPA: 35%
- Internships: 25%
- Aptitude Score: 20%
- Soft Skills: 10%
- Projects: 10%

Random noise is added to simulate variation. Students with a final score of at least `0.58` are labelled as placed.

**Important:** This is a synthetic dataset with artificially generated placement labels. Predictions demonstrate a machine learning workflow and should not be treated as reliable real-world placement assessments.

---

## ⚙️ Machine Learning Workflow

1. **Dataset Generation:** Generates 500 synthetic student records.
2. **Data Cleaning:** Removes the unique `Student_ID` column.
3. **Categorical Encoding:** Converts work experience into binary values and applies one-hot encoding to academic streams.
4. **Train-Test Split:** Splits the dataset into 80% training and 20% testing data.
5. **Feature Scaling:** Applies `StandardScaler` to standardize the features.
6. **Model Training:** Trains Logistic Regression and Random Forest classifiers.
7. **Model Evaluation:** Compares model accuracy and generates a classification report.
8. **Model Selection:** Selects the classifier with the higher test accuracy.
9. **Artifact Generation:** Saves the selected model, scaler, and feature column list using Joblib.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or later
- pip package manager

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/student-placement-predictor.git

cd student-placement-predictor
```

### 2. Create a Virtual Environment

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the following steps in order.

### Step 1: Generate the Dataset

```bash
python generate.py
```

This generates `placement_data.csv` containing 500 synthetic student records.

*Skip this step if the dataset already exists and you want to use it.*

### Step 2: Train the Machine Learning Model

```bash
python train_model.py
```

This script:

- Preprocesses the dataset.
- Trains Logistic Regression and Random Forest models.
- Compares their accuracy.
- Selects the best-performing model.
- Generates the following files:

```text
placement_model.pkl
scaler.pkl
feature_columns.pkl
```

### Step 3: Launch the Streamlit Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

---

## 🖥️ Application Inputs

Users can provide the following information:

- CGPA
- Number of internships
- Number of projects
- Aptitude test score
- Soft skills rating
- Work experience
- Academic stream

Click **Predict Placement Status** to view the prediction.

The application displays either:

- **Likely to be Placed** with the estimated placement probability.
- **Higher Risk of Non-Placement** with the estimated probability of non-placement.

---

## 📚 Learning Outcomes

Through this project, I explored:

- Synthetic dataset generation using NumPy and Pandas.
- Data preprocessing and categorical encoding.
- Feature scaling using StandardScaler.
- Training and comparing classification algorithms.
- Model evaluation using accuracy and classification reports.
- Saving and loading trained models using Joblib.
- Building interactive ML applications using Streamlit.
- Integrating a trained machine learning model into a web application.
---

## 👩‍💻 Author

**Riham Hussain**

AI & Data Science Enthusiast

GitHub: [@Riham203](https://github.com/Riham203)
