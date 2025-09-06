import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model/fake_job_model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# Streamlit UI
st.title("🕵️ Fake Job Posting Detector")
st.write("Paste a job description below, and I’ll tell you if it looks **Real** or **Fake**.")

# Input text
job_text = st.text_area("Job Description:")

if st.button("Check Job Posting"):
    if job_text.strip() == "":
        st.warning("⚠️ Please enter a job posting text.")
    else:
        # Transform input and predict
        features = vectorizer.transform([job_text])
        prediction = model.predict(features)[0]
        proba = model.predict_proba(features)[0]

        if prediction == 0:
            st.success(f"✅ This job posting looks **REAL** (Confidence: {proba[0]:.2f})")
        else:
            st.error(f"❌ This job posting looks **FAKE** (Confidence: {proba[1]:.2f})")
