# 🏦 Bank Marketing Decision Assistant

## 📌 Overview

This project predicts whether a customer will subscribe to a term deposit using a machine learning model.
It provides an interactive web interface where users can input customer details and get real-time predictions along with probability and key influencing factors.

---

## 🚀 Features

* Machine Learning model using Random Forest
* Interactive Streamlit web application
* Probability-based predictions (not just Yes/No)
* Visual confidence indicator (progress bar)
* Basic explanation of key factors influencing prediction

---

## 🧠 Model Details

* Algorithm: Random Forest Classifier
* Accuracy: ~86%
* Preprocessing:

  * StandardScaler for numerical features
  * OneHotEncoder for categorical features
* Hyperparameter tuning using RandomizedSearchCV

---

## 📊 Important Insights

* Call duration is the most influential feature
* Previous campaign success strongly impacts prediction
* Customer history (previous contacts) affects outcomes

---

## ⚠️ Limitations

* Call duration is known only after the call, causing data leakage
* Predictions are probabilistic and not guaranteed
* Explanation is rule-based and not exact model interpretation

---

## 🛠️ Tech Stack

* Python
* scikit-learn
* pandas
* Streamlit

---

## 📁 Project Structure

```
bank_project/
├── streamlit_app.py
├── model.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run the application

```
streamlit run streamlit_app.py
```

---

## 🎯 Use Case

This system can help banks:

* Identify high-potential customers
* Improve marketing efficiency
* Optimize campaign targeting

---

## 📌 Note

This project demonstrates an end-to-end machine learning pipeline from data preprocessing to deployment with a user interface.

---

## 👤 Author

Harshit Sethiya 
2nd year B.Tech AIML
 
