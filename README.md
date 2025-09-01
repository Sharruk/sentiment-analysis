# ✈️ Twitter Airline Sentiment Analysis

A machine learning project that classifies airline-related tweets into **positive**, **neutral**, or **negative** sentiments.  
Built with **Python, Scikit-learn, and Streamlit**.

---

## 🚀 Features
- Preprocessed tweets using NLP techniques (tokenization, stopword removal, TF-IDF).
- Trained ML model for sentiment classification.
- Interactive **Streamlit web app** for real-time sentiment analysis.
- Dataset: Twitter US Airline Sentiment dataset.

---

## 📂 Project Structure
sentiment-analysis/
│
├── app.py # Streamlit web app
├── data/ # Dataset files
├── models/ # Saved ML models
├── notebooks/ # Jupyter notebooks (EDA, training)
├── report.pdf # Project report
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## ⚡ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Sharruk/sentiment-analysis.git
   cd sentiment-analysis


2. Create a virtual environment and install dependencies:

python3 -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
pip install -r requirements.txt

3. Run the Streamlit app:

streamlit run app.py

