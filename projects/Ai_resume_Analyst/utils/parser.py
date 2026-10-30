import spacy

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

COMMON_SKILLS = {
    "python", "java", "c++", "sql", "r", "javascript", "react", "node.js",
    "html", "css", "machine learning", "deep learning", "nlp", "computer vision",
    "tensorflow", "pytorch", "scikit-learn", "spacy", "pandas", "numpy",
    "docker", "kubernetes", "aws", "azure", "gcp", "git", "tableau", "power bi"
}

def extract_resume_data(text: str) -> dict:
    """Extract structured insights from raw resume text."""
    doc = nlp(text)
    
    # Extract Entities
    organizations = list(set([ent.text.strip() for ent in doc.ents if ent.label_ == "ORG"]))
    dates = list(set([ent.text.strip() for ent in doc.ents if ent.label_ == "DATE"]))
    
    # Simple Keyword Skill Extractor
    tokens = [token.text.lower() for token in doc if not token.is_stop]
    text_lower = text.lower()
    found_skills = [skill for skill in COMMON_SKILLS if skill in text_lower]
    
    return {
        "organizations": organizations[:5],
        "dates": dates[:5],
        "skills": found_skills
    }