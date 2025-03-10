"""
This module provides functionality to decrypt password-protected PDF files.
It handles both single file and batch decryption operations while maintaining
the original files and providing detailed logging.

Key features:
- Single file and batch decryption
- Preserves original files
- Detailed logging
- Error handling
"""

import os
from pathlib import Path
import logging
from typing import List, Optional, Tuple
import PyPDF2
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PDFDecryptor:
    """
    A class to handle decryption of password-protected PDF files.
    """
    
    def __init__(self, password: str, output_dir: Path):
        """
        Initialize the PDFDecryptor with a password and output directory.
        
        Args:
            password: The password to decrypt the PDF files
            output_dir: Directory where decrypted files will be saved
        """
        self.password = password
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def decrypt_file(self, input_path: Path) -> Tuple[bool, Optional[str]]:
        """
        Decrypt a single PDF file.
        
        Args:
            input_path: Path to the encrypted PDF file
            
        Returns:
            Tuple of (success: bool, error_message: Optional[str])
        """
        try:
            input_path = Path(input_path)
            if not input_path.exists():
                return False, f"Input file not found: {input_path}"
            
            # Create output path
            output_path = self.output_dir / f"decrypted_{input_path.name}"
            
            logger.info(f"Attempting to decrypt: {input_path}")
            
            # Open and decrypt the PDF
            with open(input_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                
                if not pdf_reader.is_encrypted:
                    logger.warning(f"File is not encrypted: {input_path}")
                    return False, "File is not encrypted"
                
                # Try to decrypt with password
                if not pdf_reader.decrypt(self.password):
                    return False, "Invalid password"
                
                # Create a new PDF writer
                pdf_writer = PyPDF2.PdfWriter()
                
                # Add all pages to the writer
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)
                
                # Save the decrypted file
                with open(output_path, 'wb') as output_file:
                    pdf_writer.write(output_file)
                
                logger.info(f"Successfully decrypted: {output_path}")
                return True, None
                
        except Exception as e:
            error_msg = f"Error decrypting {input_path}: {str(e)}"
            logger.error(error_msg)
            return False, error_msg
            
    def batch_decrypt(self, input_dir: Path) -> List[Tuple[Path, bool, Optional[str]]]:
        """
        Decrypt all PDF files in the specified directory.
        
        Args:
            input_dir: Directory containing encrypted PDF files
            
        Returns:
            List of tuples containing (file_path, success, error_message)
        """
        input_dir = Path(input_dir)
        if not input_dir.exists():
            logger.error(f"Input directory not found: {input_dir}")
            return []
            
        results = []
        pdf_files = list(input_dir.glob("*.pdf"))
        
        if not pdf_files:
            logger.warning(f"No PDF files found in {input_dir}")
            return []
            
        logger.info(f"Found {len(pdf_files)} PDF files to process")
        
        for pdf_file in pdf_files:
            success, error = self.decrypt_file(pdf_file)
            results.append((pdf_file, success, error))
            
        # Log summary
        successful = sum(1 for _, success, _ in results if success)
        logger.info(f"Decryption complete. {successful}/{len(results)} files successfully decrypted")
        
        return results

def main():
    """
    Main function to demonstrate usage of the PDFDecryptor class.
    """
    # Example usage
    input_dir = Path("data/raw/pwd_protected_pdf")
    output_dir = Path("data/processed/decrypted_pdf")
    password = "teamheretics"
    
    decryptor = PDFDecryptor(password=password, output_dir=output_dir)
    results = decryptor.batch_decrypt(input_dir)
    
    # Print results
    for file_path, success, error in results:
        status = "Success" if success else f"Failed: {error}"
        print(f"{file_path}: {status}")

if __name__ == "__main__":
    main() 