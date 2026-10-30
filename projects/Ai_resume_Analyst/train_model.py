import os
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline

def create_dummy_dataset():
    """Generates a sample dataset if no CSV is provided."""
    data = {
        "resume_text": [
            "Data Scientist proficient in Python, SQL, Machine Learning, TensorFlow, Pandas, and Scikit-learn.",
            "Experienced Machine Learning Engineer with expertise in PyTorch, NLP, Deep Learning, and Python.",
            "Frontend Developer skilled in React, JavaScript, HTML, CSS, Redux, and Web Performance.",
            "Full Stack Web Developer with Node.js, Express, React, MongoDB, and TypeScript experience.",
            "Data Analyst experienced in SQL, Tableau, Excel, Power BI, Python, and statistical reporting.",
            "Senior Backend Engineer specializing in Python, Django, FastAPI, PostgreSQL, and Docker.",
            "UI/UX Designer proficient in Figma, Adobe XD, Wireframing, and User Research.",
            "DevOps Engineer skilled in Docker, Kubernetes, AWS, Terraform, and CI/CD pipelines."
        ],
        "category": [
            "Data Science",
            "Data Science",
            "Web Development",
            "Web Development",
            "Data Science",
            "Web Development",
            "Design",
            "DevOps"
        ]
    }
    return pd.DataFrame(data)

def train_and_save_model(data_path=None, model_output_path="models/resume_classifier.pkl"):
    """
    Trains a Machine Learning Pipeline (TF-IDF + Random Forest) on resume text
    and exports the trained pipeline to disk.
    """
    # Step 1: Load Data
    if data_path and os.path.exists(data_path):
        print(f"📥 Loading dataset from {data_path}...")
        df = pd.read_csv(data_path)
    else:
        print("⚠️ Dataset file not found or not provided. Using fallback dummy dataset...")
        df = create_dummy_dataset()

    # Verify column existence
    if "resume_text" not in df.columns or "category" not in df.columns:
        raise ValueError("Dataset must contain 'resume_text' and 'category' columns.")

    X = df["resume_text"]
    y = df["category"]

    # Step 2: Split Data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y if len(df) > 10 else None
    )

    # Step 3: Build Machine Learning Pipeline
    # TfidfVectorizer: Extracts n-gram features from text
    # RandomForestClassifier: Learns patterns to predict category
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=1000, stop_words="english", ngram_range=(1, 2))),
        ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    # Step 4: Train Model
    print("⚙️ Training Machine Learning Model...")
    pipeline.fit(X_train, y_train)

    # Step 5: Evaluate Model
    if len(X_test) > 0:
        y_pred = pipeline.predict(X_test)
        print("\n📊 Model Evaluation Results:")
        print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
        print("\nClassification Report:\n", classification_report(y_test, y_pred, zero_division=0))

    # Step 6: Save Model Artifact
    os.makedirs(os.path.dirname(model_output_path), exist_ok=True)
    joblib.dump(pipeline, model_output_path)
    print(f"✅ Model successfully trained and saved to: {model_output_path}")

if __name__ == "__main__":
    train_and_save_model()