# 🤖 AI Chatbot using Google Gemini

An interactive AI chatbot built with **Python, Streamlit, and the Google Gemini API**. The application allows users to ask questions and receive AI-generated responses in real time using streaming.

## ✨ Features

- **AI-powered conversations:** Generate responses using Google's Gemini model.
- **Real-time streaming:** Display responses as they are generated.
- **Chat history:** Maintain conversation history during the current session.
- **Interactive interface:** Simple and user-friendly chat interface built with Streamlit.
- **Environment variable support:** Securely configure the Gemini API key using a `.env` file.
- **Error handling:** Display API errors and other exceptions within the application.

## 🛠️ Tech Stack

- **Python** — Core programming language
- **Streamlit** — Web application interface
- **Google Gen AI SDK** — Integration with Google's Gemini API
- **python-dotenv** — Environment variable management

## 📁 Project Structure

```text
AI-Chatbot/
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
cd TopMentor_Coursework/projects/AI_ChatBot
```


### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**macOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 3. Install dependencies

Create a `requirements.txt` file with the following contents:

```text
streamlit
python-dotenv
google-genai
```

Install the packages:

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Obtain an API key through [Google AI Studio](https://aistudio.google.com/).

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your actual API key.

**Important:** Never commit your API key or `.env` file to GitHub.

Add the following to your `.gitignore` file:

```gitignore
.env
venv/
__pycache__/
*.py[cod]
```

### 5. Run the application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser. Enter a question in the chat input to start a conversation with Gemini.

## 💬 How It Works

1. Loads the Gemini API key from the environment.
2. Initializes the Google Gen AI client.
3. Maintains conversation messages using Streamlit session state.
4. Converts the conversation history into the format required by the Gemini API.
5. Sends the conversation to the configured Gemini model.
6. Streams the generated response to the interface.
7. Stores the assistant's response in the session history.

## 🔐 Security

- Store API credentials in environment variables.
- Keep `.env` excluded from version control.
- Never share your API key publicly.
- If an API key is accidentally exposed, revoke it and generate a replacement.

## 🚀 Future Improvements

- Add a clear-chat button.
- Add support for multiple Gemini models.
- Improve error messages for API limits and network failures.
- Add configurable chatbot settings.
- Deploy the application so it can be accessed online.

## 📌 Learning Outcomes

This project demonstrates practical experience with:

- Integrating an LLM API into a Python application.
- Building interactive web applications with Streamlit.
- Managing conversation history and session state.
- Implementing streamed AI responses.
- Managing API credentials securely.
- Handling API errors and exceptions.

## 👩‍💻 Author

**Your Name**

- GitHub: [Riham203](https://github.com/Riham203)

---

*Built as a hands-on project to explore Generative AI and LLM application development.*

