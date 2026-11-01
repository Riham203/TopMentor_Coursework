import sys
from src.summarizer import DocumentSummarizer

def main():
    sample_text = """
    Artificial Intelligence (AI) and Machine Learning (ML) systems have transitioned from theoretical 
    laboratory research into core components of enterprise software ecosystems. Modern distributed 
    enterprise platforms depend heavily on predictive models to manage automated workload placement, 
    infrastructure scaling, and real-time threat analysis. However, deploying complex transformer-based 
    deep learning models at scale presents significant challenges regarding computational overhead, 
    latency bounds, and resource scheduling...
    """ * 3

    print("Initializing Summarization Engine...")
    engine = DocumentSummarizer(
        model_name="facebook/bart-large-cnn",
        max_chunk_tokens=600,
        overlap_tokens=80
    )

    print("Processing document...")
    result = engine.summarize_document(sample_text, target_reduction=0.70)

    print("\n" + "=" * 40)
    print("SUMMARIZATION COMPLETE")
    print("=" * 40)
    print(f"Original Word Count : {result['original_word_count']}")
    print(f"Summary Word Count  : {result['summary_word_count']}")
    print(f"Reduction Ratio     : {result['reduction_percentage']}%\n")
    print("Summary Output:")
    print(result['summary'])

if __name__ == "__main__":
    main()