# AI Legal Document Assistant

## Project Overview

This project is an AI-powered **Legal Document Assistant** built using Python, Streamlit, and Google Gemini.

It helps users analyze legal agreements in PDF format by extracting important contract information, identifying potentially risky or ambiguous clauses, and answering questions based strictly on the uploaded contract.

The application combines structured AI-based contract auditing with an interactive legal question-and-answer interface.

## Features

### 1. Contract Upload & Text Extraction
- Upload legal agreements in PDF format.
- Extract text from individual PDF pages using `pypdf`.
- Preserve page markers to help identify relevant contract sections.

### 2. Automated Contract Audit
Uses Google Gemini to analyze the uploaded agreement and extract:

- Document type (NDA, Service Agreement, Employment Contract, etc.).
- Effective or execution date.
- Parties involved.
- Governing law.
- Key contractual obligations.
- High-risk and ambiguous clauses.

### 3. Risk Clause Analysis

Each identified risk includes:

- **Clause Name:** Name or title of the contract clause.
- **Risk Level:** High, Medium, or Low.
- **Explanation:** Why the clause may present a risk.
- **Recommendation:** Suggested revision or mitigation step.

### 4. Interactive Legal Q&A

Users can ask questions about their uploaded agreement, including:

- Contract termination terms.
- Payment deadlines.
- Liabilities and responsibilities.
- Contractual obligations.
- Specific clauses and conditions.

The Q&A system is instructed to answer using only the uploaded contract context and explicitly acknowledge when the contract does not address an issue.

### 5. Interactive Streamlit Interface

The application includes two main sections:

- **Contract Audit & Risk Analysis:** Displays contract metadata, obligations, and identified risks.
- **Interactive Legal Q&A:** Provides a chat interface for asking contract-related questions.

## Tools & Technologies

- **Python** – Core programming language
- **Streamlit** – Web application interface
- **Google Gemini API** – AI-powered contract analysis and question answering
- **Google GenAI SDK** – Gemini API integration
- **Pydantic** – Structured output validation using data models
- **pypdf** – PDF text extraction
- **python-dotenv** – Environment variable management
- **JSON** – Structured audit report handling

## Project Structure

```text
AI_Legal_Document_Assistant/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
```

### 2. Navigate to the Project Folder

```bash
cd TopMentor_Coursework/projects/AI_Legal_Document_Assistant
```

Adjust the folder name if your actual GitHub project folder uses a different name.

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**macOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
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

Do not upload your `.env` file or expose your API key on GitHub.

## How to Run

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

### Application Workflow

1. Upload a legal agreement in PDF format.
2. Navigate to the **Contract Audit & Risk Analysis** tab.
3. Click **Run Comprehensive Legal Audit**.
4. Review extracted contract metadata, obligations, and risk assessments.
5. Navigate to the **Interactive Legal Q&A** tab.
6. Ask questions about the uploaded agreement and receive contract-grounded responses.

## Key Learning Outcomes

- Integrating Google Gemini API into Python applications.
- Using prompt engineering for structured AI analysis.
- Extracting text from PDF documents.
- Defining structured AI outputs with Pydantic models.
- Building interactive applications using Streamlit.
- Implementing context-grounded question answering.
- Managing conversational history with Streamlit session state.
- Working with environment variables and API authentication.

## Important Disclaimer

This application provides AI-generated contract analysis for educational and informational purposes. It does not replace professional legal advice or a qualified lawyer's review.

AI-generated risk assessments may be incomplete or inaccurate. Always verify important findings against the original agreement and consult a qualified legal professional before making legal decisions.

## Author

**Riham**

GitHub: [Riham](https://github.com/Riham203)
