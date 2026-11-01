# 30 Support Vector Machine (SVM) Programs for Data Science

## Overview

This project contains 30 hands-on implementations of Support Vector Machine (SVM) concepts using Python and Scikit-Learn.

The notebook explores binary and multi-class classification, linear and non-linear kernels, Support Vector Regression (SVR), anomaly detection, hyperparameter tuning, model evaluation, and practical machine learning pipelines.

It is designed to develop a practical understanding of SVM algorithms and their applications in classification, regression, and anomaly detection.

## Topics Covered

### 1. SVM Fundamentals & Classification
1. Binary Classification with Linear SVC
2. Soft Margin Classification (Tuning C Parameter)
3. Decision Boundary Visualization
4. Non-linear Classification with RBF Kernel
5. Polynomial Kernel Classification
6. Sigmoid Kernel Classification
7. Impact of Gamma Hyperparameter in RBF Kernel
8. Fast Linear Classification with LinearSVC

### 2. Multi-class Classification & Feature Analysis
9. Multi-class Classification (One-vs-Rest)
10. Multi-class Classification (One-vs-One)
11. Importance of Feature Scaling in SVM
12. Extracting and Visualizing Feature Importances with Linear SVM
13. Predicting Probability Estimates with SVM

### 3. Model Evaluation & Hyperparameter Tuning
14. Cross-Validation Evaluation
15. Hyperparameter Tuning using GridSearchCV
16. Randomized Search for SVM Tuning
17. Handling Imbalanced Datasets using class_weight
18. Custom Sample Weights in Fitting
19. Building Scikit-Learn Pipelines with SVM

### 4. Support Vector Regression & Anomaly Detection
20. Support Vector Regression (SVR) Basics
21. Linear SVR for High-Dimensional Regression
22. Impact of Epsilon Parameter in SVR
23. One-Class SVM for Novelty/Anomaly Detection

### 5. Advanced Applications & Techniques
24. Text Classification using TF-IDF and LinearSVC
25. Image Classification with SVM (Handwritten Digits)
26. Custom Kernel Matrix with Precomputed Kernel
27. Cumulative Explained Variance Reduction with PCA + SVM
28. Calibrated Classifier CV (Probability Calibration)
29. Generating Evaluation Curves (Precision-Recall)
30. Exporting and Loading SVM Model with Joblib

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-Learn
- Joblib
- Jupyter Notebook

## Project Structure

```text
svm_30_programs/
│
└── svm_30_programs.ipynb
```

## Installation

Clone the coursework repository:

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
cd TopMentor_Coursework/projects/svm_30_programs
```

Install the required libraries:

```bash
pip install numpy pandas matplotlib scikit-learn joblib jupyter
```

## How to Run

1. Open the project directory.
2. Launch Jupyter Notebook:

```bash
jupyter notebook
```

3. Open `svm_30_programs.ipynb`.
4. Run the notebook cells sequentially to explore all 30 programs.

## Learning Outcomes

- Understand the working principles of Support Vector Machines.
- Implement linear and non-linear SVM classification.
- Explore kernel functions such as RBF, polynomial, and sigmoid.
- Understand the impact of C and gamma hyperparameters.
- Apply SVM to multi-class classification problems.
- Perform hyperparameter tuning and cross-validation.
- Handle imbalanced datasets using class and sample weights.
- Build Support Vector Regression models.
- Apply One-Class SVM for anomaly detection.
- Explore SVM applications in text and image classification.
- Save and reload trained models using Joblib.

## Note

The notebook demonstrates individual SVM techniques using sample datasets and practical examples. It is intended for educational and hands-on machine learning practice.

## Author

**Riham203**

GitHub: [Riham203](https://github.com/Riham203)
