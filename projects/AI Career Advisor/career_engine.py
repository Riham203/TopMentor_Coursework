import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from career_database import CAREER_KNOWLEDGE_BASE


class CareerAdvisorEngine:
    def __init__(self):
        self.knowledge_base = CAREER_KNOWLEDGE_BASE
        self.df = pd.DataFrame(self.knowledge_base)
        self.vectorizer = TfidfVectorizer()
        self._prepare_engine()

    def _prepare_engine(self):
        """Prepares skill text representations and trains TF-IDF Vectorizer."""
        # Convert list of skills into single space-separated string for NLP processing
        self.df["skills_text"] = self.df["skills"].apply(lambda s: " ".join(s))
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df["skills_text"])

    def analyze_profile(self, user_skills_input: str):
        """
        Analyzes user input skills against registered career profiles.
        Returns ranked matching roles, match percentages, missing skills, and roadmaps.
        """
        
        cleaned_input = user_skills_input.lower().replace(",", " ")
        user_vector = self.vectorizer.transform([cleaned_input])

        
        similarity_scores = cosine_similarity(user_vector, self.tfidf_matrix).flatten()

        user_skills_set = set([s.strip().lower() for s in user_skills_input.split(",") if s.strip()])

        results = []
        for idx, score in enumerate(similarity_scores):
            role_data = self.df.iloc[idx]
            required_skills_set = set(role_data["skills"])

            matched_skills = list(user_skills_set.intersection(required_skills_set))
            missing_skills = list(required_skills_set - user_skills_set)

            match_percentage = round(float(score) * 100, 2)

            results.append({
                "role": role_data["role"],
                "category": role_data["category"],
                "description": role_data["description"],
                "match_percentage": match_percentage,
                "matched_skills": matched_skills,
                "missing_skills": missing_skills,
                "roadmap": role_data["roadmap"]
            })

        sorted_results = sorted(results, key=lambda x: x["match_percentage"], reverse=True)
        return sorted_results