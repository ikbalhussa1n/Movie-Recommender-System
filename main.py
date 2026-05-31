import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from nltk import download


import nltk

# Safe NLTK setup for Streamlit
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

    
# Download NLTK data if not already present (for deployment environments)
try:
    nltk.data.find('corpora/stopwords')
except nltk.downloader.DownloadError:
    nltk.download('stopwords')
try:
    nltk.data.find('tokenizers/punkt')
except nltk.downloader.DownloadError:
    nltk.download('punkt')

# Load the saved vectorizer and dataframe
@st.cache_resource
def load_data():
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    with open('df_new.pkl', 'rb') as f:
        df_new = pickle.load(f)
    # Re-transform the tags to get 'x' for the loaded df_new
    x = vectorizer.fit_transform(df_new['tags'])
    return vectorizer, df_new, x

vectorizer, df_new, x = load_data()

def recommendations(title, x_matrix, df_data):
    try:
        # Get the index of the movie that matches the title (case-insensitive)
        idx = df_data[df_data['title'].str.lower() == title.lower()].index[0]

        # Compute the cosine similarity between the current movie and all other movies
        sim_scores = list(enumerate(cosine_similarity(x_matrix[idx], x_matrix)[0]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda i: i[1], reverse=True)

        # Get the scores of the 10 most similar movies
        # Skip the first one as it is the movie itself
        sim_scores = sim_scores[1:11]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top 10 most similar movies
        return df_data['title'].iloc[movie_indices]
    except IndexError:
        return "Movie not found. Please check the title."


# Streamlit app layout
st.title('Movie Recommender System')

movie_title = st.text_input('Enter a movie title:', 'Jumanji')

if st.button('Get Recommendations'):
    if movie_title:
        with st.spinner('Generating recommendations...'):
            recommended_movies = recommendations(movie_title, x, df_new)
            if isinstance(recommended_movies, str):
                st.error(recommended_movies)
            else:
                st.success(f'Recommended movies for "{movie_title}":')
                for i, movie in enumerate(recommended_movies):
                    st.write(f'{i+1}. {movie}')
    else:
        st.warning('Please enter a movie title.')
