#!/usr/bin/env python3
"""
Script to clean Databricks documentation JSON files.
Extracts markdown content and optionally other metadata.
"""

import argparse
import logging
from pathlib import Path

from src.utils.document.json_to_markdown import clean_databricks_docs, convert_databricks_docs_to_md

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    """Process Databricks documentation files."""
    parser = argparse.ArgumentParser(description='Clean and convert Databricks documentation')
    parser.add_argument('--input-file', type=str, 
                        help='Path to the input JSON file (defaults to standard location)')
    parser.add_argument('--output-file', type=str,
                        help='Path to save the cleaned JSON file (defaults to standard location)')
    parser.add_argument('--include-metadata', action='store_true',
                        help='Include metadata in the cleaned output')
    parser.add_argument('--convert-to-md', action='store_true',
                        help='Convert the cleaned JSON to markdown')
    parser.add_argument('--md-output', type=str,
                        help='Path to save the markdown output (if --convert-to-md is specified)')
    
    args = parser.parse_args()
    
    # Set paths based on arguments
    input_file = Path(args.input_file) if args.input_file else None
    output_file = Path(args.output_file) if args.output_file else None
    md_output = Path(args.md_output) if args.md_output else None
    
    # Clean the JSON
    count = clean_databricks_docs(
        input_file=input_file,
        output_file=output_file,
        include_metadata=args.include_metadata
    )
    logger.info(f"Successfully processed {count} documents")
    
    # Convert to markdown if requested
    if args.convert_to_md:
        if output_file is None:
            output_file = Path('data/documents/cleaned/Databricks_docs_cleaned.json')
            
        convert_databricks_docs_to_md(
            input_file=output_file,
            output_file=md_output
        )
        logger.info(f"Successfully converted to markdown")

if __name__ == '__main__':
    main()