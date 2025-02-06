"""
Test cases for the PDF decryptor functionality.
"""

import pytest
from pathlib import Path
import PyPDF2
from src.document.core.pdf_decryptor import PDFDecryptor

@pytest.fixture
def temp_dir(tmp_path):
    """Create temporary directories for testing."""
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()
    output_dir.mkdir()
    return input_dir, output_dir

def test_decryptor_initialization(temp_dir):
    """Test PDFDecryptor initialization."""
    _, output_dir = temp_dir
    decryptor = PDFDecryptor(password="test", output_dir=output_dir)
    assert decryptor.password == "test"
    assert decryptor.output_dir == output_dir
    assert output_dir.exists()

def test_decrypt_nonexistent_file(temp_dir):
    """Test decryption of non-existent file."""
    _, output_dir = temp_dir
    decryptor = PDFDecryptor(password="test", output_dir=output_dir)
    success, error = decryptor.decrypt_file(Path("nonexistent.pdf"))
    assert not success
    assert "not found" in error

def test_batch_decrypt_empty_directory(temp_dir):
    """Test batch decryption with empty directory."""
    input_dir, output_dir = temp_dir
    decryptor = PDFDecryptor(password="test", output_dir=output_dir)
    results = decryptor.batch_decrypt(input_dir)
    assert len(results) == 0

def test_batch_decrypt_nonexistent_directory(temp_dir):
    """Test batch decryption with non-existent directory."""
    _, output_dir = temp_dir
    decryptor = PDFDecryptor(password="test", output_dir=output_dir)
    results = decryptor.batch_decrypt(Path("nonexistent"))
    assert len(results) == 0

# TODO: Add more test cases for actual PDF decryption once we have test files
# These would include:
# - test_decrypt_encrypted_pdf_valid_password
# - test_decrypt_encrypted_pdf_invalid_password
# - test_decrypt_unencrypted_pdf
# - test_batch_decrypt_mixed_files 