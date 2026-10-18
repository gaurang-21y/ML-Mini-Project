import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import scipy.sparse

# Load movies dataset
movies = pd.read_csv("IMDB_Top_250_Movies.csv")

# Using all movies from the dataset
# movies = movies.head(100)  # Optional: limit if needed


# ✅ Ensure "genres" column exists (corrected from "genre" to "genres")
if "genre" not in movies.columns:
    raise ValueError("Error: 'genre' column not found in movies.csv!")

# ✅ Convert text data into numerical vectors
tfidf = TfidfVectorizer(stop_words="english", max_features=500)  # Limit features to reduce size

tfidf_matrix = tfidf.fit_transform(movies["genre"].fillna(""))

# ✅ Compute cosine similarity row-by-row (memory-efficient)
similarity_sparse = cosine_similarity(tfidf_matrix, tfidf_matrix, dense_output=False)

# ✅ Save similarity matrix as a sparse file
scipy.sparse.save_npz("similarity.npz", similarity_sparse)

print("✅ similarity.npz saved successfully as a sparse matrix!")
