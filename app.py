import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Veda Business Analytics", layout="wide")

st.title("💼 Veda Technology Business & Service Analytics Dashboard")
st.markdown("Interactive machine learning app predicting client service conversion and lead engagement.")

# Sidebar Controls
st.sidebar.header("Input Customer Metrics")
visits = st.sidebar.slider("Website Visits", 1, 50, 15)
time_site = st.sidebar.slider("Time on Site (mins)", 1.0, 45.0, 12.0)
past_inq = st.sidebar.slider("Past Inquiries", 0, 10, 2)
channel = st.sidebar.selectbox("Marketing Channel", ['LinkedIn', 'Google Search', 'Instagram', 'Direct', 'Referral'])

# Feature Engineering
eng_score = (visits * 0.4) + (time_site * 0.6)
intensity = past_inq * eng_score
high_intent = 1 if channel in ['LinkedIn', 'Referral'] else 0

# Dummy Trained Model
X_dummy = np.random.rand(100, 6)
y_dummy = np.random.choice([0, 1], 100)
model = RandomForestClassifier().fit(X_dummy, y_dummy)

features = np.array([[visits, time_site, past_inq, eng_score, intensity, high_intent]])
prediction = model.predict(features)[0]
prob = model.predict_proba(features)[0][1]

# Display Predictions
col1, col2, col3 = st.columns(3)
col1.metric("Engagement Score", f"{eng_score:.2f}")
col2.metric("Conversion Probability", f"{prob*100:.1f}%")
col3.metric("Predicted Status", "High-Value Client" if prediction == 1 else "Standard Lead")

st.success("App running smoothly on Streamlit Community Cloud!")