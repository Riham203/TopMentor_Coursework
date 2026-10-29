import os
import re
import sys
from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load variables from .env file into environment
load_dotenv()


class GeminiDataAnalystAgent:

    def __init__(self, api_key: str = None):
        """Initializes the Gemini Client using official google-genai SDK."""
        # Prioritize passed api_key, fallback to loaded GEMINI_API_KEY from .env
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError(
                "Gemini API Key is missing. Ensure GEMINI_API_KEY is set in your .env file."
            )

        self.client = genai.Client(api_key=self.api_key)
        self.model_name = "gemini-3.6-flash"

    def _get_dataframe_context(self, df: pd.DataFrame) -> str:
        """Extracts column types, sample rows, and numerical summaries for Gemini context."""
        buffer = StringIO()
        df.info(buf=buffer)
        info_str = buffer.getvalue()

        summary_str = f"""
Dataset Summary:
- Shape: {df.shape[0]} rows, {df.shape[1]} columns
- Columns & Types:
{info_str}

First 3 Rows:
{df.head(3).to_string()}
"""
        return summary_str

    def generate_analysis_code(self, df: pd.DataFrame, user_query: str) -> str:
        """Prompts Gemini to generate executable Python code tailored to the DataFrame context."""
        dataset_context = self._get_dataframe_context(df)

        system_instruction = """
You are an expert Python Data Analyst Agent. 
Your goal is to write executable Python code to analyze a Pandas DataFrame named `df` and answer the user's request.

Rules:
1. Return ONLY executable Python code inside a standard markdown ```python ``` code block.
2. The DataFrame is pre-loaded as `df`. Do NOT reload or recreate `df`.
3. Save any generated charts/plots to a variable or display them using `plt.gcf()` (do not call plt.show()).
4. Print key text outputs, summaries, or analytical insights using standard `print()` statements.
5. Do NOT import malicious packages. Use only pandas, numpy, matplotlib, seaborn.
"""

        prompt = f"""
Context of dataset `df`:
{dataset_context}

User Question: {user_query}

Write the complete Python code to answer this query:
"""

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.1,
            ),
        )

        raw_text = response.text
        code_match = re.search(r"```python\s*(.*?)\s*```", raw_text, re.DOTALL)

        if code_match:
            return code_match.group(1).strip()
        return raw_text.strip()

    def execute_agent_code(self, df: pd.DataFrame, code_str: str) -> dict:
        """Safely executes generated Python code, capturing stdout printed text logs and Matplotlib figures."""
        # Capture stdout from prints inside generated code
        old_stdout = sys.stdout
        redirected_output = StringIO()
        sys.stdout = redirected_output

        # Clear existing active matplotlib figures
        plt.clf()
        plt.close("all")

        # Execution namespace scope configuration
        execution_scope = {
            "df": df,
            "pd": pd,
            "plt": plt,
        }

        try:
            import matplotlib

            matplotlib.use("Agg")
            import seaborn as sns

            execution_scope["sns"] = sns
        except ImportError:
            pass

        error_message = None
        fig = None

        try:
            exec(code_str, execution_scope)
            printed_text = redirected_output.getvalue()

            # Extract generated matplotlib figure if available
            if plt.get_fignums():
                fig = plt.gcf()

        except Exception as e:
            error_message = str(e)
            printed_text = redirected_output.getvalue()
        finally:
            sys.stdout = old_stdout

        return {
            "text_output": printed_text,
            "figure": fig,
            "error": error_message,
        }


# ==========================================
# EXAMPLE EXECUTION SCRIPT
# ==========================================
if __name__ == "__main__":
    # Sample Dataset
    data = {
        "Date": pd.date_range(start="2026-01-01", periods=5, freq="D"),
        "Region": ["North", "South", "East", "West", "North"],
        "Category": [
            "Electronics",
            "Furniture",
            "Electronics",
            "Clothing",
            "Furniture",
        ],
        "Sales": [1800, 1500, 2400, 1125, 3200],
    }
    df = pd.DataFrame(data)

    query = "What is the total sales per Region? Display a bar chart."

    print("🚀 Initializing Gemini Data Analyst Agent...")
    try:
        agent = GeminiDataAnalystAgent()

        print(f"\n❓ User Question: {query}")
        print("\n🤖 Generating Python Analysis Code via Gemini...")
        generated_code = agent.generate_analysis_code(df, query)

        print("\n📝 --- Generated Python Code ---")
        print(generated_code)
        print("-------------------------------")

        print("\n⚙️ Executing Generated Code...")
        result = agent.execute_agent_code(df, generated_code)

        if result["error"]:
            print(f"\n❌ Execution Error: {result['error']}")
        else:
            print("\n📊 --- Analytical Output ---")
            print(result["text_output"])

            if result["figure"]:
                print("✅ Chart generated successfully!")
                # plt.show() # Uncomment if running locally with interactive UI

    except ValueError as err:
        print(f"\n⚠️ Initialization Error: {err}")