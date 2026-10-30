# 💼 AI Business Name Generator

An AI-powered business name generator built using **Python, Streamlit, and Google Gemini API**. This application helps entrepreneurs and startups generate creative brand names based on their industry and preferred brand tone.

It also generates a brand mission statement and suggests a color palette to help establish a brand identity.

## ✨ Features

- **🏢 Industry-Based Suggestions:** Generate business names based on your startup's industry.
- **🎨 Tone-Based Branding:** Customize suggestions based on your preferred brand tone.
- **💡 AI-Powered Name Generation:** Generate five catchy business name ideas using Google Gemini.
- **📝 Brand Mission:** Generate a one-sentence brand mission.
- **🌈 Color Palette Suggestions:** Get suggested brand colors with HEX codes.
- **🖥️ Interactive Interface:** Simple user interface built with Streamlit.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Google Gemini API | AI-powered content generation |
| python-dotenv | Environment variable management |

## 📁 Project Structure

```text
AI_Business_Name_Generator/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
cd TopMentor_Coursework/projects/Ai_buisness_name_generator
```

Navigate to the Business Name Generator project folder inside `projects`.

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

Create a `requirements.txt` file containing:

```text
streamlit
python-dotenv
google-genai
```

Install the packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API Key

Get your API key from [Google AI Studio](https://aistudio.google.com/).

Create a `.env` file in the project directory:

```env
gemini=your_gemini_api_key_here
```

**Important:** The application currently reads the API key using `os.getenv('gemini')`. Keep the variable name consistent.

Never upload your `.env` file or API key to GitHub.

Add this to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.py[cod]
```

## 🚀 Running the Application

Run the following command:

```bash
streamlit run app.py
```

The application will open in your browser.

## 💻 How to Use

1. Launch the application.
2. Enter your startup's industry (e.g., Fashion, Technology, Food, Healthcare).
3. Enter your preferred brand tone (e.g., Modern, Luxury, Minimalist, Playful, Professional).
4. Click **Submit**.
5. Wait for Gemini AI to generate the branding suggestions.
6. Explore the five business names, brand mission, and suggested color palette.

## 💡 Example Input

**Industry:** Fashion

**Brand Tone:** Modern, Minimalist, and Premium

## 🎯 Expected Output

The application generates:

1. Five catchy business name suggestions.
2. A one-sentence brand mission.
3. A suggested brand color palette with HEX codes.

*Note: Actual suggestions are generated dynamically by Gemini based on the input.*

## 🧠 How It Works

1. Collects the startup industry and preferred brand tone through Streamlit form inputs.
2. Combines the inputs into a structured prompt.
3. Sends the prompt to the Google Gemini API.
4. Gemini generates business names and branding suggestions.
5. Displays the generated response in the Streamlit interface.

## 📚 Learning Outcomes

This project demonstrates practical experience with:

- Generative AI and Large Language Models.
- Integrating Google Gemini API with Python.
- Prompt engineering.
- Building interactive applications using Streamlit.
- Managing API credentials using environment variables.
- Generating AI-powered branding content.

## 🔮 Future Improvements

- Add business name availability checking.
- Generate logo concepts for suggested names.
- Provide multiple naming styles.
- Add domain name availability checking.
- Allow users to download branding suggestions.
- Add brand personality and target audience inputs.

## ⚠️ Important Considerations

- Generated business names may already be in use.
- Trademark and domain availability should be checked independently.
- Gemini API access and usage limits apply.
- AI-generated branding suggestions should be reviewed before commercial use.

## 👩‍💻 Author

**Riham**

GitHub: [@Riham203](https://github.com/Riham203)

---

*Built as a hands-on project exploring Generative AI, prompt engineering, and AI-powered branding.*
