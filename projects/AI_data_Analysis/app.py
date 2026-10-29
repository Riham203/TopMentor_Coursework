import os
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from analyst_agent import GeminiDataAnalystAgent

# Load environment variables from .env file
load_dotenv()

st.set_page_config(
    page_title="AI Data Analyst Agent (Gemini)", page_icon="🤖", layout="wide"
)

st.title("🤖 AI Data Analyst Agent")
st.caption("Powered by Google Gemini AI & Automated Python Code Execution")

# Sidebar Configuration: API Key Input & Dataset Upload
st.sidebar.header("⚙️ Configuration")

api_key_input = os.getenv("GEMINI_API_KEY")

uploaded_file = st.sidebar.file_uploader(
    "Upload Dataset (CSV or Excel)", type=["csv", "xlsx"]
)


@st.cache_data
def load_data(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    else:
        return pd.read_excel(file)


if uploaded_file is not None:
    df = load_data(uploaded_file)

    st.subheader("📊 Dataset Preview")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.dataframe(df, use_container_width=True)
    with col2:
        st.metric("Total Rows", df.shape[0])
        st.metric("Total Columns", df.shape[1])

    st.markdown("---")
    st.subheader("💬 Ask the AI Data Analyst")

    user_query = st.text_input(
        "Ask a question about your data:",
        placeholder="e.g., What are the top 5 revenue-generating product categories? Show a bar chart.",
    )

    if st.button("🚀 Run Analysis", type="primary"):
        if not api_key_input:
            st.error(
                "Please enter your GEMINI_API_KEY in .env."
            )
        elif not user_query.strip():
            st.warning("Please type a valid question.")
        else:
            with st.spinner(
                "Gemini AI Agent is inspecting data schema & generating Python analysis code..."
            ):
                try:
                    agent = GeminiDataAnalystAgent(api_key=api_key_input)
                    generated_code = agent.generate_analysis_code(
                        df, user_query
                    )

                    st.markdown("### 🛠️ Agent Generated Code")
                    with st.expander(
                        "View Generated Python Code", expanded=False
                    ):
                        st.code(generated_code, language="python")

                    # Execute Code
                    execution_result = agent.execute_agent_code(
                        df, generated_code
                    )

                    st.markdown("### 📈 Agent Analytical Output")

                    if execution_result["error"]:
                        st.error(
                            f"Execution Error: {execution_result['error']}"
                        )

                    if execution_result["text_output"]:
                        st.info(execution_result["text_output"])

                    if execution_result["figure"]:
                        st.pyplot(execution_result["figure"])

                except Exception as e:
                    st.error(f"Agent Pipeline Failed: {str(e)}")

else:
    st.info("👈 Please upload a CSV or Excel file in the sidebar to start.")