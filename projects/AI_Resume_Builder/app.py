import json
import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, Field


load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



class WorkExperience(BaseModel):
    company: str = Field(description="Name of the company or organization")
    role: str = Field(description="Job title or designation")
    bullet_points: list[str] = Field(
        description="Action-oriented bullet points with quantified achievements"
    )


class ResumeData(BaseModel):
    professional_summary: str = Field(
        description="A compelling 3-4 sentence professional summary targeted to the job role"
    )
    core_skills: list[str] = Field(
        description="A list of 8-12 high-impact technical and domain skills matching the target role"
    )
    work_experience: list[WorkExperience] = Field(
        description="Rewritten work experience items focused on impact and metrics"
    )
    ats_keywords: list[str] = Field(
        description="Important ATS keywords extracted from the target job description"
    )


def build_prompt(
    target_role: str, experience_level: str, raw_experience: str, job_description: str
) -> tuple[str, str]:
    """Constructs System and User instructions applying Prompt Engineering techniques:

    - Persona Prompting (Executive Resume Writer & HR Recruiter)
    - X-Y-Z Bullet Point Formula (Accomplished [X], measured by [Y], by doing [Z])
    - ATS Optimization Constraints
    """

    system_instruction = (
        "You are an elite Executive Resume Writer and Talent Acquisition Specialist. "
        "Your task is to craft high-impact, ATS-optimized resumes that highlight measurable achievements, "
        "strong action verbs, and tailored keywords."
    )

    user_prompt = f"""
    ### TASK
    Transform the raw candidate experience into a polished, professional, ATS-optimized resume.

    ### INPUT CONTEXT
    - **Target Job Role:** {target_role}
    - **Experience Level:** {experience_level}
    - **Candidate Raw Background / Experience:** {raw_experience}
    - **Target Job Description (for keyword alignment):** {job_description if job_description.strip() else 'N/A - Optimize for industry standards'}

    ### FORMATTING & STRUCTURAL RULES
    1. **Professional Summary:** Write a powerful summary establishing candidate value proposition in 3-4 sentences.
    2. **Core Skills:** Extract and categorize high-converting skills relevant to the target role.
    3. **Work Experience Bullet Points:** 
       - Start every bullet with a strong action verb (e.g., 'Engineered', 'Spearheaded', 'Optimized').
       - Follow Google's X-Y-Z formula: Accomplished [X], as measured by [Y], by doing [Z].
       - Inject realistic metrics and percentages where contextually appropriate.
    4. **ATS Keywords:** Identify crucial ATS keywords present in or relevant to the job role.
    """

    return system_instruction, user_prompt


def generate_resume(
    target_role: str, experience_level: str, raw_experience: str, job_description: str
) -> dict:
    system_instruction, user_prompt = build_prompt(
        target_role, experience_level, raw_experience, job_description
    )

    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.6,
        response_mime_type="application/json",
        response_schema=ResumeData,
    )

    response = client.models.generate_content(
        model="gemini-3.6-flash", contents=user_prompt, config=config
    )

    return json.loads(response.text)



st.set_page_config(
    page_title="AI Resume Builder & ATS Optimizer", page_icon="📄", layout="wide"
)

st.title("📄 AI Resume Builder & ATS Optimizer")
st.caption("Powered by Prompt Engineering & Google Gemini")

col1, col2 = st.columns([1, 1])

with col1:
    st.header("🎯 Target Details")
    target_role = st.text_input(
        "Target Job Title / Role", placeholder="e.g., Senior Data Engineer"
    )
    experience_level = st.selectbox(
        "Experience Level",
        [
            "Entry-Level (0-2 years)",
            "Mid-Level (3-5 years)",
            "Senior / Lead (6+ years)",
            "Executive / Manager",
        ],
    )
    job_description = st.text_area(
        "Target Job Description (Optional for ATS Keyword Matching)",
        height=150,
        placeholder="Paste target job posting here to match ATS keywords...",
    )

with col2:
    st.header("👤 Your Background")
    raw_experience = st.text_area(
        "Raw Work History / Draft Experience",
        height=240,
        placeholder="Paste your unformatted work experience, key projects, technologies used, and responsibilities...",
    )

if st.button("✨ Build Optimized Resume", type="primary", use_container_width=True):
    if not target_role.strip():
        st.warning("Please enter a target job role.")
    elif not raw_experience.strip():
        st.warning("Please provide your raw work history or experience.")
    else:
        with st.spinner("Writing and optimizing your resume..."):
            try:
                result = generate_resume(
                    target_role, experience_level, raw_experience, job_description
                )

                st.divider()
                st.subheader("📌 Generated Resume Profile")

                st.markdown("### 📝 Professional Summary")
                st.info(result.get("professional_summary"))

                st.markdown("### 🛠️ Core Skills")
                skills = result.get("core_skills", [])
                st.write(" • ".join(skills))

                st.markdown("### 💼 Work Experience")
                for exp in result.get("work_experience", []):
                    st.markdown(f"**{exp.get('role')}** — *{exp.get('company')}*")
                    for bullet in exp.get("bullet_points", []):
                        st.markdown(f"- {bullet}")
                    st.write("")

                st.markdown("### 🔑 Extracted ATS Keywords")
                st.code(" | ".join(result.get("ats_keywords", [])))

                # Formatted Markdown for easy copying
                full_md = f"# Professional Summary\n{result.get('professional_summary')}\n\n## Core Skills\n"
                full_md += ", ".join(skills) + "\n\n## Work Experience\n"
                for exp in result.get("work_experience", []):
                    full_md += f"### {exp.get('role')} - {exp.get('company')}\n"
                    for bullet in exp.get("bullet_points", []):
                        full_md += f"* {bullet}\n"
                    full_md += "\n"

                st.text_area("Copy Markdown Resume:", full_md, height=250)

            except Exception as e:
                st.error(f"Error generating resume: {e}")