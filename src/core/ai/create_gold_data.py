import json
import tiktoken
from pathlib import Path
from typing import List, Dict

def count_tokens(text: str, model: str = "gpt-4") -> int:
    """Count the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def create_chunk(documents: List[Dict], max_tokens: int = 150_000) -> tuple[List[Dict], List[Dict], int]:
    """Create a chunk of documents that fits within the token limit."""
    chunk = []
    remaining = documents.copy()
    current_tokens = 0
    
    while remaining and current_tokens < max_tokens:
        doc = remaining[0]
        # Count tokens in the document
        doc_tokens = count_tokens(doc["markdown"])
        doc_tokens += count_tokens(json.dumps(doc["metadata"], ensure_ascii=False))
        
        # If adding this document would exceed the limit, stop
        if current_tokens + doc_tokens > max_tokens:
            break
            
        # Add document to chunk and update counters
        chunk.append(remaining.pop(0))
        current_tokens += doc_tokens
    
    return chunk, remaining, current_tokens

def main():
    # Set up paths
    base_dir = Path(__file__).parent.parent
    input_file = base_dir / "subsidies" / "vlaio_subsidies_cleaned_no_changes.json"
    output_dir = base_dir / "gold_data"
    output_dir.mkdir(exist_ok=True)
    
    # Load the JSON data
    print("Loading input file...")
    with open(input_file, 'r', encoding='utf-8') as f:
        documents = json.load(f)
    
    # Create chunks
    remaining_docs = documents.copy()
    chunk_num = 1
    
    while remaining_docs:
        print(f"\nProcessing chunk {chunk_num}...")
        chunk, remaining_docs, token_count = create_chunk(remaining_docs)
        
        # Save chunk to file
        output_file = output_dir / f"vlaio_subsidies_part_{chunk_num}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(chunk, f, ensure_ascii=False, indent=2)
        
        print(f"Chunk {chunk_num}:")
        print(f"- Documents: {len(chunk)}")
        print(f"- Tokens: {token_count:,}")
        print(f"- Saved to: {output_file.name}")
        
        chunk_num += 1
    
    print(f"\nTotal chunks created: {chunk_num - 1}")

if __name__ == "__main__":
    main() 