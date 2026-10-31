# 📄 AI Resume Builder & ATS Optimizer

An AI-powered resume generation application built using **Python, Streamlit, and Google Gemini**. It transforms raw work experience into structured, professional, and ATS-optimized resume content tailored to a target job role.

The application uses prompt engineering and structured AI outputs to generate professional summaries, relevant technical skills, achievement-focused experience bullet points, and ATS keywords.

## 📌 Features

### 1. Target Job Configuration
- Enter the target job title or role.
- Select experience level:
  - Entry-Level (0–2 years)
  - Mid-Level (3–5 years)
  - Senior / Lead (6+ years)
  - Executive / Manager
- Optionally paste a target job description for keyword alignment.

### 2. AI-Powered Resume Generation
Transforms unformatted candidate experience into structured resume content using Google Gemini.

Generates:
- Professional Summary (3–4 sentences).
- Core Skills (8–12 relevant technical and domain skills).
- Work Experience.
- ATS Keywords.

### 3. Prompt Engineering

The application applies several prompt engineering techniques:

- **Persona Prompting:** Assigns Gemini the role of an Executive Resume Writer and Talent Acquisition Specialist.
- **X-Y-Z Formula:** Structures achievement-focused bullet points around accomplishments, measurable results, and methods.
- **ATS Optimization:** Aligns resume content with the target role and job description.
- **Structured Output:** Uses Pydantic models to define the expected JSON response format.

### 4. ATS Keyword Optimization
- Identifies important keywords associated with the target job.
- Aligns skills with the job description.
- Displays extracted ATS keywords for easy reference.

### 5. Resume Preview & Export-Friendly Output
- Displays the generated resume profile in organized sections.
- Provides formatted Markdown resume content.
- Allows users to copy the generated resume text for further editing.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Google Gemini API | AI-powered resume generation |
| Google GenAI SDK | Gemini API integration |
| Pydantic | Structured response validation |
| python-dotenv | Environment variable management |
| JSON | Structured AI response handling |

## 📂 Project Structure

```text
AI_Resume_Builder/
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or later
- pip
- Google Gemini API key

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
```

### 2. Navigate to the Project Folder

```bash
cd TopMentor_Coursework/projects/AI_Resume_Builder
```

Adjust the folder name if your actual GitHub project folder uses a different name.

### 3. Create a Virtual Environment

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Gemini API Key

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your actual Google Gemini API key.

**Important:** Never upload your `.env` file or expose your API key on GitHub.

## ⚙️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 📝 Application Workflow

1. Enter your target job title.
2. Select your experience level.
3. Paste the target job description (optional).
4. Enter your raw work history, projects, technologies, and responsibilities.
5. Click **Build Optimized Resume**.
6. Review the generated professional summary, core skills, work experience, and ATS keywords.
7. Copy the formatted Markdown resume for further editing.

## 🎯 Key Learning Outcomes

- Integrating Google Gemini API into Python applications.
- Applying prompt engineering for professional content generation.
- Using Pydantic for structured AI responses.
- Building interactive applications using Streamlit.
- Implementing ATS keyword alignment.
- Applying the X-Y-Z achievement writing formula.
- Managing API keys through environment variables.
- Generating structured Markdown content dynamically.

## ⚠️ Limitations

- AI-generated achievements and metrics must be verified against the candidate's actual experience.
- ATS keyword matching does not guarantee passing an applicant tracking system.
- The application generates Markdown content rather than a downloadable PDF or DOCX resume.
- Resume quality depends on the accuracy and completeness of the information provided by the user.

## 👩‍💻 Author

**Riham Hussain**

AI & Data Science Enthusiast

GitHub: [Riham203](https://github.com/Riham203)
