import streamlit as st
import pandas as pd
from utils.extractor import parse_resume_text
from utils.parser import extract_resume_data
from utils.scorer import compute_similarity

# Page Config
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="🎯",
    layout="wide"
)

def main():
    st.title("🎯 AI Resume Screening & Candidate Ranking System")
    st.markdown("Automate candidate evaluation using SBERT Semantic Similarity and spaCy NLP Parsing.")

    st.sidebar.header("📋 Job Description")
    jd_text = st.sidebar.text_area(
        "Paste the Job Description (JD) here:",
        height=350,
        placeholder="e.g. Looking for a Data Scientist proficient in Python, Machine Learning, SQL, and NLP..."
    )

    st.header("📤 Candidate Resumes")
    uploaded_files = st.file_uploader(
        "Upload Resumes (.pdf or .docx)",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

    if st.button("🚀 Rank Resumes", type="primary"):
        if not jd_text.strip():
            st.error("Please provide a valid Job Description in the sidebar.")
            return
        
        if not uploaded_files:
            st.error("Please upload at least one candidate resume.")
            return

        resume_texts = []
        valid_files = []
        parsed_data = []

        # Step 1: Processing Files
        with st.spinner("Extracting and parsing documents..."):
            for file in uploaded_files:
                try:
                    text = parse_resume_text(file)
                    if text.strip():
                        resume_texts.append(text)
                        valid_files.append(file.name)
                        parsed_data.append(extract_resume_data(text))
                    else:
                        st.warning(f"Could not read text from {file.name}. It may be empty or an image scan.")
                except Exception as e:
                    st.error(f"Error processing {file.name}: {str(e)}")

        if not resume_texts:
            st.error("No valid text could be extracted from the uploaded files.")
            return

        # Step 2: Compute Semantic Similarities
        with st.spinner("Generating embeddings and computing match scores..."):
            scores = compute_similarity(jd_text, resume_texts)

        # Step 3: Format Results
        results = []
        for i in range(len(valid_files)):
            results.append({
                "Filename": valid_files[i],
                "Match Score (%)": round(scores[i] * 100, 2),
                "Detected Skills": ", ".join(parsed_data[i]["skills"]) if parsed_data[i]["skills"] else "None",
                "Organizations": ", ".join(parsed_data[i]["organizations"]) if parsed_data[i]["organizations"] else "None",
                "Raw Snippet": resume_texts[i][:250] + "..."
            })

        df_results = pd.DataFrame(results).sort_values(by="Match Score (%)", ascending=False)
        df_results.reset_index(drop=True, inplace=True)

        # Step 4: Display Output
        st.divider()
        st.subheader("📊 Ranking Leaderboard")
        
        # Display Top Candidate Banner
        top_match = df_results.iloc[0]
        st.success(f"🏆 **Top Match:** {top_match['Filename']} with a match score of **{top_match['Match Score (%)']}%**")

        st.dataframe(
            df_results[["Filename", "Match Score (%)", "Detected Skills", "Organizations"]],
            use_container_width=True
        )

        st.subheader("🔍 Deep-Dive Breakdown")
        for idx, row in df_results.iterrows():
            with st.expander(f"Rank {idx+1}: {row['Filename']} — Match: {row['Match Score (%)']}%"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Identified Skills:**", row["Detected Skills"])
                with col2:
                    st.write("**Identified Experience:**", row["Organizations"])
                st.caption("**Resume Snippet:**")
                st.text(row["Raw Snippet"])

if __name__ == "__main__":
    main()