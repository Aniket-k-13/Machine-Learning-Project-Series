# 🧠 Parkinson's Disease Detection using Machine Learning

This project focuses on detecting Parkinson's Disease using Machine Learning techniques and biomedical voice measurements. The goal is to classify whether a person is healthy or affected by Parkinson's Disease based on various voice-related features.

---

# 📌 Project Overview

Parkinson's Disease is a progressive neurological disorder that affects movement, speech, and coordination. Early detection can assist healthcare professionals in diagnosis and treatment planning.

In this project, two Machine Learning classification models were implemented and compared:

* Support Vector Machine (SVM)
* Logistic Regression

The models were trained using biomedical voice measurements and evaluated using accuracy scores and confusion matrices.

---

# 📊 Dataset Information

Dataset Source:

https://www.kaggle.com/datasets/thecansin/parkinsons-data-set

The dataset contains multiple biomedical voice measurements collected from healthy individuals and Parkinson's patients.

### Target Variable

* 0 → Healthy Person
* 1 → Parkinson's Disease

---

# 🧠 Concepts Used

* Data Preprocessing
* Feature Scaling
* Classification
* Support Vector Machine (SVM)
* Logistic Regression
* Model Evaluation
* Confusion Matrix
* Healthcare AI

---

# 🛠 Tech Stack

* Python
* NumPy
* Pandas
* Scikit-Learn
* Matplotlib
* Seaborn

---

# 🔄 Workflow

1. Load Dataset
2. Data Exploration
3. Feature Selection
4. Feature Scaling using StandardScaler
5. Train-Test Split
6. Train SVM Model
7. Train Logistic Regression Model
8. Evaluate Performance
9. Compare Results

---

# 🤖 Models Used

## Support Vector Machine (SVM)

Support Vector Machine was used as the primary classification model due to its effectiveness on structured datasets and high-dimensional feature spaces.

### Results

* Accuracy Score: 87.18%

Confusion Matrix:

| Actual / Predicted | Healthy | Parkinson's |
| ------------------ | ------- | ----------- |
| Healthy            | 5       | 3           |
| Parkinson's        | 2       | 29          |

---

## Logistic Regression

Logistic Regression was implemented as a baseline classification model for comparison.

### Results

* Accuracy Score: 82.05%

Confusion Matrix:

| Actual / Predicted | Healthy | Parkinson's |
| ------------------ | ------- | ----------- |
| Healthy            | 5       | 3           |
| Parkinson's        | 4       | 27          |

---

# 📈 Model Comparison

| Model                  | Accuracy |
| ---------------------- | -------- |
| Support Vector Machine | 87.18%   |
| Logistic Regression    | 82.05%   |

🏆 Best Performing Model: Support Vector Machine (SVM)

---

# 📌 Key Learnings

Through this project, I learned:

* Importance of feature scaling in Machine Learning
* Healthcare applications of AI and Machine Learning
* Performance comparison between classification algorithms
* Interpretation of confusion matrices
* Evaluating models beyond simple accuracy scores

---

# 📂 Project Structure

```bash
ML-14-Parkinsons-Disease-Detection/
├── parkinsons.csv
├── Parkinsons_Disease_Detection.ipynb
├── README.md
```

---

# 🚀 Future Improvements

* Hyperparameter Tuning
* Random Forest Classification
* XGBoost Classification
* Cross Validation
* Streamlit Deployment

---

# 👨‍💻 Author

Aniket Khandare

GitHub:
https://github.com/Aniket-k-13

LinkedIn:
https://linkedin.com/in/aniket-khandare-18b822329/

---

⭐ If you found this project useful, consider giving it a star.
