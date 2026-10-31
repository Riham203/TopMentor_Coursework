import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Load Dataset from CSV
df = pd.read_csv('placement_data.csv')

# 2. Drop unique identifier columns that don't help prediction
if 'Student_ID' in df.columns:
    df = df.drop(columns=['Student_ID'])

# 3. Handle Categorical Features (Stream, Work_Experience)
# Convert binary categorical columns (e.g., 'Yes'/'No' -> 1/0)
if 'Work_Experience' in df.columns:
    df['Work_Experience'] = df['Work_Experience'].map({'Yes': 1, 'No': 0})

# One-Hot Encode remaining categorical columns (e.g., Stream)
df = pd.get_dummies(df, drop_first=True)

# Save feature column names so the app knows exact input layout later
feature_columns = [col for col in df.columns if col != 'Placed']

# 4. Separate Features (X) and Target (y)
X = df.drop(columns=['Placed'])
y = df['Placed']

# 5. Train-Test Split (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 6. Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 7. Model Training & Comparison
models = {
    'Logistic Regression': LogisticRegression(),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
}

best_model = None
best_accuracy = 0
best_model_name = ""

print("--- Model Evaluation ---")
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    predictions = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, predictions)
    print(f"{name} Accuracy: {acc * 100:.2f}%")

    if acc > best_accuracy:
        best_accuracy = acc
        best_model = model
        best_model_name = name

print(f"\nSelected Model: {best_model_name} ({best_accuracy * 100:.2f}% Accuracy)")

# 8. Detailed Classification Report for Best Model
y_pred = best_model.predict(X_test_scaled)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 9. Save Artifacts for Streamlit App
joblib.dump(best_model, 'placement_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(feature_columns, 'feature_columns.pkl')

print("Model, Scaler, and Feature List saved successfully!")