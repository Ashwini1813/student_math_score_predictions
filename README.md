![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)




![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)




![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)



# 🎓 Student Math Score Predictor

## 🌐 Live Demo
👉 [Launch App](https://student-math-score-predictions-1.streamlit.app/)

---

## 📌 Overview
Student Math Score Predictor is a Machine Learning-powered web application that predicts a student's math score based on their academic and demographic details.

The app uses historical exam data and compares multiple regression models to predict math scores based on reading score, writing score, gender, parental education, lunch type, and test preparation status.

---

## 🎯 Features
- ✅ Predicts math score based on 7 input features
- ✅ Interactive Streamlit interface with dropdowns and sliders
- ✅ Real-time prediction with instant results
- ✅ Performance feedback (Excellent/Good/Needs Improvement)
- ✅ Clean, modern UI with custom styling

---

## 🛠️ Tech Stack
| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Machine Learning | Linear Regression, Decision Tree, Random Forest |
| Data Processing | Pandas, NumPy |
| ML Framework | Scikit-learn |
| Visualization | Matplotlib, Seaborn |
| Model Serialization | Joblib |
| Deployment | Streamlit Cloud |

---

## 📊 Model Performance
| Model | R² Score | MAE | RMSE |
|-------|----------|-----|------|
| **Linear Regression** | **88.38%** | 4.13 | 5.32 |
| Random Forest | 83.92% | 4.81 | 6.26 |
| Decision Tree | 72.07% | 6.58 | 8.24 |

**Selected Model:** Linear Regression — best performance on this dataset, indicating a strong linear relationship between reading/writing scores and math score.

---

## 🔧 Feature Engineering
- **avg_score** — Average of reading and writing scores
- **score_gap** — Difference between reading and writing scores
- Label Encoding applied to categorical variables (gender, race/ethnicity, parental education, lunch, test preparation)

**Total features used: 9**

---

## 📂 Dataset
- **Source:** Students Performance in Exams (Kaggle)
- **Records:** 1000 student records
- **Target Variable:** Math Score

---

## 📈 Workflow
1. Data Loading & Exploration
2. Exploratory Data Analysis (EDA)
3. Correlation Analysis
4. Label Encoding & Feature Engineering
5. Model Training & Comparison
6. Feature Importance Analysis
7. Model Deployment with Streamlit

---

## 🚀 Run Locally

```bash
git clone https://github.com/Ashwini1813/Student_performance_prediction.git
cd Student_performance_prediction
pip install -r requirements.txt
streamlit run app.py

👩‍💻 Developer
Ashwini Parmar
