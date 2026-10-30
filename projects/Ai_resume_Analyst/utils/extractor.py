import pdfplumber
import docx
import io

def extract_text_from_pdf(file_bytes) -> str:
    """Extract text from a PDF file buffer."""
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

def extract_text_from_docx(file_bytes) -> str:
    """Extract text from a DOCX file buffer."""
    doc = docx.Document(io.BytesIO(file_bytes))
    full_text = [para.text for para in doc.paragraphs if para.text]
    return "\n".join(full_text).strip()

def parse_resume_text(uploaded_file) -> str:
    """Route file to appropriate parser based on extension."""
    file_bytes = uploaded_file.read()
    filename = uploaded_file.name.lower()
    
    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file_bytes)
    elif filename.endswith(".docx"):
        return extract_text_from_docx(file_bytes)
    else:
        raise ValueError("Unsupported file format. Please upload PDF or DOCX.")
