# 🕵️ Fake Job Posting Detector

## 📌 Problem
Fake job postings are a major issue online, often used for scams, identity theft, and fraud. Many people fall for them because they look very similar to real postings.

## 💡 Solution
We built a **Machine Learning model** that detects whether a job posting is **Real** or **Fake** using text classification.  
Our project also includes a **Streamlit web app** where users can paste job descriptions and instantly check their authenticity.

## 🗂️ Dataset
- Source: [Kaggle – Real or Fake Job Posting Prediction](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)  
- Size: ~18,000 job postings (real + fake)  
- Preprocessing: Removed missing values, selected relevant text columns, cleaned text.

## ⚙️ Tech Stack
- Python  
- Pandas, Scikit-learn  
- Streamlit (for UI)  
- Kaggle (for model training)  

## 📊 Model
- Algorithm: Logistic Regression  
- Accuracy: **96%**  
- Metrics:
  - Precision (Real): 0.97  
  - Precision (Fake): 0.95  
  - Weighted F1: 0.96  

## 🖥️ Streamlit App
- Input: Paste a job description.  
- Output: Prediction → **REAL ✅** or **FAKE ❌**, along with confidence score.  

Run locally:
```bash
pip install -r requirements.txt
streamlit run app.py
