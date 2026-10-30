from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

@st.cache_resource
def load_embedding_model():
    """Cache SBERT model in memory to avoid reloading on every run."""
    return SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity(job_description: str, resume_texts: list) -> list:
    """Calculate semantic cosine similarity between JD and resumes."""
    model = load_embedding_model()
    
    # Encode job description and all resumes into vector space
    doc_embeddings = model.encode([job_description] + resume_texts)
    
    jd_vector = doc_embeddings[0:1]
    resume_vectors = doc_embeddings[1:]
    
    # Calculate Cosine Similarities
    similarities = cosine_similarity(jd_vector, resume_vectors)[0]
    return [float(score) for score in similarities]