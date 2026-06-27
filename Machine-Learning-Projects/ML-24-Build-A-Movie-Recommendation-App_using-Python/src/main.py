# app.py
import json
import sys
from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from recommend import df, recommend_movies
from omdb_utils import get_movie_details

config_path = BASE_DIR / "config.json"
with config_path.open("r", encoding="utf-8") as file_handle:
    config = json.load(file_handle)

# OMDB api key
OMDB_API_KEY = config.get("OMDB_API_KEY", "").strip()

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered",
)

st.title("🎬 Movie Recommender")

if not OMDB_API_KEY or OMDB_API_KEY == "your_omdb_api_key":
    st.info("Add a real OMDb API key in the config file to display detailed plots and posters. The recommender still works without it.")

# Using 'title' instead of 'song' now
movie_list = sorted(df["title"].dropna().unique())
selected_movie = st.selectbox("🎬 Select a movie:", movie_list)

if st.button("🚀 Recommend Similar Movies"):
    with st.spinner("Finding similar movies..."):
        recommendations = recommend_movies(selected_movie)
        if recommendations is None or recommendations.empty:
            st.warning("Sorry, no recommendations found.")
        else:
            st.success("Top similar movies:")
            for _, row in recommendations.iterrows():
                movie_title = row["title"]
                plot, poster = get_movie_details(movie_title, OMDB_API_KEY)

                with st.container():
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        if poster != "N/A":
                            st.image(poster, width=100)
                        else:
                            st.write("❌ No Poster Found")
                    with col2:
                        st.markdown(f"### {movie_title}")
                        st.markdown(f"*{plot}*" if plot != "N/A" else "_Plot not available_")
