#!/usr/bin/env python3

"""
This script converts processed Crew AI JSON documentation files to markdown format,
adding dividers between pages and proper formatting.
"""

import json
import os
import re
from pathlib import Path
import logging
from typing import Dict, List, Any

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def clean_markdown_content(content: str) -> str:
    """
    Clean up markdown content by removing navigation elements and unnecessary sections.
    
    Args:
        content: Original markdown content
        
    Returns:
        Cleaned markdown content
    """
    # Remove navigation header
    content = re.sub(r'\[CrewAI home page.*?\n\nNavigation.*?\n\n', '', content, flags=re.DOTALL)
    
    # Remove "Was this page helpful?" sections
    content = re.sub(r'Was this page helpful\?\s*\n\s*YesNo\s*\n', '', content)
    
    # Remove navigation links at bottom
    content = re.sub(r'\[(Previous|Next|Introduction|Quickstart|Tasks|Examples|Flows)]\([^)]+\)\s*', '', content)
    
    # Remove "On this page" sections
    content = re.sub(r'On this page\s*\n\n-.*?(?=\n\n|$)', '', content, flags=re.DOTALL)
    
    # Remove empty lines with only whitespace
    content = re.sub(r'\n\s*\n', '\n\n', content)
    
    return content.strip()

def convert_doc_to_markdown(doc: Dict[str, Any]) -> str:
    """
    Convert a single document to markdown format.
    
    Args:
        doc: Dictionary containing the document data
        
    Returns:
        Formatted markdown string
    """
    # Clean up the markdown content
    cleaned_markdown = clean_markdown_content(doc['markdown'])
    
    markdown = f"# {doc['source_url']}\n\n"
    markdown += f"## Description\n{doc['description']}\n\n"
    markdown += f"## Content\n{cleaned_markdown}"
    return markdown

def process_file(input_path: Path, output_path: Path) -> None:
    """
    Process a JSON file and convert it to markdown.
    
    Args:
        input_path: Path to the input JSON file
        output_path: Path where the markdown file will be saved
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Convert each document to markdown with dividers
        markdown_sections = [convert_doc_to_markdown(doc) for doc in data]
        markdown_content = "\n\n" + "\n\n---\n\n".join(markdown_sections)
        
        # Create output directory if it doesn't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save markdown content
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
            
        logger.info(f"Successfully converted {input_path} -> {output_path}")
        
    except Exception as e:
        logger.error(f"Error processing {input_path}: {str(e)}")
        raise

def main():
    """
    Main function to process all JSON files and convert them to markdown.
    """
    # Get the workspace root directory (where the script is located)
    workspace_root = Path(__file__).parent.parent
    
    # Define input and output directories
    input_dir = workspace_root / "processed_crew_ai_docs"
    output_dir = workspace_root / "markdown_docs"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Process all processed JSON files
    for input_file in input_dir.glob("processed_Crew_AI_docs_*.json"):
        output_file = output_dir / f"{input_file.stem}.md"
        process_file(input_file, output_file)
        
    logger.info("Conversion complete!")

if __name__ == "__main__":
    main() 