# 🕵️ Fake Job Posting Detector

An AI-powered tool to detect fraudulent job postings and protect users from online scams.

## 📌 Problem
Fake job postings are rising online. Scammers use them to steal personal information or money from job seekers. Since these postings look very similar to real ones, it’s hard to identify them manually.

## 💡 Solution
We built a **Machine Learning model** that classifies job postings as **Real** or **Fake**.  
The model is integrated into a **Streamlit web app** where users can paste job descriptions and instantly check their authenticity.

## 🗂️ Dataset
- Source: [Kaggle – Real or Fake Job Posting Prediction](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)  
- ~18,000 job postings (real + fake)  
- Cleaned and preprocessed text data for training

## ⚙️ Tech Stack
- Python  
- Pandas, Scikit-learn  
- Streamlit  
- Kaggle  

## 📊 Model
- Algorithm: Logistic Regression  
- Accuracy: **96%**  
- Metrics:
  - Precision (Real): 0.97  
  - Precision (Fake): 0.95  
  - Weighted F1: 0.96  

## 🖥️ How to Run the Project

### 🔹 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/FakeJobPostingDetector.git
cd FakeJobPostingDetector
