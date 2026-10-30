# 🎯 AI Resume Analyst – Resume Screening & Candidate Ranking System

An AI-powered resume screening and candidate ranking system built using **Python, Streamlit, SBERT (Sentence-BERT), spaCy, and Machine Learning**.

The application analyzes candidate resumes against a target Job Description (JD), calculates semantic similarity scores, extracts relevant skills and information using NLP, and ranks candidates based on their relevance to the job requirements.

It also includes a standalone Machine Learning pipeline using **TF-IDF and Random Forest** to classify resumes into different job categories.

## ✨ Features

- **📄 Multi-Format Resume Parsing:** Extract text from PDF and DOCX resume files.
- **🧠 Semantic Similarity Matching:** Use SBERT (`all-MiniLM-L6-v2`) to calculate contextual similarity between resumes and job descriptions.
- **🔍 NLP Information Extraction:** Use spaCy Named Entity Recognition (NER) to identify organizations, employment-related dates, and relevant information.
- **💡 Skill Extraction:** Identify relevant skills and keyword matches between resumes and job descriptions.
- **🏆 Candidate Ranking:** Automatically rank candidates based on their resume relevance scores.
- **📊 Interactive Leaderboard:** Display candidate rankings and matching scores through a Streamlit interface.
- **🔎 Candidate Deep Dive:** View matched skills, extracted organizations, and resume text snippets.
- **🤖 Resume Classification:** Use a TF-IDF and Random Forest pipeline to categorize resumes into job-related domains.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Sentence-Transformers (SBERT) | Semantic similarity matching |
| spaCy | NLP and Named Entity Recognition |
| Scikit-learn | Machine Learning and classification |
| TF-IDF | Text feature extraction |
| Random Forest | Resume classification |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| pdfplumber | PDF text extraction |
| python-docx | DOCX text extraction |
| Joblib | Model serialization |

## 📁 Project Structure

```text
ai_resume_analyst/
│
├── data/
│   └── resume_dataset.csv
│
├── models/
│   └── resume_classifier.pkl
│
├── sample_data/
│   ├── jd.txt
│   ├── resume_data_analyst.pdf
│   ├── resume_data_science.pdf
│   └── resume_web_dev.pdf
│
├── utils/
│   ├── extractor.py
│   ├── parser.py
│   └── scorer.py
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
cd TopMentor_Coursework/projects/ai_resume_analyst
```

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

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Download the spaCy Language Model

```bash
python -m spacy download en_core_web_sm
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
2. Enter or paste the target Job Description (JD) into the sidebar.
3. Upload one or multiple candidate resumes in PDF or DOCX format.
4. Click **🚀 Rank Resumes**.
5. View the candidate leaderboard and semantic similarity scores.
6. Explore individual candidate details, matched skills, organizations, and resume text snippets.

## 🧠 How It Works

The project follows an AI-powered resume screening pipeline:

**1. Resume Extraction**

Extract text from uploaded PDF and DOCX files using `pdfplumber` and `python-docx`.

**2. NLP Processing**

Process extracted resume text using spaCy to identify entities, organizations, employment-related dates, and relevant skills.

**3. Semantic Matching**

Convert the Job Description and candidate resumes into contextual embeddings using SBERT.

**4. Similarity Scoring**

Calculate cosine similarity scores to evaluate how closely each resume matches the target Job Description.

**5. Candidate Ranking**

Rank candidates dynamically according to their semantic similarity scores.

**6. Resume Classification**

Use a separate TF-IDF and Random Forest pipeline to classify resumes into job-related categories.

## ⚙️ Training the Classification Model (Optional)

The project includes a standalone Machine Learning pipeline to train or update the resume classification model.

Run:

```bash
python train_model.py
```

The training pipeline:

1. Loads the resume dataset from `data/resume_dataset.csv` or uses a fallback dataset.
2. Converts resume text into numerical features using TF-IDF.
3. Trains a Random Forest classifier.
4. Saves the trained model as:

```text
models/resume_classifier.pkl
```

## 📚 Learning Outcomes

This project demonstrates practical experience with:

- Natural Language Processing (NLP).
- Sentence-BERT and transformer-based embeddings.
- Semantic similarity and cosine similarity.
- Named Entity Recognition using spaCy.
- PDF and DOCX document processing.
- Text preprocessing and TF-IDF vectorization.
- Random Forest classification.
- Machine Learning model training and serialization.
- Building interactive AI applications using Streamlit.

## 🔮 Future Improvements

- Add advanced skill extraction using NLP.
- Introduce candidate filtering based on experience and qualifications.
- Generate detailed candidate evaluation reports.
- Add downloadable candidate ranking reports.
- Improve resume classification accuracy.
- Support additional resume formats.
- Introduce explainable AI for candidate ranking.

## ⚠️ Important Considerations

- Semantic similarity scores indicate textual relevance, not a candidate's actual competence.
- Resume screening should support human decision-making, not replace it.
- Candidate information should be handled securely and with appropriate privacy protections.
- The classification model and similarity scores should be evaluated before being used in real recruitment decisions.

## 👩‍💻 Author

**Riham**

GitHub: [@Riham203](https://github.com/Riham203)

---

*Built as a hands-on project exploring AI, NLP, Machine Learning, and automated resume screening.*
