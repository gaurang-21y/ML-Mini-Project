# 🎬 Movie Recommendation System

A simple yet powerful movie recommendation system built using Python. This project uses content-based filtering to recommend movies similar to the user's choice, based on the IMDB Top 250 dataset.

# 🚀 Features

- Recommend similar movies based on content similarity
- Interactive interface using Streamlit
- Precomputed similarity matrix for fast performance
- Clean and modular Python code
- Easy to deploy on platforms like Streamlit

## 🧰 Technologies Used

- **Python** – Core programming language
- **Pandas** – Data manipulation and analysis
- **NumPy** – Efficient numeric and matrix operations
- **Scikit-learn** – For computing cosine similarity
- **Streamlit** – For building the web interface
- **Jupyter Notebook** – For data exploration and prototyping
- **Git** – Version control
- **CSV** – As dataset format

##  🧠 How It Works

- The system reads metadata from the IMDB Top 250 dataset.
- It computes content-based similarity using text features like genres, cast, etc.
- A similarity matrix is generated and saved (similarity.npz) for faster recommendation.
- When a user selects a movie, the app fetches and displays similar movies instantly.

## 📊 Dataset

IMDB_Top_250_Movies.csv: Curated dataset of top movies from IMDB with relevant metadata used for recommendations.

## 📦 Deployment

You can deploy this app on Streamlit
