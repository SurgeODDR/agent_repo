#!/usr/bin/env python3
"""
Script to convert various JSON documentation formats to Markdown.
Supports multiple document types and cleaning options.
"""

import argparse
import logging
from pathlib import Path

from src.utils.document.json_to_markdown import convert_json_to_md

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    """Main function for converting JSON to markdown."""
    parser = argparse.ArgumentParser(description='Convert JSON documentation to markdown format')
    parser.add_argument('input_file', type=str, help='Path to the input JSON file')
    parser.add_argument('--output-file', '-o', type=str, help='Path to save the output markdown file')
    parser.add_argument('--doc-type', '-t', type=str, default='general',
                      choices=['general', 'crew_ai', 'databricks'],
                      help='Type of documentation in the JSON file')
    parser.add_argument('--include-metadata', '-m', action='store_true',
                      help='Include metadata like source URLs and descriptions')
    parser.add_argument('--disable-aggressive-clean', '-c', action='store_true',
                      help='Disable aggressive cleaning of metadata')
    
    args = parser.parse_args()
    
    try:
        # Convert the file
        convert_json_to_md(
            json_file_path=args.input_file,
            output_file_path=args.output_file,
            doc_type=args.doc_type,
            aggressive_clean=not args.disable_aggressive_clean,
            include_metadata=args.include_metadata
        )
        
        # Determine output path for logging
        output_path = args.output_file if args.output_file else f"{args.input_file}.md"
        logger.info(f"Successfully converted {args.input_file} to {output_path}")
        
    except Exception as e:
        logger.error(f"Error converting file: {str(e)}")
        raise

if __name__ == '__main__':
    main()