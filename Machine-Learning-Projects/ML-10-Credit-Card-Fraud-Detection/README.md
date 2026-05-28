# 💳 Credit Card Fraud Detection using Machine Learning

A Machine Learning project focused on detecting fraudulent credit card transactions using Logistic Regression and multiple imbalance handling techniques.

---

## 📌 Project Overview

Credit card fraud detection is a highly imbalanced classification problem where fraudulent transactions represent only a very small portion of the dataset.

In this project, multiple balancing techniques were implemented and compared to understand how data balancing affects fraud detection performance.

The project also demonstrates an important Machine Learning insight:

> More data does not always guarantee better model performance.

---

## 📊 Dataset Information

Original Dataset: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

- **Dataset:** Credit Card Fraud Detection Dataset
- **Total Transactions:** 284,807
- **Legitimate Transactions:** 284,315
- **Fraudulent Transactions:** 492

This dataset is extremely imbalanced and represents a real-world fraud detection challenge.

---

## ⚙️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn

---

## 🤖 Machine Learning Model

- Logistic Regression

The same model was used across all balancing techniques to fairly compare their impact on performance.

---

## 🔄 Balancing Techniques Implemented

### 1. Random Undersampling
Randomly reduces the majority class to balance the dataset.

### 2. Random Oversampling
Duplicates minority class samples to balance the dataset.

### 3. SMOTE
Creates synthetic minority samples instead of simple duplication.

### 4. ADASYN
Adaptive synthetic sampling focusing more on difficult minority samples.

### 5. SMOTE + Tomek Links
Combines synthetic sampling with noise cleaning.

### 6. SMOTEENN
Combines SMOTE with Edited Nearest Neighbors cleaning.

### 7. NearMiss
Smart undersampling technique based on nearest neighbors.

---

## 📈 Evaluation Metrics

The following metrics were used to compare performance:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 📌 Key Learning Outcomes

Through experimentation, the following observations were made:

- High accuracy can be misleading for imbalanced datasets.
- Recall and F1-score are more important in fraud detection tasks.
- Larger balanced datasets did not always produce better results.
- Simple undersampling surprisingly performed very well in this experiment.
- Different balancing methods create different trade-offs between false positives and fraud detection capability.

---

## 🏆 Experimental Insights

### ✅ Undersampling
- Achieved the best F1-score in this experiment.
- Produced a smaller but cleaner balanced dataset.
- Demonstrated strong fraud detection capability.

### ✅ SMOTEENN
- Achieved very high fraud recall.
- Performed well on a more realistic large-scale dataset.
- Reduced missed fraud transactions significantly.

---

## 📊 Visualizations Included

- Fraud Recall Comparison
- Precision Comparison
- F1-Score Comparison
- Dataset Size vs Performance Analysis
- Confusion Matrix Visualization

---

## 🚀 Future Improvements

Possible future enhancements include:

- Feature Scaling
- Hyperparameter Tuning
- Ensemble Learning
- Random Forest / XGBoost
- Deep Learning Approaches
- Threshold Optimization

---

## 📂 Project Structure

```bash
├── creditcard.csv
├── Credit_Card_Fraud_Detection.ipynb
├── README.md
```

---

## 📌 Conclusion

This project demonstrates the importance of properly handling imbalanced datasets in fraud detection systems.

The experiments showed that:

- Balancing strategy significantly impacts model performance.
- Evaluation metrics matter more than raw accuracy.
- More data does not always guarantee better fraud detection results.

---

## 👨‍💻 Author

### Aniket Khandare

- GitHub: [Aniket-k-13](https://github.com/Aniket-k-13)
- LinkedIn: [Aniket Khandare](https://www.linkedin.com/in/aniket-khandare-18b822329)

---
