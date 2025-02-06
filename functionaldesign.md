# Repository Restructuring Design Document

## 1. Project Overview
This repository appears to be a data processing and document conversion system with various tools for handling subsidies data, PDF processing, and document transformations.

## 2. Current Structure Analysis
The current repository has mixed concerns and could benefit from a more organized structure. Key components include:
- Document processing tools
- Data extraction utilities
- Configuration management
- Testing infrastructure
- Various data directories

## 3. Proposed Directory Structure

```
├── src/                      # Main source code directory
│   ├── core/                 # Core business logic
│   │   ├── agent.py         # Main agent implementation
│   │   └── validation.py    # Data validation logic
│   ├── tools/               # Tool implementations
│   │   ├── document/        # Document processing tools
│   │   │   ├── pdf.py      # PDF processing
│   │   │   └── markdown.py  # Markdown processing
│   │   ├── extractors/      # Data extraction tools
│   │   │   └── subsidy.py   # Subsidy data extraction
│   │   └── integrations/    # External service integrations
│   │       ├── jina.py      # Jina integration
│   │       └── perplexity.py# Perplexity integration
│   ├── utils/               # Utility functions
│   │   ├── logging.py       # Logging configuration
│   │   └── config.py        # Configuration management
│   └── cli/                 # Command-line interface
│       └── commands.py      # CLI commands
├── tests/                   # Test directory
│   ├── unit/               # Unit tests
│   ├── integration/        # Integration tests
│   └── fixtures/           # Test fixtures
├── data/                   # Data directory
│   ├── raw/                # Raw input data
│   ├── processed/          # Processed output data
│   └── gold/               # Gold standard data for validation
├── docs/                   # Documentation
│   ├── api/                # API documentation
│   ├── guides/             # User guides
│   └── examples/           # Usage examples
├── requirements/           # Requirements files
│   ├── base.txt           # Base requirements
│   ├── dev.txt            # Development requirements
│   └── test.txt           # Test requirements
└── scripts/               # Utility scripts
    └── setup.sh           # Setup scripts
```

## 4. Key Changes and Benefits

### 4.1 Source Code Organization
- Separate core business logic from tools and utilities
- Group related functionality (document processing, data extraction)
- Clear separation of concerns between different components

### 4.2 Testing Structure
- Separate unit and integration tests
- Dedicated fixtures directory
- Better organization for test resources

### 4.3 Documentation
- Centralized documentation in docs/
- API documentation separate from user guides
- Clear examples directory

### 4.4 Requirements Management
- Split requirements by purpose (base, dev, test)
- Better dependency management
- Easier environment setup

### 4.5 Data Management
- Clear separation of raw and processed data
- Dedicated gold data directory
- Better data versioning support

## 5. Migration Plan

1. Create new directory structure
2. Move files to their new locations
3. Update import statements
4. Update configuration paths
5. Verify all tests pass
6. Update documentation

## 6. Future Improvements

- Add CI/CD pipeline configuration
- Implement automated code quality checks
- Add contribution guidelines
- Setup pre-commit hooks
- Add API documentation generation

## 7. Maintenance Guidelines

1. Keep related code together
2. Follow consistent naming conventions
3. Maintain clear separation of concerns
4. Regular cleanup of unused code
5. Keep documentation up to date
6. Regular dependency updates

# PDF Decryption Functionality

## Overview
This functionality will decrypt password-protected PDF files located in the specified directory using a known password.

## Requirements
1. Decrypt all PDF files in `/data/raw/pwd_protected_pdf` directory
2. Use the password "teamheretics" for decryption
3. Save decrypted files in a new location to preserve originals
4. Handle errors gracefully and provide logging
5. Support batch processing of multiple files

## Technical Design

### Components

1. **PDF Decryptor Class**
   - Responsible for decrypting individual PDF files
   - Handles password validation and decryption
   - Uses PyPDF2 library for PDF operations

2. **Batch Processor**
   - Handles multiple files
   - Manages output directory creation
   - Provides progress tracking

### File Structure
```
src/
  document/
    core/
      pdf_decryptor.py    # Main decryption logic
tests/
  test_pdf_decryptor.py   # Unit tests
data/
  raw/
    pwd_protected_pdf/    # Input directory
  processed/
    decrypted_pdf/       # Output directory
```

### Error Handling
- File not found errors
- Invalid password errors
- Corrupted PDF errors
- Permission errors

### Logging
- Log all operations
- Track successful and failed decryptions
- Include timestamps and error details

## Future Improvements (TODOs)
1. Add support for different output formats
2. Implement parallel processing for large batches
3. Add progress bar for batch operations
4. Support different encryption methods
5. Add file integrity verification

## Dependencies
- PyPDF2>=3.0.0
- python-dotenv (for handling sensitive data like passwords)
- logging (built-in)
- pathlib (built-in)

## Security Considerations
1. Password should be stored securely (e.g., in environment variables)
2. Original files should not be modified
3. Implement proper file permissions for output files
4. Clear sensitive data from memory after use 