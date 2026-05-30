# 🛒 Big Mart Sales Prediction using Machine Learning

A Machine Learning project focused on predicting product sales for Big Mart outlets using regression techniques and feature engineering.

---

## 📌 Project Overview

Big Mart sales prediction is a regression problem where the goal is to predict product sales based on various product and outlet characteristics.

This project demonstrates a complete Machine Learning workflow including:

* Data Cleaning
* Missing Value Handling
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Categorical Encoding
* Model Training
* Hyperparameter Tuning
* Cross Validation
* Model Evaluation

---

## 📊 Dataset Information

Dataset Source:
https://www.kaggle.com/datasets/brijbhushannanda1979/bigmart-sales-data

The dataset contains information about products and outlets, including:

* Item Weight
* Item Fat Content
* Item Visibility
* Item Type
* Outlet Type
* Outlet Establishment Year
* Outlet Size
* Outlet Location Type
* Item Outlet Sales (Target Variable)

---

## 🛠 Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost

---

## 🤖 Machine Learning Model

### XGBoost Regressor

The model was trained and later tuned to improve generalization performance and reduce overfitting.

---

## 🔄 Workflow

1. Load Dataset
2. Handle Missing Values
3. Perform Exploratory Data Analysis
4. Encode Categorical Features
5. Split Dataset into Training and Testing Sets
6. Train XGBoost Regressor
7. Perform Hyperparameter Tuning
8. Evaluate Model Performance
9. Validate using Cross Validation

---

## 📈 Model Performance

### Final Results

* Training R² Score: 0.633
* Testing R² Score: 0.588
* 5-Fold Cross Validation R²: 0.596

The final tuned model showed significantly improved generalization and reduced overfitting compared to the initial model.

---

## 📌 Key Learnings

Through this project, I learned:

* Feature engineering plays a major role in regression tasks
* Cross-validation provides a more reliable estimate of model performance
* Higher training accuracy does not always mean a better model
* Reducing overfitting can improve real-world performance
* Hyperparameter tuning improves model generalization

---

## 📊 Visualizations Included

* Sales Distribution Analysis
* Feature Relationship Analysis
* Missing Value Analysis
* Correlation Analysis

---

## 🚀 Future Improvements

* Compare with Random Forest Regressor
* Experiment with Ensemble Models
* Feature Selection Optimization
* Deploy using Streamlit

---

## 📂 Project Structure

```bash
ML-12-Big-Mart-Sales-Prediction/
├── Train.csv
├── Project_12_Big_Mart_Sales_Prediction.ipynb
├── README.md
```

---

## 👨‍💻 Author

Aniket Khandare

GitHub: https://github.com/Aniket-k-13

LinkedIn: https://linkedin.com/in/aniket-khandare-18b822329

---

⭐ If you found this project useful, consider giving it a star.
