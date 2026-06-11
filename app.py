import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page config
st.set_page_config(page_title="Student Score Predictor", layout="wide")
model = joblib.load('student_model.pkl')

# Styling
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #1a0a2e, #2d1b4e, #4a0e6b);
        }
        .stSelectbox label, .stSlider label {
            color: #00d4ff !important;
            font-size: 16px !important;
        }
        .stButton > button {
            background: linear-gradient(90deg, #00d4ff, #7b2ff7); 
            color: black; 
            border: none; 
            padding: 10px 30px; 
            border-radius: 25px;
            font-size: 18px;
            font-weight: bold; width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
    <div style='
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #00d4ff;
        letter-spacing: 2px;
        text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
        margin-top: 20px;
        font-family: "Segoe UI", sans-serif;
    '>
        🎓 Student Math Score Predictor
    </div>
    <div style='
        text-align: center;
        font-size: 16px;
        color: #a0b4c8;
        letter-spacing: 4px;
        margin-top: 8px;
        margin-bottom: 30px;
        font-family: "Segoe UI", sans-serif;
    '>
        ML-POWERED ACADEMIC PERFORMANCE PREDICTION
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Banner Image
st.image("student_model.jpg", use_container_width=True)

st.markdown("---")

# Two columns layout
col1, col2 = st.columns(2)

with col1:
    st.markdown(
    "<h3 style='color:#ffcc00;'>👤 Student Details</h3>",
    unsafe_allow_html=True
    )
    gender = st.selectbox("Gender", ["male", "female"])
    race = st.selectbox("Race/Ethnicity",
        ["group A", "group B", "group C", "group D", "group E"])
    parental_edu = st.selectbox("Parental Level of Education",
        ["some high school", "high school", "some college",
         "associate's degree", "bachelor's degree", "master's degree"])

with col2:
    st.markdown(
    "<h3 style='color:#ffcc00;'>📚 Academic Details</h3>",
    unsafe_allow_html=True
    )
    lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
    test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])
    reading_score = st.slider("Reading Score", 0, 100, 50)
    writing_score = st.slider("Writing Score", 0, 100, 50)

st.markdown("---")

# Predict Button
if st.button("🎯 Predict Math Score"):

    # Encode inputs
    gender_enc = 1 if gender == "male" else 0

    race_map = {"group A": 0, "group B": 1, "group C": 2,
                "group D": 3, "group E": 4}
    race_enc = race_map[race]

    edu_map = {
        "some high school": 5,
        "high school": 2,
        "some college": 4,
        "associate's degree": 0,
        "bachelor's degree": 1,
        "master's degree": 3
    }
    edu_enc = edu_map[parental_edu]

    lunch_enc = 1 if lunch == "standard" else 0
    test_enc = 1 if test_prep == "completed" else 0

    avg_score = (reading_score + writing_score) / 2
    score_gap = reading_score - writing_score

    # Input dataframe
    input_data = pd.DataFrame([{
        'gender': gender_enc,
        'race/ethnicity': race_enc,
        'parental level of education': edu_enc,
        'lunch': lunch_enc,
        'test preparation course': test_enc,
        'reading score': reading_score,
        'writing score': writing_score,
        'avg_score': avg_score,
        'score_gap': score_gap
    }])

    # Predict
    prediction = model.predict(input_data)[0]

    # Show result
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, #667eea, #764ba2);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
    '>
        <div style='font-size: 24px; color: #a0b4c8;'>Predicted Math Score</div>
        <div style='font-size: 60px; font-weight: 800; color: #00d4ff;'>{prediction:.1f}</div>
    </div>
    """, unsafe_allow_html=True)

    if prediction >= 80:
        st.balloons()
        st.success("🌟 Excellent Performance!")
    elif prediction >= 60:
        st.info("👍 Good Performance!")
    else:
        st.warning("📚 Needs Improvement!")

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #a0b4c8; font-size: 14px;'>
    ⚡ Developed by <b style="color:#00d4ff;">Ashwini Parmar</b>| Data Science Portfolio Project
</div>
""", unsafe_allow_html=True)
