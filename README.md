# Document Processing and Management System

A comprehensive system for processing, converting, and managing various types of documents including invoices, legal documents, and research papers. The system includes AI-powered tools for document analysis, financial data processing, and automated document generation.

## 🏗 Project Structure

```
repository/
├── src/                      # All source code
│   ├── core/                 # Core business logic 
│   │   ├── document/         # Document processing core functionality
│   │   ├── finance/          # Financial data processing
│   │   └── ai/               # AI integration components
│   ├── utils/                # Utility functions
│   │   ├── document/         # Document-specific utilities
│   │   ├── finance/          # Finance-specific utilities
│   │   └── ai/               # AI-specific utilities
│   ├── scripts/              # Standalone scripts and entry points
│   │   ├── document/         # Document processing scripts
│   │   ├── finance/          # Financial scripts
│   │   └── ai/               # AI scripts
│   └── config/               # Configuration and environment setup
├── data/                     # All data
│   ├── raw/                  # Raw, unprocessed data
│   │   ├── documents/        # Raw document files
│   │   ├── financial/        # Raw financial data
│   │   └── legal/            # Raw legal documents
│   ├── processed/            # Processed intermediate data
│   │   ├── documents/        # Processed document files
│   │   ├── financial/        # Processed financial data
│   │   └── legal/            # Processed legal documents
│   └── gold/                 # Final, ready-to-use datasets
├── docs/                     # Documentation
│   ├── api/                  # API documentation
│   ├── user/                 # User guides
│   ├── examples/             # Usage examples
│   └── research/             # Research papers and findings
├── tests/                    # Test suite
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   └── fixtures/             # Test fixtures
└── scripts/                  # Repository-level scripts
    ├── setup/                # Setup scripts
    └── maintenance/          # Maintenance scripts
```

## 🚀 Features

- **Document Processing**
  - Markdown to PDF conversion with professional formatting
  - Document structure analysis and validation
  - Automated document generation
  - PDF decryption for password-protected files

- **AI Integration**
  - Jina AI for semantic search
  - Perplexity integration for document analysis
  - Token counting and optimization
  - JSON to Markdown conversion for documentation

- **Financial Tools**
  - Invoice generation and management
  - Financial data extraction
  - Subsidy processing
  - Financial planning

- **Legal Document Management**
  - Contract processing
  - Legal document templates
  - Agreement generation

## 🔄 Repository Restructuring

The repository has recently undergone a major restructuring to improve organization, maintainability, and clarity. Key changes include:

- **Clear separation of concerns** between core functionality, utilities, and scripts
- **Improved data organization** with raw, processed, and gold datasets
- **Better documentation** organized by purpose
- **Centralized configuration** for easier management
- **Enhanced CLI** for common operations

See [REORGANIZATION.md](REORGANIZATION.md) for detailed information on the new structure and migration process.

## 🛠 Setup

1. **Run Setup Script**
   ```bash
   # Make the script executable if needed
   chmod +x scripts/setup/setup.sh
   
   # Run the script
   ./scripts/setup/setup.sh
   ```
   
   This script will:
   - Create a virtual environment
   - Install dependencies
   - Run the repository migration script
   - Create a template `.env` file

2. **Manual Setup (Alternative)**
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Unix/macOS
   # or
   .\venv\Scripts\activate  # On Windows
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Run migration script
   python scripts/setup/migrate_repository.py
   ```

3. **Environment Configuration**
   - Update the `.env` file with your API keys and configurations

## 💻 Usage

### Command Line Interface
```bash
# Show available commands
python src/cli.py --help

# Decrypt PDF files
python src/cli.py decrypt --input-dir data/raw/documents/pwd_protected_pdf --output-dir data/processed/documents/decrypted_pdf

# Clean documents
python src/cli.py clean --input-file data/raw/documents/Databricks_docs.json
```

### Document Conversion
```python
from src.core.document.md_pdf import convert_markdown_to_pdf
from pathlib import Path

# Convert markdown to PDF
convert_markdown_to_pdf(
    input_path=Path("docs/example.md"),
    output_path=Path("docs/example.pdf")
)
```

### AI Document Analysis
```python
from src.core.ai.jina import JinaReader
from src.config.settings import JINA_API_KEY

# Initialize Jina reader
reader = JinaReader()

# Scrape content from URL
content = reader.scrape_url("https://example.com")
```

### PDF Decryption
```python
from src.core.document.pdf_decryptor import PDFDecryptor
from pathlib import Path

# Initialize decryptor
decryptor = PDFDecryptor(
    password="your_password",
    output_dir=Path("data/processed/documents/decrypted_pdf")
)

# Decrypt a file
success, error = decryptor.decrypt_file(Path("data/raw/documents/encrypted.pdf"))
```

## 📚 Documentation

- [Repository Restructuring](docs/RESTRUCTURING.md) - Information about the repository structure
- [API Documentation](docs/api/README.md) - API reference
- [User Guide](docs/user/README.md) - User guides and tutorials
- [Examples](docs/examples/README.md) - Usage examples

## 🧪 Testing

Run the test suite:
```bash
# Run all tests
python -m pytest tests/

# Run only unit tests
python -m pytest tests/unit/

# Run a specific test
python -m pytest tests/test_pdf_decryptor.py
```

## 🛣️ Roadmap

1. **Comprehensive Documentation** - Complete API documentation and user guides
2. **CI/CD Pipeline** - Set up automated testing and deployment
3. **Code Quality Tools** - Add code quality checks and pre-commit hooks
4. **Extended CLI** - Add more commands to the CLI for common operations
5. **Web Interface** - Develop a web interface for document management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

See our [Contributing Guide](CONTRIBUTING.md) for more details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- WeasyPrint for PDF generation
- Jina AI for semantic search capabilities
- Perplexity for document analysis
- PyPDF2 for PDF manipulation 