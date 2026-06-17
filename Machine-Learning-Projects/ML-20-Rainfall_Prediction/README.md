# 🌧️ Rainfall Prediction using Machine Learning

This project focuses on predicting rainfall based on various weather parameters using Machine Learning techniques.

Accurate rainfall prediction plays an important role in agriculture, disaster management, water resource planning, and weather forecasting. In this project, a Random Forest Classifier was trained on weather-related features to predict whether rainfall will occur.

---

# 📌 Project Overview

Weather forecasting is one of the most impactful applications of Machine Learning. By analyzing atmospheric and environmental conditions, machine learning models can identify patterns that indicate the likelihood of rainfall.

This project uses historical weather data containing temperature, humidity, pressure, cloud cover, sunshine, wind speed, and wind direction to build a rainfall prediction system.

---

# 📊 Dataset Features

The dataset contains weather-related attributes including:

* Pressure
* Maximum Temperature
* Average Temperature
* Minimum Temperature
* Dew Point
* Humidity
* Cloud Cover
* Sunshine
* Wind Direction
* Wind Speed

Target Variable:

* Rainfall (Yes / No)

---

# 🧠 Concepts Used

* Data Preprocessing
* Classification
* Feature Analysis
* Random Forest Classifier
* Hyperparameter Tuning
* Cross Validation
* Model Evaluation

---

# 🛠 Tech Stack

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-Learn

---

# 🔄 Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Selection
5. Train-Test Split
6. Random Forest Training
7. Hyperparameter Tuning using GridSearchCV
8. Cross Validation
9. Model Evaluation

---

# 📈 Results

### Random Forest Classifier

✅ Test Accuracy: **74.47%**

✅ Mean Cross Validation Score: **82.42%**

### Classification Performance

* Precision: 0.77 (No Rain)

* Precision: 0.72 (Rain)

* Recall: 0.71 (No Rain)

* Recall: 0.78 (Rain)

### Confusion Matrix

```text
[[17  7]
 [ 5 18]]
```

The model demonstrates a good balance between precision and recall, showing its ability to identify rainfall events effectively.

---

# 🌍 Real-World Applications

* Weather Forecasting
* Agriculture Planning
* Flood Prevention
* Disaster Management
* Water Resource Management
* Smart Farming

---

# 📌 Key Learnings

Through this project, I learned:

* Weather Data Analysis
* Classification Techniques
* Hyperparameter Tuning
* Cross Validation
* Random Forest Implementation
* Model Evaluation and Validation

---

# 📂 Project Structure

```text
ML-20-Rainfall-Prediction/
├── Project_20_24_Rainfall_Prediction.ipynb
├── README.md
```

---

## 👨‍💻 Author

Aniket Khandare

GitHub Repository:
https://github.com/Aniket-k-13/Machine-Learning-Project-Series

---

⭐ If you found this project useful, consider giving it a star.
