# 🎬 Movie Recommendation System

This project is a **content-based movie recommender system** that suggests similar movies based on textual features such as overviews, genres, and taglines using **TF-IDF vectorization** and **cosine similarity**.

---

## 📌 Table of Contents
- Project Overview
- Features
- Tech Stack
- Local Setup
- Deployment
- Usage

---

## 📖 Project Overview

The goal of this project is to recommend movies similar to a user-selected movie by analyzing textual features.

We convert movie text data into numerical vectors using **TF-IDF (Term Frequency–Inverse Document Frequency)** and compute similarity using **cosine similarity**.

---

## ✨ Features

- 🎯 Content-Based Filtering (no user history required)
- 🧠 TF-IDF Vectorization of movie features
- 📊 Cosine Similarity for ranking movies
- 🔤 Case-insensitive movie search
- 🌐 Interactive Streamlit web application

---

## ⚙️ Tech Stack

- Python
- Pandas
- Scikit-learn
- NLTK
- Streamlit

---

## 📥 Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/ikbalhussa1n/Movie-Recommender-System.git
cd Movie-Recommender-System
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🌐 Deployment

<a href="https://movie-recommender-system-a7ak3yskk5bwumeqynbzhg.streamlit.app/" target="_blank">
  <img src="https://img.shields.io/badge/🚀%20Live%20App-Click%20Here-brightgreen?style=for-the-badge" />
</a>

---

## 🚀 Usage

```bash
streamlit run main.py
```

Steps:
1. Run Streamlit app  
2. Enter movie name  
3. Get recommendations
