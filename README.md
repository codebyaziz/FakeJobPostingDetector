🕵️ Fake Job Posting Detector

An AI-powered tool that detects fake job postings using Machine Learning + Streamlit.
It helps job seekers stay safe from scams, fraud, and identity theft by analyzing job descriptions and predicting whether they are Real or Fake.


🚀 Features

🔍 Text Classification model trained on real-world dataset (Kaggle)

📊 Achieved 96% accuracy on validation data

🖥️ Easy-to-use Streamlit web app

⚡ Real-time prediction with confidence score

🔒 Protects users from online scams


📂 Project Structure
📁 FakeJobPostingDetector
 ┣ 📂 model                # Trained model + vectorizer
 ┣ 📜 app.py               # Streamlit app
 ┣ 📜 notebook.ipynb       # Model training notebook (Kaggle)
 ┣ 📜 requirements.txt     # Dependencies
 ┗ 📜 README.md            # Project documentation

⚙️ Installation

Clone the repository:

git clone https://github.com/codebyaziz/FakeJobPostingDetector.git
cd FakeJobPostingDetector


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

🎯 Usage

Real Job:

We are hiring a Data Analyst at XYZ Corp. 
Requirements: SQL, Python, problem-solving skills. 
Apply with your resume through our career portal.


Fake Job:

Work from home, earn $5000 weekly with no experience required! 
Just send your bank details and ID proof to start immediately.

📊 Results

Accuracy: 96.5%

Precision (Fake class): 0.95

Recall (Fake class): 0.35


🛠️ Tech Stack

Python 🐍

Scikit-learn 🤖

Pandas, NumPy 📊

Streamlit 🌐



Aziz Jalaluddin
B.Tech CSE (Data Science)
