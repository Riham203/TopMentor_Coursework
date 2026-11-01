# 30 K-Nearest Neighbors (KNN) Programs for Data Science

## Overview

This project contains 30 practical implementations of the K-Nearest Neighbors (KNN) algorithm using Python and Scikit-Learn.

The notebook explores KNN classification and regression, distance metrics, feature scaling, hyperparameter tuning, model evaluation, dimensionality reduction, missing-data handling, and practical machine learning pipelines.

It is designed to build a strong understanding of instance-based learning through hands-on examples.

## Topics Covered

### 1. KNN Fundamentals
1. Basic KNN Classification
2. Finding Nearest Neighbors and Distances
3. Impact of K Value on Overfitting and Underfitting
4. Visualizing KNN Decision Boundaries
5. Distance Weighting (Uniform vs. Distance)

### 2. Distance Metrics & Search Algorithms
6. KNN with Manhattan Distance (L1 Metric)
7. KNN with Minkowski Distance (Custom p-value)
8. KNN with Cosine Distance Metric
9. Comparing Neighbor Search Algorithms (KD-Tree vs. Ball-Tree vs. Brute)
10. Custom Distance Metric in KNN

### 3. Feature Scaling & Hyperparameter Tuning
11. Impact of Feature Scaling on KNN
12. Finding Optimal K using Elbow Method
13. Predicting Class Probabilities with KNN
14. Cross-Validation Evaluation
15. Grid Search CV for Hyperparameter Tuning
16. Randomized Search for Fast KNN Tuning
17. Building Scikit-Learn Pipelines with KNN

### 4. KNN Regression & Anomaly Detection
18. Basic KNN Regression
19. KNN Regression with Distance Weighting
20. Multi-output KNN Regression
21. Outlier Detection using Local Outlier Factor (LOF)

### 5. Data Preprocessing & Advanced Applications
22. KNN Imputer for Missing Data Handling
23. Radius Neighbors Classification
24. Overcoming Curse of Dimensionality with PCA + KNN
25. Text Document Classification with TF-IDF + KNN
26. Image Classification on Handwritten Digits Dataset
27. Neighborhood Components Analysis (NCA) Feature Reduction

### 6. Model Evaluation & Deployment
28. Evaluating Classification Metrics (Precision, Recall, ROC-AUC)
29. Handling Imbalanced Data using Neighborhood Cleaning
30. Persisting and Reloading a KNN Model using Joblib

## Technologies Used

- Python
- NumPy
- Matplotlib
- Scikit-Learn
- Joblib
- Jupyter Notebook

## Project Structure

```text
knn_30_programs/
│
└── knn_30_programs.ipynb
```

## Installation

Clone the coursework repository:

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
cd TopMentor_Coursework/projects/knn_30_programs
```

Install the required libraries:

```bash
pip install numpy matplotlib scikit-learn joblib jupyter
```

## How to Run

1. Open the project directory.
2. Launch Jupyter Notebook:

```bash
jupyter notebook
```

3. Open `knn_30_programs.ipynb`.
4. Run the cells sequentially to explore all 30 programs.

## Learning Outcomes

- Understand the working principles of K-Nearest Neighbors.
- Explore different distance metrics and neighbor-search algorithms.
- Understand the importance of feature scaling in distance-based models.
- Perform hyperparameter tuning using Grid Search and Randomized Search.
- Build KNN classification and regression models.
- Apply dimensionality reduction and missing-value imputation.
- Explore anomaly detection and imbalanced-data handling.
- Evaluate models using classification metrics.
- Save and reload trained machine learning models using Joblib.

## Note

The notebook uses built-in Scikit-Learn datasets and generated sample datasets for demonstration. The examples are intended for educational and practical learning purposes.

## Author

**Riham203**

GitHub: [Riham203](https://github.com/Riham203)
