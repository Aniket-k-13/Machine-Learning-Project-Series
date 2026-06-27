# omdb_utils.py
import requests


def get_movie_details(title, api_key):
    if not api_key or api_key == "your_omdb_api_key":
        return "Add a valid OMDb API key to view plots.", "N/A"

    url = f"http://www.omdbapi.com/?t={title}&plot=full&apikey={api_key}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        res = response.json()
    except requests.RequestException:
        return "Plot unavailable.", "N/A"

    if res.get("Response") == "True":
        return res.get("Plot", "N/A"), res.get("Poster", "N/A")

    return "N/A", "N/A"
