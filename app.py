import streamlit as st
import joblib

# Load model + vectorizer
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

st.title("✈️ Twitter Airline Sentiment Analysis")

tweet = st.text_area("Enter a tweet to analyze:")

if st.button("Predict Sentiment"):
    if tweet.strip() != "":
        features = vectorizer.transform([tweet])
        prediction = model.predict(features)[0]
        st.success(f"Sentiment: **{prediction.upper()}**")
    else:
        st.warning("Please enter a tweet before predicting.")
