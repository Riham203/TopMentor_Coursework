import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title=" Chatbot", page_icon="✨")
st.title("🤖 AI Chatbot")

if not api_key:
    st.error("Missing `GEMINI_API_KEY`. Add it to your `.env` file.")
    st.stop()

client = genai.Client(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Ask Gemini anything..."):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    
    contents = [
        {"role": "model" if msg["role"] == "assistant" else "user", "parts": [{"text": msg["content"]}]}
        for msg in st.session_state.messages
    ]

    with st.chat_message("assistant"):
        try:
           
            response_stream = client.models.generate_content_stream(
                    model="gemini-3.6-flash", 
                    contents=contents
            )
            
            
            def stream_parser():
                for chunk in response_stream:
                    if chunk.text:
                        yield chunk.text

            full_response = st.write_stream(stream_parser())
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except APIError as e:
            st.error(f"Gemini API Error: {e}")
        except Exception as e:
            st.error(f"An error occurred: {e}")