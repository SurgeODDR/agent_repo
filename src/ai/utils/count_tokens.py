import json
import tiktoken
from pathlib import Path

def count_tokens(text: str, model: str = "gpt-4") -> int:
    """Count the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def main():
    # Set up paths
    base_dir = Path(__file__).parent.parent
    input_file = base_dir / "subsidies" / "vlaio_subsidies_cleaned_no_changes.json"
    
    # Load the JSON data
    with open(input_file, 'r', encoding='utf-8') as f:
        documents = json.load(f)
    
    # Initialize counters
    total_tokens = 0
    markdown_tokens = 0
    metadata_tokens = 0
    
    # Process each document
    for i, doc in enumerate(documents, 1):
        # Count tokens in markdown
        doc_markdown_tokens = count_tokens(doc["markdown"])
        markdown_tokens += doc_markdown_tokens
        
        # Count tokens in metadata
        metadata_str = json.dumps(doc["metadata"], ensure_ascii=False)
        doc_metadata_tokens = count_tokens(metadata_str)
        metadata_tokens += doc_metadata_tokens
        
        # Update total
        doc_total = doc_markdown_tokens + doc_metadata_tokens
        total_tokens += doc_total
        
        # Print progress every 50 documents
        if i % 50 == 0:
            print(f"Processed {i} documents...")
    
    # Print results
    print("\nToken count summary:")
    print(f"Total documents: {len(documents)}")
    print(f"Markdown tokens: {markdown_tokens:,}")
    print(f"Metadata tokens: {metadata_tokens:,}")
    print(f"Total tokens: {total_tokens:,}")
    print(f"\nAverage tokens per document: {total_tokens / len(documents):,.1f}")

if __name__ == "__main__":
    main() 