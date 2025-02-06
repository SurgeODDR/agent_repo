#!/usr/bin/env python3

"""
This script processes Crew AI JSON documentation files to create a simplified version
containing only the source URL, description, and markdown fields.

The script will:
1. Read JSON files with Crew AI documentation
2. Extract only the required fields (source URL, description, markdown)
3. Save the processed data to new JSON files
"""

import json
import os
from pathlib import Path
import logging
from typing import Dict, List, Any

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def process_crew_ai_doc(doc: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process a single Crew AI document to keep only required fields.
    
    Args:
        doc: Dictionary containing the original document data
        
    Returns:
        Dictionary containing only the source URL, description, and markdown
    """
    return {
        "source_url": doc.get("metadata", {}).get("sourceURL", ""),
        "description": doc.get("metadata", {}).get("description", ""),
        "markdown": doc.get("markdown", "")
    }

def process_file(input_path: Path, output_path: Path) -> None:
    """
    Process a single JSON file containing Crew AI documentation.
    
    Args:
        input_path: Path to the input JSON file
        output_path: Path where the processed JSON file will be saved
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Process each document in the file
        processed_data = [process_crew_ai_doc(doc) for doc in data]
        
        # Create output directory if it doesn't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save processed data
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, indent=2, ensure_ascii=False)
            
        logger.info(f"Successfully processed {input_path} -> {output_path}")
        
    except Exception as e:
        logger.error(f"Error processing {input_path}: {str(e)}")
        raise

def main():
    """
    Main function to process all Crew AI JSON files in the root directory.
    """
    # Get the workspace root directory (where the script is located)
    workspace_root = Path(__file__).parent.parent
    
    # Define output directory
    output_dir = workspace_root / "processed_crew_ai_docs"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Process all Crew AI JSON files
    for input_file in workspace_root.glob("Crew_AI_docs_*.json"):
        output_file = output_dir / f"processed_{input_file.name}"
        process_file(input_file, output_file)
        
    logger.info("Processing complete!")

if __name__ == "__main__":
    main() 