# 🚀 AI Social Media Content Generator

## Project Overview

An AI-powered **Social Media Content Generator** built using Python, Streamlit, and Google Gemini.

This application generates platform-specific social media content based on a user's topic, target audience, brand tone, and marketing objective.

It uses prompt engineering and structured AI responses to create engaging hooks, main content, calls to action (CTAs), and relevant hashtags for different social media platforms.

## 📌 Features

### 1. Multi-Platform Content Generation

Generate content optimized for:

- **LinkedIn:** Professional posts with key insights and relevant hashtags.
- **Twitter / X:** Short posts under 280 characters, followed by a three-tweet thread.
- **Instagram:** Captivating captions with emojis and carousel slide ideas.
- **YouTube Shorts / Reels:** Structured 30-second video scripts with hooks, visual and audio directions, and CTAs.

### 2. Customizable Brand Tone

Choose from five writing styles:

- Professional & Authoritative
- Casual & Conversational
- Witty & Engaging
- Inspirational
- Educational

### 3. Marketing Objectives

Customize generated content based on the primary campaign goal:

- Drive Website Traffic
- Encourage Comments & Engagement
- Brand Awareness
- Lead Generation / Sales

### 4. Audience Targeting

Specify the intended audience, such as:
- Tech Founders
- Gen Z Students
- Digital Marketers
- Business Owners
- Entrepreneurs

### 5. Structured AI-Generated Content

Each generated post contains:

- **Hook:** A scroll-stopping opening line.
- **Main Content:** Platform-specific post, caption, thread, or script.
- **Call to Action:** A specific action to encourage the audience.
- **Hashtags:** Relevant hashtags for improved content discovery.

### 6. Copy-Ready Output

- Displays generated content in organized sections.
- Provides a complete formatted post in a text area.
- Makes it easy to copy and reuse generated content.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Google Gemini API | AI-powered content generation |
| Google GenAI SDK | Gemini API integration |
| Pydantic | Structured response validation |
| python-dotenv | Environment variable management |
| JSON | Structured AI response handling |

## 📂 Project Structure

```text
AI_Social_Media_Generator/
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
cd TopMentor_Coursework/projects/AI_Social_Media_Generator
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

Never upload your `.env` file or expose your API key on GitHub.

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

1. Select your target social media platform.
2. Choose the desired brand tone.
3. Select your primary marketing objective.
4. Enter your target audience.
5. Describe your main topic or campaign idea.
6. Click **Generate Post**.
7. Review the generated hook, main content, CTA, and hashtags.
8. Copy the ready-to-use social media content.

## 🎯 Key Learning Outcomes

- Integrating Google Gemini API into Python applications.
- Applying prompt engineering for content generation.
- Generating platform-specific social media content.
- Using Pydantic for structured AI responses.
- Building interactive applications with Streamlit.
- Implementing audience and objective-based content customization.
- Managing API keys using environment variables.
- Generating reusable content dynamically using Python.

## ⚠️ Limitations

- Generated content may require human editing before publication.
- Platform character limits and formatting should be verified before posting.
- Hashtag recommendations do not guarantee increased reach or engagement.
- The application generates content but does not directly publish posts to social media platforms.

## 👩‍💻 Author

**Riham Hussain**

AI & Data Science Enthusiast

GitHub: [Riham203](https://github.com/Riham203)
