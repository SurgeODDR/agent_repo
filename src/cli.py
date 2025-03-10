#!/usr/bin/env python3
"""
Command-line interface for the Document Processing and Management System.
"""

import argparse
import logging
import sys
from pathlib import Path

from src.config.settings import DEFAULT_LOG_LEVEL
from src.core.document.pdf_decryptor import PDFDecryptor
from src.utils.document.json_to_markdown import clean_databricks_docs

# Configure logging
logging.basicConfig(
    level=getattr(logging, DEFAULT_LOG_LEVEL),
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def decrypt_pdfs(args):
    """Handle PDF decryption command."""
    try:
        decryptor = PDFDecryptor(
            password=args.password,
            output_dir=Path(args.output_dir)
        )
        
        if args.file:
            # Decrypt a single file
            success, error = decryptor.decrypt_file(Path(args.file))
            if success:
                logger.info(f"Successfully decrypted {args.file}")
            else:
                logger.error(f"Failed to decrypt {args.file}: {error}")
        else:
            # Decrypt all files in directory
            results = decryptor.batch_decrypt(Path(args.input_dir))
            successful = sum(1 for _, success, _ in results if success)
            logger.info(f"Decryption complete. {successful}/{len(results)} files successfully decrypted")
    except Exception as e:
        logger.error(f"Error during PDF decryption: {str(e)}")
        sys.exit(1)

def clean_docs(args):
    """Handle document cleaning command."""
    try:
        input_file = Path(args.input_file) if args.input_file else None
        output_file = Path(args.output_file) if args.output_file else None
        
        count = clean_databricks_docs(
            input_file=input_file,
            output_file=output_file,
            include_metadata=args.include_metadata
        )
        logger.info(f"Successfully processed {count} documents")
    except Exception as e:
        logger.error(f"Error during document cleaning: {str(e)}")
        sys.exit(1)

def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description='Document Processing and Management System CLI'
    )
    parser.add_argument(
        '--log-level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default=DEFAULT_LOG_LEVEL,
        help='Set the logging level'
    )
    
    subparsers = parser.add_subparsers(
        dest='command',
        help='Command to execute'
    )
    
    # PDF decryption command
    decrypt_parser = subparsers.add_parser(
        'decrypt',
        help='Decrypt password-protected PDF files'
    )
    decrypt_parser.add_argument(
        '--file',
        help='Single PDF file to decrypt'
    )
    decrypt_parser.add_argument(
        '--input-dir',
        default='data/raw/pwd_protected_pdf',
        help='Directory containing PDF files to decrypt'
    )
    decrypt_parser.add_argument(
        '--output-dir',
        default='data/processed/decrypted_pdf',
        help='Directory to save decrypted PDF files'
    )
    decrypt_parser.add_argument(
        '--password',
        default='teamheretics',
        help='Password for the PDF files'
    )
    decrypt_parser.set_defaults(func=decrypt_pdfs)
    
    # Document cleaning command
    clean_parser = subparsers.add_parser(
        'clean',
        help='Clean and process document files'
    )
    clean_parser.add_argument(
        '--input-file',
        help='Input JSON file to clean'
    )
    clean_parser.add_argument(
        '--output-file',
        help='Output file to save cleaned data'
    )
    clean_parser.add_argument(
        '--include-metadata',
        action='store_true',
        help='Include metadata in cleaned output'
    )
    clean_parser.set_defaults(func=clean_docs)
    
    # Parse arguments
    args = parser.parse_args()
    
    # Set logging level
    logging.getLogger().setLevel(getattr(logging, args.log_level))
    
    # Execute command
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()