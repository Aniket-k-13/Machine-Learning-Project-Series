# 🎬 Movie Recommendation System using Machine Learning

This project focuses on building a Content-Based Movie Recommendation System that suggests movies similar to a user's favorite movie.

The recommendation engine analyzes movie attributes such as genres, keywords, cast, tagline, and director to identify movies with similar characteristics.

---

# 📌 Project Overview

Recommendation systems are widely used by platforms such as Netflix, Amazon Prime Video, YouTube, and Spotify to provide personalized content suggestions.

In this project, a content-based filtering approach was implemented using Natural Language Processing (NLP) techniques and Cosine Similarity.

The system recommends movies based on the similarity of movie metadata rather than user ratings.

---

# 📊 Dataset Information

Dataset: Movie Dataset

Features used for recommendation:

* Genres
* Keywords
* Tagline
* Cast
* Director

These features were combined and transformed into numerical vectors using TF-IDF Vectorization.

---

# 🧠 Concepts Used

* Recommendation Systems
* Content-Based Filtering
* Feature Engineering
* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Cosine Similarity
* Similarity Search

---

# 🛠 Tech Stack

* Python
* NumPy
* Pandas
* Scikit-Learn
* TF-IDF Vectorizer
* Cosine Similarity

---

# 🔄 Workflow

1. Load Movie Dataset
2. Select Important Features
3. Handle Missing Values
4. Combine Features into a Single Text Representation
5. Apply TF-IDF Vectorization
6. Calculate Cosine Similarity Scores
7. Accept User Movie Input
8. Find Closest Movie Match
9. Generate Similar Movie Recommendations

---

# 🤖 Recommendation Approach

### Content-Based Filtering

The recommendation engine compares movie characteristics instead of user behavior.

Movies are represented as numerical vectors using TF-IDF, and similarity between movies is calculated using Cosine Similarity.

This allows the system to recommend movies that share similar genres, themes, cast members, directors, and keywords.

---

# 📈 Output

Given a movie entered by the user:

```text
Example Input:
Avatar
```

The system generates a ranked list of movies with the highest similarity scores.

Example:

```text
Recommended Movies:

1. Guardians of the Galaxy
2. John Carter
3. Star Trek
4. The Avengers
5. Thor
...
```

---

# 🌍 Real-World Applications

* Netflix Recommendations
* Amazon Prime Recommendations
* YouTube Suggestions
* Music Recommendation Systems
* E-Commerce Product Recommendations

---

# 📌 Key Learnings

Through this project, I learned:

* Fundamentals of Recommendation Systems
* Feature Engineering for Recommendation Engines
* TF-IDF Vectorization
* Cosine Similarity
* NLP Applications in Recommender Systems
* Content-Based Filtering Techniques

---

# 📂 Project Structure

```text
ML-18-Movie-Recommendation-System/
├── Project_18_24_Movie_Recommendation_System.ipynb
├── movies.csv
├── README.md
```

---

## 👨‍💻 Author

Aniket Khandare

GitHub:
https://github.com/Aniket-k-13

LinkedIn:
https://linkedin.com/in/aniket-khandare-18b822329/

---

⭐ If you found this project useful, consider giving it a star.
