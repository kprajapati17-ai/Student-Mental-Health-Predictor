# 🎓 Student Mental Health Score Predictor

A machine learning web application that predicts a student's mental health score based on their social media usage, study habits, sleep, physical activity, and stress level.

## ✨ Features

- Predicts a mental health score using a machine learning model.
- Accepts student lifestyle and demographic information.
- Validates user inputs before prediction.
- Displays the predicted score through a web interface.
- Provides a visual score gauge and score interpretation.
- Uses FastAPI to connect the frontend with the ML model.

## 🛠️ Technologies Used

- **Language:** Python
- **Machine Learning:** Scikit-learn
- **Backend:** FastAPI, Uvicorn, Pydantic
- **Data Processing:** Pandas, NumPy
- **Model Saving:** Joblib
- **Frontend:** HTML, CSS, JavaScript

## 📊 Dataset

Dataset: `Student Social Media And Mental Health Impact.csv`

The dataset contains student information such as:

- Age, gender, and academic level
- Social media platform and daily usage
- Daily phone unlocks
- Study hours and physical activity
- Sleep duration and stress level
- Mental health score

## 🤖 Machine Learning Model

This project uses a **Random Forest Regressor** to predict a continuous mental health score.

The model includes preprocessing steps for numerical and categorical data before making predictions.

## 📁 Project Structure

```text
Student-Mental-Health-Predictor/
├── main.py
├── Mental_health_model.pkl
├── index.html
├── style.css
├── script.js
├── requirements.txt
├── Mental_Health.ipynb
├── test.py
├── Student Social Media And Mental Health Impact.csv
└── README.md
```

## 🚀 Try the Project

You can explore the project through the live demo below.

🔗 **Live Demo:** [Open Student Mental Health Score Predictor](https://student-mental-health-predictor-1-2iyy.onrender.com)
