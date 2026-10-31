import json
import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from pypdf import PdfReader


load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



class RiskClause(BaseModel):
    clause_name: str = Field(description="Name or title of the clause (e.g., Indemnification, Termination)")
    risk_level: str = Field(description="High, Medium, or Low risk rating")
    explanation: str = Field(description="Detailed legal explanation of why this clause presents a risk")
    recommendation: str = Field(description="Suggested revision or mitigation step")


class LegalAuditReport(BaseModel):
    document_type: str = Field(description="Identified contract type (e.g., NDA, Service Agreement, Employment Contract)")
    effective_date: str = Field(description="Effective date or execution date of the agreement")
    parties_involved: list[str] = Field(description="Entities or individuals entering into the contract")
    governing_law: str = Field(description="Jurisdiction or governing law specified in the agreement")
    key_obligations: list[str] = Field(description="Primary duties and responsibilities assigned to each party")
    high_risk_clauses: list[RiskClause] = Field(description="List of identified risky or unfair clauses requiring legal review")



def extract_text_from_pdf(pdf_file) -> str:
    """Extracts raw text content from an uploaded legal PDF file."""
    pdf_reader = PdfReader(pdf_file)
    extracted_text = ""
    for page_num, page in enumerate(pdf_reader.pages, start=1):
        page_text = page.extract_text()
        if page_text:
            extracted_text += f"\n--- Page {page_num} ---\n" + page_text
    return extracted_text


def run_legal_audit(contract_text: str) -> dict:
    """Performs structured legal analysis using Gemini JSON schema enforcement."""
    system_instruction = (
        "You are an expert Legal Counsel and Contract Auditor. Your task is to perform "
        "a rigorous review of the provided legal agreement, extracting key metadata, primary obligations, "
        "and auditing the contract for high-risk, ambiguous, or non-standard legal clauses."
    )

    user_prompt = f"""
    Perform a complete legal audit on the following agreement:

    ### CONTRACT TEXT:
    {contract_text}
    """

    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.2,  # Low temperature for precise legal compliance
        response_mime_type="application/json",
        response_schema=LegalAuditReport,
    )

    response = client.models.generate_content(
        model="gemini-3.6-flash", contents=user_prompt, config=config
    )

    return json.loads(response.text)


def build_qa_system_instruction(contract_text: str) -> str:
    """System prompt for legal Q&A grounded strictly in contract text."""
    return f"""
    You are a Legal Assistant specializing in contract interpretation. Answer user questions 
    strictly based on the contract context provided below.

    ### LEGAL GROUNDING RULES:
    1. Base your answer ONLY on explicit terms found in the provided contract.
    2. If a specific clause or term is absent, explicitly state: 
       "This contract does not contain specific clauses addressing this issue."
    3. Do NOT provide binding legal advice; provide factual contract analysis.
    4. Quote or cite relevant page/section markers when possible.

    ### CONTRACT CONTEXT:
    {contract_text}
    """


st.set_page_config(page_title="AI Legal Document Assistant", page_icon="⚖️", layout="wide")

st.title("⚖️ AI Legal Document Assistant")
st.caption("Powered by Prompt Engineering & Google Gemini")


st.sidebar.header("📂 Contract Upload")
uploaded_file = st.sidebar.file_uploader("Upload Legal Agreement (PDF)", type=["pdf"])


if "contract_text" not in st.session_state:
    st.session_state.contract_text = None

if "audit_report" not in st.session_state:
    st.session_state.audit_report = None

if "qa_chat_history" not in st.session_state:
    st.session_state.qa_chat_history = []

if "processed_file_name" not in st.session_state:
    st.session_state.processed_file_name = None


if uploaded_file is not None:
    if st.session_state.processed_file_name != uploaded_file.name:
        with st.spinner("Parsing legal document..."):
            extracted_text = extract_text_from_pdf(uploaded_file)
            st.session_state.contract_text = extracted_text
            st.session_state.processed_file_name = uploaded_file.name
            st.session_state.audit_report = None
            st.session_state.qa_chat_history = []
            st.sidebar.success(f"Loaded: {uploaded_file.name}")


tab1, tab2 = st.tabs(["🔍 Contract Audit & Risk Analysis", "💬 Interactive Legal Q&A"])


with tab1:
    if not st.session_state.contract_text:
        st.info("Please upload a legal document (PDF) in the sidebar to begin analysis.")
    else:
        if st.button("🚀 Run Comprehensive Legal Audit", type="primary"):
            with st.spinner("Auditing contract clauses and extracting metadata..."):
                try:
                    report = run_legal_audit(st.session_state.contract_text)
                    st.session_state.audit_report = report
                except Exception as e:
                    st.error(f"Error analyzing contract: {e}")

        if st.session_state.audit_report:
            report = st.session_state.audit_report

            st.markdown("## 📌 Key Contract Metadata")
            col1, col2, col3 = st.columns(3)
            col1.metric("Document Type", report.get("document_type", "N/A"))
            col2.metric("Effective Date", report.get("effective_date", "N/A"))
            col3.metric("Governing Law", report.get("governing_law", "N/A"))

            st.markdown("### 🤝 Parties Involved")
            st.write(", ".join(report.get("parties_involved", [])))

            st.markdown("### 📋 Core Obligations")
            for obligation in report.get("key_obligations", []):
                st.markdown(f"- {obligation}")

            st.markdown("### ⚠️ High Risk & Ambiguous Clauses")
            risks = report.get("high_risk_clauses", [])
            if risks:
                for risk in risks:
                    level = risk.get("risk_level", "Medium")
                    badge_color = "🔴" if level.lower() == "high" else "🟡"
                    with st.expander(f"{badge_color} **{risk.get('clause_name')}** ({level} Risk)"):
                        st.markdown(f"**Explanation:** {risk.get('explanation')}")
                        st.markdown(f"**Mitigation Recommendation:** {risk.get('recommendation')}")
            else:
                st.success("No critical high-risk clauses were flagged in this document.")


with tab2:
    if not st.session_state.contract_text:
        st.info("Please upload a legal document (PDF) in the sidebar to ask questions.")
    else:
        st.markdown("### Ask questions regarding liabilities, termination terms, payment deadlines, etc.")

        for msg in st.session_state.qa_chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if question := st.chat_input("e.g., What are the terms for agreement termination?"):
            st.chat_message("user").markdown(question)
            st.session_state.qa_chat_history.append({"role": "user", "content": question})

            with st.chat_message("assistant"):
                with st.spinner("Scanning contract text..."):
                    try:
                        system_inst = build_qa_system_instruction(st.session_state.contract_text)
                        config = types.GenerateContentConfig(
                            system_instruction=system_inst,
                            temperature=0.1
                        )

                        contents = [msg["content"] for msg in st.session_state.qa_chat_history]
                        response = client.models.generate_content(
                            model="gemini-3.6-flash",
                            contents=contents,
                            config=config
                        )

                        st.markdown(response.text)
                        st.session_state.qa_chat_history.append({"role": "assistant", "content": response.text})

                    except Exception as e:
                        st.error(f"Error answering legal query: {e}")