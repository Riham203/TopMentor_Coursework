import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)
num_samples = 500

# Generating Features
student_ids = [f'STU_{i:04d}' for i in range(1, num_samples + 1)]
cgpa = np.round(np.random.uniform(5.0, 9.8, num_samples), 2)
internships = np.random.choice([0, 1, 2, 3], size=num_samples, p=[0.4, 0.35, 0.18, 0.07])
projects = np.random.choice([0, 1, 2, 3, 4], size=num_samples, p=[0.1, 0.3, 0.35, 0.18, 0.07])
aptitude_score = np.random.randint(40, 100, num_samples)
soft_skills_score = np.random.randint(3, 10, num_samples)
stream = np.random.choice(
    ['Computer Science', 'Information Technology', 'Electronics', 'Mechanical', 'Civil'],
    size=num_samples,
    p=[0.35, 0.25, 0.2, 0.1, 0.1]
)
work_exp = np.random.choice(['Yes', 'No'], size=num_samples, p=[0.25, 0.75])

# Calculate Placement Probability using weighted score formula
scores = (
    (cgpa / 10.0) * 0.35 +
    (internships / 3.0) * 0.25 +
    (aptitude_score / 100.0) * 0.20 +
    (soft_skills_score / 10.0) * 0.10 +
    (projects / 4.0) * 0.10
)

# Add random noise to simulate real-world variance
scores += np.random.normal(0, 0.05, num_samples)

# Assign binary target 'Placed' (1 = Placed, 0 = Not Placed)
placed = (scores >= 0.58).astype(int)

# Create DataFrame
placement_df = pd.DataFrame({
    'Student_ID': student_ids,
    'CGPA': cgpa,
    'Internships': internships,
    'Projects': projects,
    'Aptitude_Score': aptitude_score,
    'Soft_Skills_Score': soft_skills_score,
    'Stream': stream,
    'Work_Experience': work_exp,
    'Placed': placed
})

# Save to CSV
placement_df.to_csv('placement_data.csv', index=False)
print('`placement_data.csv` successfully generated with 500 records!')