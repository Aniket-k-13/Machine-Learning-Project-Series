# 📧 Spam Mail Prediction using Machine Learning

This project focuses on building a Machine Learning model capable of classifying emails as Spam or Ham (Legitimate Mail) using Natural Language Processing (NLP) techniques.

Spam detection is one of the most common real-world applications of Machine Learning and plays a critical role in email security systems.

---

# 📌 Project Overview

The objective of this project is to develop a text classification system that can accurately identify spam emails based on their content.

The project applies Natural Language Processing (NLP) techniques and Machine Learning algorithms to transform textual email data into numerical representations and perform classification.

---

# 🧠 Concepts Used

* Natural Language Processing (NLP)
* Text Classification
* Data Cleaning
* TF-IDF Vectorization
* Logistic Regression
* Model Evaluation
* Train-Test Split

---

# 🛠 Tech Stack

* Python
* NumPy
* Pandas
* Scikit-Learn
* NLTK
* Matplotlib
* Seaborn

---

# 🔄 Workflow

1. Load Dataset
2. Data Cleaning & Preprocessing
3. Label Encoding
4. TF-IDF Feature Extraction
5. Train-Test Split
6. Train Logistic Regression Model
7. Evaluate Performance
8. Predict New Email Messages

---

# 🤖 Model Used

## Logistic Regression

Logistic Regression was used as the classification algorithm for identifying spam emails.

Combined with TF-IDF feature extraction, the model successfully learned textual patterns commonly associated with spam and legitimate messages.

---

# 📈 Results

### Training Accuracy

**96.77%**

### Testing Accuracy

**96.68%**

### Classification Metrics

| Metric    | Ham  | Spam |
| --------- | ---- | ---- |
| Precision | 1.00 | 0.96 |
| Recall    | 0.76 | 1.00 |
| F1-Score  | 0.86 | 0.98 |

### Overall Performance

* Accuracy: **96.68%**
* Macro Average F1 Score: **0.92**
* Weighted Average F1 Score: **0.96**

The very small difference between training and testing accuracy indicates excellent model generalization and minimal overfitting.

---

# 📊 Confusion Matrix Analysis

| Actual / Predicted | Ham | Spam |
| ------------------ | --- | ---- |
| Ham                | 118 | 37   |
| Spam               | 0   | 960  |

Key Observation:

✅ The model successfully detected all spam emails in the test set.

✅ Zero spam emails were incorrectly classified as legitimate emails.

---

# 🌍 Real-World Applications

* Email Spam Filtering
* SMS Spam Detection
* Fraud Message Detection
* Phishing Prevention Systems
* Cybersecurity Solutions

---

# 📌 Key Learnings

Through this project, I learned:

* Fundamentals of Natural Language Processing
* Text Vectorization using TF-IDF
* Binary Text Classification
* Logistic Regression for NLP Tasks
* Evaluation of Classification Models
* Real-world Applications of Spam Detection Systems

---

# 📂 Project Structure

```text
ML-17-Spam-Mail-Prediction/
├── Project_17_24_Spam_Mail_Prediction.ipynb
├── mail_data.csv
├── README.md
```

---

## 👨‍💻 Author

Aniket Khandare

GitHub:
https://github.com/Aniket-k-13

LinkedIn:
https://linkedin.com/in/aniket-khandare-18b822329/

---

⭐ If you found this project useful, consider giving it a star.
