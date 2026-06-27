# 🎬 Movie Recommendation App

This project is a content-based movie recommender built with Python and Streamlit. It recommends movies similar to the one you choose by analyzing movie metadata such as genres, keywords, and plot descriptions using TF-IDF vectorization and cosine similarity.

## ✨ Features

- Select a movie from the built-in dataset
- Get five similar movie recommendations instantly
- View movie plots and posters when an OMDb API key is configured
- Run the app interactively through a simple Streamlit web interface

## 📁 Project Structure

- [src/main.py](src/main.py) — Streamlit app entry point
- [src/recommend.py](src/recommend.py) — Loads the precomputed similarity data and returns recommendations
- [src/preprocess.py](src/preprocess.py) — Cleans the dataset, builds the TF-IDF model, and saves the recommendation artifacts
- [src/movies.csv](src/movies.csv) — Movie dataset used for recommendations
- [src/config.json](src/config.json) — Stores the OMDb API key

## 🧰 Requirements

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

Main dependencies include:
- streamlit
- numpy
- pandas
- scikit-learn
- nltk
- joblib
- requests

## ▶️ Setup and Run

1. Open the project folder in a terminal.
2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Generate the recommendation model files:

```bash
python src/preprocess.py
```

5. Start the app:

```bash
python -m streamlit run src/main.py
```

6. Open the local URL shown in the terminal, usually:

```text
http://127.0.0.1:8501
```

## 🔑 OMDb API Key (Optional)

The app can run without an OMDb API key, but movie plots and posters will not be shown unless you configure one.

1. Get a free API key from https://www.omdbapi.com/
2. Open [src/config.json](src/config.json)
3. Replace the placeholder value with your real key:

```json
{
  "OMDB_API_KEY": "your_real_api_key"
}
```

## 🧠 How It Works

1. Movie text data is cleaned and tokenized.
2. TF-IDF features are extracted from the combined metadata fields.
3. Cosine similarity is calculated between the movie vectors.
4. When a movie is selected, the app returns the most similar titles.

## 📝 Notes

- The preprocessing step creates the model files `df_cleaned.pkl`, `tfidf_matrix.pkl`, and `cosine_sim.pkl` inside the src folder.
- The app has already been tested locally and is ready to run on the local Streamlit server.

