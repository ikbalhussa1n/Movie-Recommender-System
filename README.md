# 🎬 Movie Recommendation System

This project is a content-based movie recommender system that suggests similar movies based on textual features such as overviews, genres, and taglines using TF-IDF vectorization and cosine similarity.

---

## 📖 Project Overview

The goal of this project is to recommend movies similar to a user-selected movie by analyzing textual features.

We convert movie text data into numerical vectors using TF-IDF (Term Frequency–Inverse Document Frequency) and compute similarity using cosine similarity to find the most relevant recommendations.

---

## ✨ Features

- Content-Based Filtering (no user history required)
- TF-IDF Vectorization of movie features
- Cosine Similarity for ranking movies
- Case-insensitive movie search
- Streamlit web application

---

## ⚙️ Tech Stack

- Python
- Pandas
- Scikit-learn
- NLTK
- Streamlit

---

## 🚀 Local Setup

### 1. Clone the repository

git clone https://github.com/ikbalhussa1n/Movie-Recommender-System.git
cd Movie-Recommender-System

### 2. Create Virtual Environment

python -m venv venv

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Required Files

- main.py
- df_new.pkl
- vectorizer.pkl

### 5. Run App

streamlit run main.py

---

## 🌐 Deployment

Live App:
https://movie-recommender-system-a7ak3yskk5bwumeqynbzhg.streamlit.app/

---

## 🎮 Usage

1. Run Streamlit app
2. Enter movie name
3. Get recommendations
