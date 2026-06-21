# 📞 Customer Churn Prediction using Machine Learning

This project focuses on predicting customer churn using machine learning techniques.

Customer churn occurs when customers stop using a company's services. Predicting churn helps businesses identify at-risk customers and improve customer retention strategies.

---

## 📌 Project Overview

The objective of this project is to build a machine learning model capable of predicting customer churn based on customer demographics, account details, and service usage information.

The project includes:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Encoding
- Handling Imbalanced Data using SMOTE
- Model Training & Comparison
- Cross Validation
- Model Evaluation

---

## 📊 Dataset Information

Dataset: Telco Customer Churn Dataset

Source:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

Dataset Size:

- 7,043 Customer Records
- Multiple Customer Features

Features include:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Contract Type
- Payment Method
- Monthly Charges
- Total Charges

Target Variable:

- Churn
  - Yes = Customer Left
  - No = Customer Retained

---

## 🧠 Machine Learning Models Used

### Decision Tree Classifier

Cross Validation Accuracy:

- 78%

### Random Forest Classifier

Cross Validation Accuracy:

- 84%

### XGBoost Classifier

Cross Validation Accuracy:

- 83%

---

## 🏆 Best Model

### Random Forest Classifier

Performance on Test Dataset:

- Accuracy: 77.86%

---

## 📈 Model Evaluation

### Confusion Matrix

```text
[[878 158]
 [154 219]]
```

### Classification Report

| Metric | Churn = No | Churn = Yes |
|----------|----------|----------|
| Precision | 0.85 | 0.58 |
| Recall | 0.85 | 0.59 |
| F1-Score | 0.85 | 0.58 |

---

## 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Scikit-Learn
- XGBoost
- Imbalanced-Learn (SMOTE)
- Matplotlib
- Seaborn

---

## 📚 Concepts Covered

- Data Preprocessing
- Label Encoding
- Handling Imbalanced Data
- SMOTE
- Classification
- Decision Trees
- Random Forest
- XGBoost
- Cross Validation
- Model Evaluation

---

## 🌍 Real-World Applications

- Customer Retention
- Subscription-Based Businesses
- Telecom Analytics
- Customer Behavior Analysis
- Business Intelligence
- Marketing Strategy Optimization

---

## 📂 Project Structure

```bash

ML-22-Customer-Churn-Prediction/

├── Project_22_24_Customer_Churn_Prediction_.ipynb
├── README.md

```

---

## 👨‍💻 Author

Aniket Khandare

GitHub Repository:

https://github.com/Aniket-k-13/Machine-Learning-Project-Series

---

⭐ If you found this project useful, consider giving it a star!