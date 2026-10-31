import joblib
import pandas as pd
import streamlit as st

# 1. Load Artifacts
model = joblib.load('placement_model.pkl')
scaler = joblib.load('scaler.pkl')
feature_columns = joblib.load('feature_columns.pkl')

st.title('🎓 Student Placement Predictor')
st.write(
    'Enter student details below to predict campus placement probability.'
)

# 2. Collect Inputs
cgpa = st.slider('CGPA', 0.0, 10.0, 7.5, step=0.1)
internships = st.number_input(
    'Number of Internships', min_value=0, max_value=10, value=1
)
projects = st.number_input(
    'Number of Projects', min_value=0, max_value=10, value=2
)
aptitude = st.slider('Aptitude Test Score (%)', 0, 100, 70)
soft_skills = st.slider('Soft Skills Rating (1–10)', 1, 10, 7)

work_exp = st.selectbox('Work Experience', ['No', 'Yes'])
stream = st.selectbox(
    'Stream',
    [
        'Computer Science',
        'Information Technology',
        'Electronics',
        'Mechanical',
        'Civil',
    ],
)

if st.button('Predict Placement Status'):
    # 3. Create a dictionary with user inputs
    input_data = {
        'CGPA': cgpa,
        'Internships': internships,
        'Projects': projects,
        'Aptitude_Score': aptitude,
        'Soft_Skills_Score': soft_skills,
        'Work_Experience': 1 if work_exp == 'Yes' else 0,
        'Stream': stream,
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # One-Hot Encode categorical columns
    input_df = pd.get_dummies(input_df)

    # 4. Reindex to align with training features (fills missing dummy columns with 0)
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    # 5. Scale & Predict
    scaled_features = scaler.transform(input_df)
    prediction = model.predict(scaled_features)[0]
    probability = model.predict_proba(scaled_features)[0][1] * 100

    # Output Results
    st.markdown('---')
    if prediction == 1:
        st.success(
            f'🎉 **Likely to be Placed!** (Confidence: {probability:.1f}%)'
        )
    else:
        st.error(
            f'⚠️ **Higher Risk of Non-Placement.** (Confidence: {100 - probability:.1f}%)'
        )