# 🤖 Transformer-Based Text Summarization Engine

Hi, I'm **Riham Hussain**, an AI & Data Science Enthusiast! 👋

An end-to-end Python-based text summarization engine powered by **Hugging Face Transformers** and the pre-trained `facebook/bart-large-cnn` model.

The project is designed to summarize long-form technical documents by splitting them into manageable chunks, generating individual summaries, and combining them into a consolidated summary while preserving important context.

---

## ✨ Key Features

- **Transformer-Based Summarization:** Uses the pre-trained BART model (`facebook/bart-large-cnn`) for abstractive text summarization.
- **Sentence-Aware Chunking:** Splits long documents at sentence boundaries instead of cutting text arbitrarily.
- **Token-Aware Processing:** Uses the model tokenizer to keep chunks within the configured token budget.
- **Overlapping Context Windows:** Retains sentences from previous chunks to reduce context loss between segments.
- **Map-Reduce Summarization:** Summarizes individual chunks and consolidates intermediate summaries when necessary.
- **Dynamic Summary Length:** Calculates summary length parameters based on the requested reduction ratio.
- **Device Detection:** Automatically selects CUDA when available, otherwise uses CPU.
- **Summary Statistics:** Reports original word count, summary word count, and actual reduction percentage.

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Deep Learning Framework | PyTorch |
| NLP / Transformers | Hugging Face Transformers |
| Pre-trained Model | BART (`facebook/bart-large-cnn`) |
| Tokenization | AutoTokenizer |
| Model Architecture | Sequence-to-Sequence |
| Processing | Regular Expressions |

---

## 📂 Project Structure

```text
summarizer/
│
├── src/
│   └── summarizer.py       # Core DocumentSummarizer implementation
│
├── main.py                 # Main execution entry point
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── .gitignore              # Ignored files and folders
```

---

## ⚙️ How It Works

The summarization engine follows a multi-stage processing pipeline.

### 1. Document Input

Accepts long-form text as input for summarization.

### 2. Sentence Splitting

Uses regular expressions to identify sentence boundaries and divide the document into sentences.

### 3. Token-Aware Chunking

- Measures sentence lengths using the BART tokenizer.
- Groups sentences into chunks within the configured token limit.
- Maintains overlapping sentences between consecutive chunks to preserve context.

### 4. Map Phase – Individual Summarization

Each chunk is processed independently using the BART model to generate a shorter summary.

### 5. Reduce Phase – Summary Consolidation

If the combined intermediate summaries exceed the configured token threshold, another summarization pass is performed to consolidate them.

### 6. Final Output

Returns:

- Final summarized text
- Original word count
- Summary word count
- Actual reduction percentage

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or later
- pip package manager
- Internet connection for downloading the pre-trained model on first use
- Sufficient memory to load the BART model

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
cd TopMentor_Coursework/projects/AI_Legal_Document_Assistant
```

### 2. Create a Virtual Environment

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

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the main execution script:

```bash
python main.py
```

The script initializes the summarization engine, processes sample technical text, and displays the summarization results in the terminal.

The first execution may take longer because the pre-trained BART model needs to be downloaded and loaded.

---

## 💻 Python API Usage

You can also import the `DocumentSummarizer` class into another Python program.

```python
from src.summarizer import DocumentSummarizer

# Initialize the summarization engine
engine = DocumentSummarizer(
    model_name="facebook/bart-large-cnn",
    max_chunk_tokens=600,
    overlap_tokens=80
)

# Provide document text
report_text = """
Your long technical report or document text goes here.
"""

# Generate summary targeting 70% reduction
result = engine.summarize_document(
    report_text,
    target_reduction=0.70
)

# Display results
print("Summary:", result["summary"])
print("Original Word Count:", result["original_word_count"])
print("Summary Word Count:", result["summary_word_count"])
print("Reduction:", result["reduction_percentage"], "%")
```

---

## 🔧 Configuration

The summarization engine supports configurable parameters.

| Parameter | Description |
|---|---|
| `model_name` | Hugging Face model identifier |
| `max_chunk_tokens` | Maximum token budget for each chunk |
| `overlap_tokens` | Number of tokens retained from previous chunks |
| `device` | Execution device: CUDA or CPU, with automatic detection by default |
| `target_reduction` | Desired proportion of text to remove |

Example configuration:

```python
engine = DocumentSummarizer(
    model_name="facebook/bart-large-cnn",
    max_chunk_tokens=600,
    overlap_tokens=80
)
```

A `target_reduction` of `0.70` requests approximately 70% compression. The actual reduction is calculated from the final word counts and may differ from the requested value.

---

## 📚 Learning Outcomes

Through this project, I explored:

- Transformer-based NLP applications.
- Pre-trained sequence-to-sequence models.
- Hugging Face Transformers and tokenizers.
- Abstractive text summarization using BART.
- Token-aware document processing.
- Sentence boundary detection and overlapping chunking.
- Map-Reduce strategies for long-document summarization.
- Dynamic output-length configuration.
- PyTorch inference and device selection.
- Building reusable Python classes and modules.

---

## ⚠️ Limitations

- The project currently processes text strings rather than directly extracting text from PDF or Word documents.
- The sample execution script uses predefined technical text.
- The BART model has input token limits, so long documents are handled through chunking.
- Summaries may omit details or occasionally produce inaccurate information, as with other generative summarization models.
- Actual compression depends on the input and model output; the requested reduction is not guaranteed.

## 👩‍💻 Author

**Riham Hussain**

AI & Data Science Enthusiast

GitHub: [@Riham203](https://github.com/Riham203)
