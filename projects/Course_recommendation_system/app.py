import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Course Recommendation System",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Machine Learning Course Recommendation System")
st.write("Discover similar courses based on content, subjects, and topic metadata using TF-IDF & Cosine Similarity.")

# ---------------------------------------------------------
# 1. Data Loading & Caching
# ---------------------------------------------------------
@st.cache_data
def load_data():
    # Sample dataset creation if CSV doesn't exist locally
    try:
        df = pd.read_csv("udemy_courses.csv")
    except FileNotFoundError:
        # Fallback dummy dataset for immediate testing
        data = {
            'course_id': [1, 2, 3, 4, 5, 6, 7],
            'course_title': [
                "Complete Python Web Bootstrap Developer Course",
                "Machine Learning A-Z: Hands-On Python & R In Data Science",
                "Deep Learning Specialization with TensorFlow",
                "Web Development Bootcamp with React and Node",
                "Data Science and Python for Beginners",
                "Financial Analysis and Stock Market Trading",
                "Graphic Design Masterclass - Learn Photoshop & Illustrator"
            ],
            'subject': [
                "Web Development", "Data Science", "Data Science",
                "Web Development", "Data Science", "Finance", "Design"
            ],
            'price': [50, 100, 120, 80, 40, 60, 45],
            'num_subscribers': [12000, 45000, 32000, 28000, 15000, 8000, 11000]
        }
        df = pd.DataFrame(data)
    
    # Preprocessing: Combine text columns to build rich features
    df['course_title'] = df['course_title'].fillna('')
    df['subject'] = df['subject'].fillna('')
    df['combined_features'] = df['course_title'] + " " + df['subject']
    
    return df

df = load_data()

# ---------------------------------------------------------
# 2. Vectorization & Similarity Matrix Computation
# ---------------------------------------------------------
@st.cache_resource
def compute_similarity(df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['combined_features'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

cosine_sim = compute_similarity(df)

# Helper function to get recommendations
def recommend(course_title, num_recommendations=5):
    indices = pd.Series(df.index, index=df['course_title']).drop_duplicates()
    
    if course_title not in indices:
        return None
    
    idx = indices[course_title]
    
    # Get similarity scores for all courses with that course
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort courses based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get scores of top N most similar courses (excluding itself)
    sim_scores = sim_scores[1:num_recommendations+1]
    
    course_indices = [i[0] for i in sim_scores]
    similarity_values = [round(i[1] * 100, 2) for i in sim_scores]
    
    results = df.iloc[course_indices].copy()
    results['Match Score (%)'] = similarity_values
    
    return results[['course_title', 'subject', 'Match Score (%)']]

# ---------------------------------------------------------
# 3. User Interface Controls
# ---------------------------------------------------------
col1, col2 = st.columns([2, 1])

with col1:
    selected_course = st.selectbox(
        "Select a course you completed or like:",
        df['course_title'].values
    )

with col2:
    num_rec = st.slider("Number of recommendations:", min_value=1, max_value=10, value=3)

# ---------------------------------------------------------
# 4. Display Recommendations
# ---------------------------------------------------------
if st.button("Get Recommendations 🚀", type="primary"):
    with st.spinner("Finding best matches..."):
        recommendations = recommend(selected_course, num_rec)
        
        if recommendations is not None and not recommendations.empty:
            st.subheader(f"Top Recommendations for: *{selected_course}*")
            
            for index, row in recommendations.iterrows():
                with st.container():
                    st.markdown(f"### 📘 {row['course_title']}")
                    c1, c2 = st.columns(2)
                    c1.write(f"**Subject:** {row['subject']}")
                    c2.write(f"**Similarity Match:** `{row['Match Score (%)']}%`")
                    st.divider()
        else:
            st.error("No similar courses found.")