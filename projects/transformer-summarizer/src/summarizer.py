import math
import re
from typing import List
import torch #type: ignore
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM #type: ignore


class DocumentSummarizer:
    def __init__(
        self,
        model_name: str = "facebook/bart-large-cnn",
        max_chunk_tokens: int = 800,
        overlap_tokens: int = 100,
        device: str = None
    ):
        """
        Initializes the BART-based text summarizer with chunking capabilities.
        
        :param model_name: Hugging Face model identifier
        :param max_chunk_tokens: Maximum tokens per chunk (below BART's 1024 token limit)
        :param overlap_tokens: Overlap between consecutive chunks to retain context
        :param device: Computing device ('cuda', 'cpu', or auto-detect)
        """
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device
            
        print(f"Loading model '{model_name}' on device '{self.device}'...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(self.device)
        
        self.max_chunk_tokens = max_chunk_tokens
        self.overlap_tokens = overlap_tokens

    def _split_into_sentences(self, text: str) -> List[str]:
        """Splits raw text into sentences using standard regex patterns."""
        sentence_endings = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s')
        sentences = sentence_endings.split(text)
        return [s.strip() for s in sentences if s.strip()]

    def _create_token_aware_chunks(self, text: str) -> List[str]:
        """
        Splits long document into overlapping chunks without breaking mid-sentence.
        """
        sentences = self._split_into_sentences(text)
        chunks = []
        current_chunk_sentences = []
        current_token_count = 0

        for sentence in sentences:
            sentence_tokens = len(self.tokenizer.encode(sentence, add_special_tokens=False))
            
            # If adding this sentence exceeds chunk budget, finalize current chunk
            if current_token_count + sentence_tokens > self.max_chunk_tokens and current_chunk_sentences:
                chunk_text = " ".join(current_chunk_sentences)
                chunks.append(chunk_text)
                
                # Build overlap window from tail sentences of previous chunk
                overlap_sentences = []
                overlap_count = 0
                for s in reversed(current_chunk_sentences):
                    s_tokens = len(self.tokenizer.encode(s, add_special_tokens=False))
                    if overlap_count + s_tokens <= self.overlap_tokens:
                        overlap_sentences.insert(0, s)
                        overlap_count += s_tokens
                    else:
                        break
                
                current_chunk_sentences = overlap_sentences
                current_token_count = overlap_count

            current_chunk_sentences.append(sentence)
            current_token_count += sentence_tokens

        # Append remaining sentences
        if current_chunk_sentences:
            chunks.append(" ".join(current_chunk_sentences))

        return chunks

    def _summarize_chunk(self, chunk_text: str, target_reduction: float = 0.70) -> str:
        """
        Summarizes an individual text chunk using BART.
        Calculates dynamic min/max lengths to hit the target condensation ratio (~70%).
        """
        inputs = self.tokenizer(
            chunk_text,
            return_tensors="pt",
            truncation=True,
            max_length=1024
        ).to(self.device)

        input_length = inputs["input_ids"].shape[1]
        
        # Calculate max output tokens based on target reduction ratio (30% length remaining)
        target_max_length = int(input_length * (1.0 - target_reduction))
        max_summary_length = max(30, target_max_length)
        min_summary_length = max(10, int(max_summary_length * 0.5))

        with torch.no_grad():
            summary_ids = self.model.generate(
                inputs["input_ids"],
                num_beams=4,
                max_length=max_summary_length,
                min_length=min_summary_length,
                length_penalty=2.0,
                early_stopping=True,
                no_repeat_ngram_size=3
            )

        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    def summarize_document(self, text: str, target_reduction: float = 0.70) -> dict:
        """
        Processes long-form documents using a multi-stage Map-Reduce approach.
        
        :param text: Full-length raw text input
        :param target_reduction: Desired ratio of text to condense (0.70 = 70% reduction)
        :return: Dict containing final summary, original length, and summary length
        """
        # Step 1: Chunk the text
        chunks = self._create_token_aware_chunks(text)
        print(f"Document split into {len(chunks)} contextual chunk(s). Processing...")

        # Step 2: Summarize each chunk (Map phase)
        chunk_summaries = []
        for idx, chunk in enumerate(chunks, start=1):
            summary = self._summarize_chunk(chunk, target_reduction=target_reduction)
            chunk_summaries.append(summary)

        combined_summary_text = " ".join(chunk_summaries)

        # Step 3: If combined summaries exceed token threshold, perform recursive reduction (Reduce phase)
        combined_token_count = len(self.tokenizer.encode(combined_summary_text, add_special_tokens=False))
        if len(chunks) > 1 and combined_token_count > self.max_chunk_tokens:
            print("Consolidating intermediate chunk summaries...")
            final_summary = self._summarize_chunk(combined_summary_text, target_reduction=0.30)
        else:
            final_summary = combined_summary_text

        orig_word_count = len(text.split())
        summary_word_count = len(final_summary.split())
        actual_reduction = 1.0 - (summary_word_count / orig_word_count if orig_word_count > 0 else 0)

        return {
            "summary": final_summary,
            "original_word_count": orig_word_count,
            "summary_word_count": summary_word_count,
            "reduction_percentage": round(actual_reduction * 100, 2)
        }


# Example Execution pipeline
if __name__ == "__main__":
    # Sample long text simulation
    sample_technical_report = """
    Artificial Intelligence (AI) and Machine Learning (ML) systems have transitioned from theoretical laboratory research 
    into core components of enterprise software ecosystems. Modern distributed enterprise platforms depend heavily on 
    predictive models to manage automated workload placement, infrastructure scaling, and real-time threat analysis. 
    However, deploying complex transformer-based deep learning models at scale presents significant challenges regarding 
    computational overhead, latency bounds, and resource scheduling.
    
    Model optimization strategies such as quantization, low-rank adaptation, and structured pruning have emerged as 
    critical techniques to compress large parameter representations into edge-friendly execution units. Quantization 
    converts floating-point 32-bit parameters down to 8-bit or 4-bit integer values, dramatically reducing GPU memory 
    bandwidth demands while sacrificing less than one percent of model precision. Meanwhile, dynamic batching and local 
    inference caches assist in scaling request throughput across distributed inference pipelines.
    
    Furthermore, managing data context limits remains a primary bottleneck when dealing with high-throughput document 
    ingestion engines. Pre-trained seq2seq models like BART and T5 are structurally constrained by fixed positional 
    embedding registers, typically capped at 512 or 1024 tokens. When processing multi-page technical reports, systems 
    must employ token-aware sliding window algorithms or hierarchical Map-Reduce summarization passes. By preserving sentence 
    integrity and overlapping adjacent context blocks, processing pipelines eliminate edge boundary context loss while 
    maintaining linear execution scaling.
    """ * 4  # Duplicated to simulate longer document length

    summarizer = DocumentSummarizer(
        model_name="facebook/bart-large-cnn",
        max_chunk_tokens=600,
        overlap_tokens=80
    )

    result = summarizer.summarize_document(
        text=sample_technical_report,
        target_reduction=0.70
    )

    print("\n--- SUMMARIZATION RESULTS ---")
    print(f"Original Word Count: {result['original_word_count']}")
    print(f"Summary Word Count:  {result['summary_word_count']}")
    print(f"Total Condensation:  {result['reduction_percentage']}%\n")
    print("--- SUMMARY TEXT ---")
    print(result['summary'])
