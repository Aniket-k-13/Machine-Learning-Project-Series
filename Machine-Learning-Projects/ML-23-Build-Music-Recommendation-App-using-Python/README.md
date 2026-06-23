# Music Recommendation App (ML-23)

🎵 A content-based music recommendation system built with Python and Streamlit. This project demonstrates preprocessing song metadata/lyrics, building a compact TF‑IDF + cosine-similarity recommender, and exposing recommendations through an interactive Streamlit UI.

**Table of contents**

- Overview
- Features
- Quickstart
- Project structure
- Data format
- Model & preprocessing
- Example outputs
- Troubleshooting
- Contributing & License

## Overview

This repo contains a small-scale music recommender intended for learning and demo purposes. The system uses textual and metadata features (lyrics, artist, genre, tags) to compute similarity between tracks and suggest candidates similar to a seed track or a small user profile.

## Features

- Content-based recommendations using TF‑IDF vectorization of lyrics and metadata
- Cosine-similarity ranking for nearest-neighbour suggestions
- Preprocessing script to clean and prepare data for fast lookup
- Streamlit UI for interactive exploration and recommendation delivery

## Quickstart

From the project root directory (ML-23 folder):

```bash
pip install -r requirements.txt
cd src
python preprocess.py     # creates processed artifacts used by the recommender
streamlit run main.py    # open http://localhost:8501 in your browser
```

If you prefer a single-step convenience sequence (already saved in `start_app.txt`):

```bash
pip install -r requirements.txt
cd src
python preprocess.py
streamlit run main.py
```

## Project structure

- `start_app.txt` — quick start commands
- `requirements.txt` — Python dependencies
- `src/`
	- `preprocess.py` — load raw CSV(s), clean text, extract features, save processed artifacts (`.pkl` / `.npz`)
	- `model.py` — recommender utilities (vectorizer loading, similarity search)
	- `main.py` — Streamlit application
	- `data/` — (optional) raw and processed datasets
	- `assets/` — images or small static assets used by the UI

Link to this README: [Machine-Learning-Projects/ML-23-Build-Music-Recommendation-App-using-Python/README.md](Machine-Learning-Projects/ML-23-Build-Music-Recommendation-App-using-Python/README.md)

## Data format

The preprocessing script expects one or more CSV files containing track metadata. Minimal required columns:

- `track_id` — unique identifier for the track
- `title` — track title
- `artist` — primary artist
- `lyrics` — song lyrics or textual description (if available)
- `genre` / `tags` — optional categorical metadata

If your dataset stores columns with different names, either rename them or update `preprocess.py` to map the fields.

## Model & preprocessing (details)

1. Text cleaning: lowercasing, punctuation removal, optional stopword removal and basic lemmatization.
2. Feature construction: combine `title`, `artist`, `genre` and `lyrics` into a single text field and compute TF‑IDF vectors.
3. Similarity: compute cosine similarity between a seed vector (selected track or aggregated user profile) and the corpus vectors; return top‑K nearest tracks.

Typical files produced by `preprocess.py`:

- `vectorizer.pkl` — TF‑IDF vectorizer
- `track_vectors.npz` — sparse matrix of corpus vectors
- `tracks_meta.pkl` — pandas DataFrame with track metadata indexed by `track_id`

These artifacts are loaded by `model.py` at runtime to answer queries quickly.

## Example outputs

When you search for recommendations for a track (example shown in the Streamlit UI), the app returns a ranked list like:

```
Seed: "Song Title" — Artist Name
Recommendations:
1) "Close Match 1" — Other Artist (score: 0.82)
2) "Close Match 2" — Artist X (score: 0.79)
3) "Close Match 3" — Artist Y (score: 0.76)
```

You can tune the returned fields in the UI to also show album, year, or a short lyric excerpt.

## Screenshots

Add a screenshot to `assets/` and reference it here for a visual demo. Example markdown to include a screenshot once available:

```markdown
![App screenshot](assets/screenshot.png)
```

## Troubleshooting

- If Streamlit fails to start: ensure Python is 3.8+ and dependencies from `requirements.txt` are installed.
- If preprocessing fails: check CSV column names and encoding (use `encoding='utf-8'` when reading large datasets).
- Port conflict for Streamlit: run `streamlit run main.py --server.port 8502` to change port.

## Contributing

Improvements welcome — open issues or submit PRs. Suggestions:

- Add embedding-based recommendations (e.g., sentence-transformers) for semantic matches
- Add hybrid ranking that blends collaborative signals and content similarity
- Improve UI: include audio previews, playlist export, and user profiles

## License

Add a `LICENSE` file to declare project license (MIT recommended for demos).

---

If you'd like, I can:

- add example screenshots to `assets/` and embed them in this README
- generate a sample `requirements.txt` pinned to tested versions
- convert the recommender to use sentence embeddings for better semantic matches

Tell me which of the above you'd like next.
