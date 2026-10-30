# 🎓 AI Career Advisor & Skill Matcher

An AI-inspired career recommendation application built using **Python, Streamlit, TF-IDF Vectorization, and Cosine Similarity**.

This project analyzes a user's technical skills and compares them against predefined career profiles to recommend suitable career paths. It calculates skill similarity scores, identifies matching and missing skills, and provides personalized learning roadmaps to help users understand what they need to learn for their desired career.

## ✨ Features

- **🛠️ Skill Input:** Enter technical and soft skills separated by commas.
- **🎯 Career Recommendations:** Identify suitable career paths based on the user's skill set.
- **📊 Match Percentage:** Calculate similarity scores between user skills and career profiles.
- **✅ Matched Skills:** Identify skills that match the requirements of each career.
- **⚠️ Missing Skills:** Highlight additional skills required for different career paths.
- **🗺️ Learning Roadmaps:** Provide structured learning paths for recommended careers.
- **📋 Detailed Match Breakdown:** Display career categories, descriptions, match scores, and skill comparisons.
- **🖥️ Interactive Interface:** Explore career recommendations through a Streamlit application.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Pandas | Career knowledge base management |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning and similarity calculations |
| TF-IDF Vectorizer | Convert skills into numerical feature vectors |
| Cosine Similarity | Calculate similarity between skill profiles |

## 📁 Project Structure

```text
AI_Career_Advisor/
│
├── app.py
├── career_engine.py
├── career_database.py
├── requirements.txt
└── README.md
```

## 🎯 Supported Career Paths

The current career knowledge base includes six career profiles:

| Career Role | Category |
|---|---|
| Data Scientist | Data & AI |
| Data Engineer | Data & AI |
| Full Stack Software Engineer | Software Engineering |
| MLOps Engineer | Data & AI |
| Cloud Architect | Cloud & Infrastructure |
| Cybersecurity Analyst | Security |

Each career profile contains a description, required skills, and a recommended learning roadmap.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
cd TopMentor_Coursework
```

Navigate to the AI Career Advisor project folder inside `projects`.

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
2. Enter your technical and professional skills in the input field.
3. Separate individual skills using commas.
4. Click **🚀 Analyze Profile & Recommend Careers**.
5. View your top recommended career path.
6. Explore career match percentages and categories.
7. Review matched skills and missing skills for each career.
8. Follow the recommended learning roadmaps to develop the required skills.

## 💡 Example Input

```text
Python, SQL, Data Analysis, Pandas, Machine Learning
```

## 🧠 How It Works

The application follows a skill-based career recommendation pipeline.

**1. Skill Input**

Collect the user's technical and professional skills through the Streamlit interface.

**2. Career Knowledge Base**

Load predefined career profiles containing job roles, categories, descriptions, required skills, and learning roadmaps.

**3. Text Preprocessing**

Convert the user's input into lowercase text and prepare the career skill descriptions for comparison.

**4. TF-IDF Vectorization**

Use `TfidfVectorizer` to convert career skill descriptions and user input into numerical feature vectors.

**5. Cosine Similarity**

Calculate cosine similarity between the user's skill vector and each career profile to determine matching percentages.

**6. Skill Comparison**

Compare the user's entered skills with the required skills for each career to identify matched and missing skills.

**7. Career Ranking**

Sort career recommendations by their similarity scores in descending order.

**8. Result Presentation**

Display the top career recommendation, match percentages, skill breakdowns, and learning roadmaps through Streamlit.

## 📚 Learning Outcomes

This project demonstrates practical experience with:

- Python application development.
- Building interactive applications using Streamlit.
- Text preprocessing and feature extraction.
- TF-IDF vectorization.
- Cosine similarity calculations.
- Skill-based recommendation systems.
- Working with Pandas DataFrames.
- Designing structured knowledge bases.
- Ranking recommendations using similarity scores.
- Building data-driven career recommendation workflows.

## ⚠️ Important Considerations

- Recommendations are based on the predefined career knowledge base.
- Match percentages represent TF-IDF cosine similarity, not actual job eligibility or employment probability.
- Only six career profiles are currently included.
- Skill matching uses comma-separated skill names and direct set comparisons.
- Results depend on how closely the user's skill terminology matches the predefined skills.

## 🔮 Future Improvements

- Expand the career database with more technical and non-technical roles.
- Add experience-level and education-based recommendations.
- Integrate real-time job market information.
- Include salary and career growth insights.
- Add downloadable career recommendation reports.
- Introduce interactive learning plans.
- Improve skill matching with semantic embeddings.
- Add user profiles and recommendation history.

## 👩‍💻 Author

**Riham**

GitHub: [@Riham203](https://github.com/Riham203)

---

*Built as a hands-on project exploring Python, Machine Learning, NLP techniques, and recommendation systems.*
