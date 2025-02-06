import json
import os
import re
from pathlib import Path
from typing import List, Dict

def load_json_file(file_path: str) -> List[Dict]:
    """Load and parse a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def clean_markdown(markdown: str) -> str:
    """Remove cookie-related content from markdown."""
    # Find the position of the main content link
    main_content_pos = markdown.find("[Overslaan en naar de inhoud gaan](#main-content)")
    if main_content_pos != -1:
        # Get everything after the main content link
        cleaned_text = markdown[main_content_pos + len("[Overslaan en naar de inhoud gaan](#main-content)"):]
        # Remove any leading/trailing whitespace
        cleaned_text = cleaned_text.strip()
        return cleaned_text
    return markdown

def filter_and_reduce_vlaio_documents(documents: List[Dict]) -> List[Dict]:
    """Filter documents and reduce schema to only include markdown and specific metadata fields."""
    filtered_docs = []
    for doc in documents:
        source_url = doc.get("metadata", {}).get("sourceURL", "")
        # Only include documents that:
        # 1. Are from the subsidiedatabank
        # 2. Don't contain 'wijzigingen' in the URL
        if ("vlaio.be/nl/subsidies-financiering/subsidiedatabank/" in source_url and 
            "wijzigingen" not in source_url):
            # Clean the markdown content
            cleaned_markdown = clean_markdown(doc["markdown"])
            if cleaned_markdown:  # Only add if there's content after cleaning
                filtered_docs.append({
                    "markdown": cleaned_markdown,
                    "metadata": {
                        "sourceURL": source_url,
                        "title": doc["metadata"]["title"]
                    }
                })
    return filtered_docs

def main():
    # Set up paths
    base_dir = Path(__file__).parent.parent
    json_dir = base_dir / "subsidies" / "json_data"
    output_file = base_dir / "subsidies" / "vlaio_subsidies_cleaned_no_changes.json"
    
    # Initialize list to store all filtered documents
    all_filtered_documents = []
    
    # Process each JSON file in the directory
    for json_file in json_dir.glob("*.json"):
        print(f"Processing {json_file.name}...")
        try:
            # Load and filter documents from the current file
            documents = load_json_file(str(json_file))
            filtered_docs = filter_and_reduce_vlaio_documents(documents)
            all_filtered_documents.extend(filtered_docs)
            print(f"Found {len(filtered_docs)} matching documents in {json_file.name}")
        except Exception as e:
            print(f"Error processing {json_file.name}: {str(e)}")
    
    # Save filtered results
    print(f"\nTotal matching documents found: {len(all_filtered_documents)}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_filtered_documents, f, ensure_ascii=False, indent=2)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main() 