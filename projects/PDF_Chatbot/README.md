# PDF Chatbot using Google Gemini

## Project Overview

This project is an AI-powered **PDF Chatbot** built using Python, Streamlit, and Google Gemini.

It allows users to upload PDF documents and ask questions about their contents through an interactive chat interface. The application extracts text from the uploaded PDF and uses Google's Gemini model to generate answers grounded strictly in the document.

The chatbot uses prompt engineering techniques to reduce hallucinations and ensure responses are based only on the uploaded document.

## Features

### 1. PDF Upload & Text Extraction
- Upload PDF documents through the Streamlit sidebar.
- Extract text from PDF pages using `pypdf`.
- Preserve page numbers in the extracted text for reference.
- Automatically process newly uploaded documents.

### 2. Document-Based Question Answering
- Ask questions about the uploaded PDF.
- Generate answers using Google Gemini.
- Restrict responses to information explicitly available in the document.
- Return a predefined response when requested information is missing.

### 3. Prompt Engineering

The application uses:
- **Persona Assignment:** Defines Gemini as an intelligent Document Assistant.
- **Strict Grounding Constraints:** Instructs the model to use only the uploaded document.
- **Context Injection:** Includes extracted PDF text in the system instruction.
- **Low Temperature:** Uses a temperature of 0.2 to encourage factual responses.

### 4. Interactive Chat Interface
- Maintains conversation history using Streamlit session state.
- Displays messages in a chat-based interface.
- Clears previous chat history when a new PDF is uploaded.
- Includes an option to clear chat history.

## Tools & Technologies

- **Python** – Core programming language
- **Streamlit** – Interactive web application
- **Google Gemini API** – AI-powered question answering
- **Google GenAI SDK** – Gemini API integration
- **pypdf** – PDF text extraction
- **python-dotenv** – Environment variable management

## Project Structure

```text
PDF_Chatbot/
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
cd TopMentor_Coursework/projects/PDF_Chatbot
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
pip install streamlit google-genai python-dotenv pypdf
```

### 5. Configure Gemini API Key

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your actual Google Gemini API key.

Never upload your `.env` file or expose your API key on GitHub.

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

1. Upload a PDF document using the sidebar.
2. Wait for the application to extract the document text.
3. Ask a question using the chat input.
4. Gemini analyzes the question using the extracted PDF context.
5. View the generated answer in the chat interface.
6. Upload another PDF to start a new document conversation.

## Key Learning Outcomes

- Integrating Google Gemini API into Python applications.
- Building document-based AI chatbots.
- Extracting text from PDF documents.
- Applying prompt engineering techniques.
- Implementing context-grounded question answering.
- Managing chat history using Streamlit session state.
- Handling API requests and exceptions.
- Managing API keys using environment variables.

## Limitations

- Text extraction depends on the PDF containing machine-readable text.
- Scanned PDFs may require OCR, which is not implemented.
- The entire extracted document is passed as context, so large PDFs may exceed model input limits.
- AI-generated answers may still contain inaccuracies and should be checked against the original document.

## Author

**Riham**

GitHub: [Riham](https://github.com/Riham203)
