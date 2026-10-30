import streamlit as st
import pandas as pd
from career_engine import CareerAdvisorEngine

st.set_page_config(
    page_title="AI Career Advisor & Skill Matcher",
    page_icon="🎓",
    layout="wide"
)

# Initialize Engine
@st.cache_resource
def load_engine():
    return CareerAdvisorEngine()

engine = load_engine()

# Header Section
st.title("🎓 AI Career Advisor & Path Recommender")
st.caption("Powered by NLP, TF-IDF Vectorization, and Semantic Cosine Similarity Engine")

st.markdown("---")

# Main Input Layout
col_input, col_info = st.columns([2, 1])

with col_input:
    st.subheader("🛠️ Enter Your Skills & Experience")
    user_skills = st.text_area(
        "List your skills separated by commas:",
        value="Python, SQL, Data Analysis, Pandas, Machine Learning",
        height=120,
        help="Example: Python, SQL, React, AWS, Docker, Machine Learning"
    )

with col_info:
    st.subheader("💡 Tips for Better Results")
    st.markdown("""
    * **Be Specific:** Enter technical skills, programming languages, and tools.
    * **Use Commas:** Separate skills with commas for accurate parsing.
    * **Include Soft & Hard Skills:** E.g., `Python, SQL, Communication, Docker`.
    """)

if st.button("🚀 Analyze Profile & Recommend Careers", type="primary"):
    if not user_skills.strip():
        st.error("Please enter at least a few skills to generate career recommendations.")
    else:
        recommendations = engine.analyze_profile(user_skills)
        
        st.markdown("---")
        st.subheader("🎯 Career Matches & Recommendations")

        top_match = recommendations[0]

        # Metric Summaries
        m1, m2, m3 = st.columns(3)
        m1.metric("Top Recommended Path", top_match["role"])
        m2.metric("Match Score", f"{top_match['match_percentage']}%")
        m3.metric("Category", top_match["category"])

        st.markdown("### 📋 Detailed Match Breakdown")

        for rec in recommendations:
            with st.expander(f"💼 **{rec['role']}** — Match Score: {rec['match_percentage']}%", expanded=(rec == top_match)):
                st.write(f"**Category:** {rec['category']}")
                st.write(f"**Description:** {rec['description']}")

                # Progress Bar Visualization
                st.progress(int(min(rec['match_percentage'], 100)))

                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("#### ✅ Matched Skills")
                    if rec["matched_skills"]:
                        st.write(", ".join([f"`{s}`" for s in rec["matched_skills"]]))
                    else:
                        st.write("No direct overlap found.")

                with col_b:
                    st.markdown("#### ⚠️ Missing Skills to Acquire")
                    if rec["missing_skills"]:
                        st.write(", ".join([f"`{s}`" for s in rec["missing_skills"]]))
                    else:
                        st.write("You possess all core skills listed for this role!")

                st.markdown("#### 🗺️ Recommended Learning Roadmap")
                st.info(rec["roadmap"])