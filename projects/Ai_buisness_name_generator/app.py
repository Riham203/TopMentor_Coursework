import os
from dotenv import load_dotenv
from google import genai
import streamlit as st
load_dotenv()

api_key = os.getenv('gemini')

client = genai.Client(api_key=api_key)

st.set_page_config(
    page_title="Business Name Generator",
    page_icon="💼"
)
st.title("Business Name Generator")

with st.form("business_name_form"):
    industry = st.text_input("What type of your startup?")
    tone = st.text_input("What tone should the brand be in?")

    submit_button = st.form_submit_button("Submit")
    if submit_button:
        prompt_content = f"""
             Role: Branding Expert.
                Target: {industry}. Tone: {tone}.
                Provide:
                   1. 5 catchy names
                   2. A 1-sentence brand mission
                   3. A color palette suggestion (Hex codes)
        """
        with st.spinner("Generating business names..."):
            response = client.models.generate_content(
                model = 'gemini-3.6-flash',
                contents = prompt_content
            )

        st.success("Done!")
        st.write(response.text)