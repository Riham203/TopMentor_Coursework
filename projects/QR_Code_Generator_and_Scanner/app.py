import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pypdf import PdfReader


load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



def extract_text_from_pdf(pdf_file) -> str:
    """Extracts raw text content from an uploaded PDF file."""
    pdf_reader = PdfReader(pdf_file)
    extracted_text = ""
    for page_num, page in enumerate(pdf_reader.pages, start=1):
        page_text = page.extract_text()
        if page_text:
            extracted_text += f"\n--- Page {page_num} ---\n" + page_text
    return extracted_text


def build_system_instruction(pdf_text: str) -> str:
    """
    Constructs System Prompt applying Prompt Engineering:
    - Persona Assignment (Document Intelligence Assistant)
    - Strict Grounding Constraints (Prevents Hallucinations)
    - Context Injection (Extracted PDF Text)
    """
    return f"""
    You are an intelligent Document Assistant. Your job is to accurately answer user questions 
    based ONLY on the provided PDF document context below.

    ### STRICT CONSTRAINTS:
    1. Answer the question using ONLY information explicitly stated in the context.
    2. If the answer cannot be found in the document, reply with: 
       "I'm sorry, but that information is not mentioned in the uploaded PDF document."
    3. Do NOT invent facts or rely on external general knowledge outside this text.
    4. Cite page numbers where possible when referencing specific facts (e.g., "[Page 2]").

    ### DOCUMENT CONTEXT:
    {pdf_text}
    """



st.set_page_config(page_title="PDF Chatbot - Gemini AI", page_icon="💬", layout="wide")

st.title("💬 PDF Chatbot using Google Gemini")
st.caption("Powered by Prompt Engineering & Gemini Flash")


st.sidebar.header("📂 Document Upload")
uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = None

if "processed_file_name" not in st.session_state:
    st.session_state.processed_file_name = None


if uploaded_file is not None:
    if st.session_state.processed_file_name != uploaded_file.name:
        with st.spinner("Extracting text from PDF..."):
            extracted_text = extract_text_from_pdf(uploaded_file)
            st.session_state.pdf_text = extracted_text
            st.session_state.processed_file_name = uploaded_file.name
            st.session_state.chat_history = []  # Clear previous chat on new upload
            st.sidebar.success(f"Successfully processed: {uploaded_file.name}")

if st.session_state.pdf_text:
    st.sidebar.info(f"📄 Active File: **{st.session_state.processed_file_name}**")
    if st.sidebar.button("🗑️ Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()


for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if user_question := st.chat_input("Ask a question about your PDF..."):
    if not st.session_state.pdf_text:
        st.warning("Please upload a PDF document first before asking questions.")
    else:
       
        st.chat_message("user").markdown(user_question)
        st.session_state.chat_history.append({"role": "user", "content": user_question})

        
        with st.chat_message("assistant"):
            with st.spinner("Analyzing document context..."):
                try:
                    system_instruction = build_system_instruction(st.session_state.pdf_text)
                    
                    config = types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.2,  # Low temperature for strict factual accuracy
                    )

                    # Build conversation contents for Gemini
                    contents = []
                    for msg in st.session_state.chat_history:
                        contents.append(msg["content"])

                    response = client.models.generate_content(
                        model="gemini-3.6-flash",
                        contents=contents,
                        config=config
                    )

                    st.markdown(response.text)
                    st.session_state.chat_history.append({"role": "assistant", "content": response.text})

                except Exception as e:
                    st.error(f"Error processing query: {e}")