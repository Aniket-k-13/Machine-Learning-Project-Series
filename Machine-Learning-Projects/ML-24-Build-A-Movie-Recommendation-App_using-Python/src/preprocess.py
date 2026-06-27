# preprocess.py
import logging
import re
from pathlib import Path

import joblib
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).resolve().parent
LOG_PATH = BASE_DIR / "preprocess.log"

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logging.info("🚀 Starting preprocessing...")

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

# Text cleaning
stop_words = set(stopwords.words("english"))

# Load and sample dataset
try:
    df = pd.read_csv(BASE_DIR / "movies.csv")
    logging.info("✅ Dataset loaded successfully. Total rows: %d", len(df))
except Exception as exc:
    logging.error("❌ Failed to load dataset: %s", str(exc))
    raise exc


def preprocess_text(text):
    text = re.sub(r"[^a-zA-Z\s]", "", str(text))
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)


# filter the required columns for recommendation
required_columns = ["genres", "keywords", "overview", "title"]

df = df[required_columns]

df = df.dropna().reset_index(drop=True)

df["combined"] = df["genres"] + " " + df["keywords"] + " " + df["overview"]

logging.info("🧹 Cleaning text...")
df["cleaned_text"] = df["combined"].apply(preprocess_text)
logging.info("✅ Text cleaned.")


# Vectorization
logging.info("🔠 Vectorizing using TF-IDF...")
tfidf = TfidfVectorizer(max_features=5000)
tfidf_matrix = tfidf.fit_transform(df["cleaned_text"])
logging.info("✅ TF-IDF matrix shape: %s", tfidf_matrix.shape)

# Cosine similarity
logging.info("📐 Calculating cosine similarity...")
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
logging.info("✅ Cosine similarity matrix generated.")

# Save everything
joblib.dump(df, BASE_DIR / "df_cleaned.pkl")
joblib.dump(tfidf_matrix, BASE_DIR / "tfidf_matrix.pkl")
joblib.dump(cosine_sim, BASE_DIR / "cosine_sim.pkl")
logging.info("💾 Data saved to disk.")

logging.info("✅ Preprocessing complete.")
