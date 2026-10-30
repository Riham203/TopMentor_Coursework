# 🎓 Machine Learning Course Recommendation System

A content-based course recommendation system built using **Python, Streamlit, Pandas, and Scikit-learn**.

This application recommends similar courses based on course titles and subject metadata using **TF-IDF Vectorization and Cosine Similarity**. Users can select a course they have completed or are interested in and discover other relevant courses based on content similarity.

## ✨ Features

- **📚 Course Selection:** Select a course from the available Udemy course dataset.
- **🔍 Content-Based Recommendations:** Recommend courses based on course titles and subject categories.
- **🧠 TF-IDF Vectorization:** Convert course information into numerical feature representations.
- **📊 Cosine Similarity:** Calculate similarity scores between courses.
- **🎯 Custom Recommendations:** Choose how many similar courses to display.
- **📈 Match Scores:** Display similarity percentages for recommended courses.
- **🖥️ Interactive Interface:** Explore recommendations through a Streamlit application.
- **⚡ Performance Optimization:** Use Streamlit caching to avoid unnecessary data loading and similarity calculations.
- **🔄 Fallback Dataset:** Use a small sample dataset if the main CSV file is unavailable.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Pandas | Dataset loading and manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning and similarity calculations |
| TF-IDF Vectorizer | Text feature extraction |
| Cosine Similarity | Course similarity measurement |

## 📁 Project Structure

```text
ML_Course_Recommendation/
│
├── app.py
├── udemy_courses.csv
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
cd TopMentor_Coursework
```

Navigate to the Machine Learning Course Recommendation project folder inside `projects`.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

Launch the Streamlit application:

```bash
streamlit run app.py
```

Open your browser and navigate to:

```text
http://localhost:8501
```

## 💻 How to Use

1. Launch the application.
2. Select a course you have completed or are interested in.
3. Choose the number of recommendations using the slider.
4. Click **Get Recommendations 🚀**.
5. View the recommended courses.
6. Compare their subjects and similarity match percentages.

## 🧠 How It Works

The application follows a content-based recommendation pipeline.

**1. Data Loading**

Load the Udemy course dataset using Pandas. If the CSV file is unavailable, the application uses a small fallback dataset.

**2. Data Preprocessing**

Handle missing values in the course title and subject columns and combine them into a single text feature.

**3. TF-IDF Vectorization**

Use `TfidfVectorizer` with English stop-word removal to convert course information into numerical vectors.

**4. Similarity Calculation**

Calculate pairwise cosine similarity between all course vectors.

**5. Course Selection**

Retrieve the selected course's index from the dataset.

**6. Recommendation Ranking**

Sort other courses according to their similarity scores and select the requested number of top matches.

**7. Result Presentation**

Display recommended course titles, subjects, and similarity percentages through Streamlit.

## 📊 Recommendation Example

**Selected Course:**

Machine Learning A-Z: Hands-On Python & R In Data Science

The system compares this course with other available courses and recommends the most similar ones based on their textual content and subject metadata.

*Note: Recommendations depend on the dataset and calculated similarity scores.*

## 📚 Learning Outcomes

This project demonstrates practical experience with:

- Content-based recommendation systems.
- Text preprocessing and feature engineering.
- TF-IDF vectorization.
- Cosine similarity calculations.
- Pairwise similarity matrices.
- Ranking and filtering recommendations.
- Working with Pandas DataFrames.
- Building interactive applications using Streamlit.
- Optimizing application performance with caching.

## ⚠️ Important Considerations

- Recommendations are based on textual similarity, not course quality or student reviews.
- Match percentages represent cosine similarity, not a probability of course suitability.
- Recommendation quality depends on the available course descriptions and subject metadata.
- The current implementation uses course titles and subjects as its combined text features.

## 🔮 Future Improvements

- Include course descriptions and detailed topic information.
- Add course price and subscriber information to recommendation filters.
- Introduce user ratings and reviews.
- Build personalized recommendations based on learning goals.
- Add course filtering by price, subject, and popularity.
- Explore hybrid recommendation techniques combining content and user preferences.

## 👩‍💻 Author

**Riham**

GitHub: [@Riham203](https://github.com/Riham203)

---

*Built as a hands-on project exploring Machine Learning, Natural Language Processing, and recommendation systems.*
