# Document Processing and Management System

A comprehensive system for processing, converting, and managing various types of documents including invoices, legal documents, and research papers. The system includes AI-powered tools for document analysis, financial data processing, and automated document generation.

## 🏗 Project Structure

```
repository/
├── src/                  # Source code
│   ├── ai/              # AI-related functionality
│   │   ├── core/        # Core AI components (Jina, Perplexity)
│   │   └── utils/       # AI utilities
│   ├── document/        # Document processing
│   │   ├── core/        # Core document handling
│   │   └── utils/       # Document utilities
│   ├── finance/         # Financial processing
│   │   ├── core/        # Core financial components
│   │   └── utils/       # Financial utilities
│   ├── legal/          # Legal document processing
│   │   ├── core/       # Core legal components
│   │   └── utils/      # Legal utilities
│   └── common/         # Shared functionality
├── data/               # Data storage
│   ├── documents/      # Document data
│   ├── financial/      # Financial data
│   └── legal/         # Legal data
└── docs/              # Documentation
    ├── api/           # API documentation
    ├── invoices/      # Invoice documents
    ├── legal/         # Legal documents
    └── research/      # Research papers
```

## 🚀 Features

- **Document Processing**
  - Markdown to PDF conversion with professional formatting
  - Document structure analysis and validation
  - Automated document generation

- **AI Integration**
  - Jina AI for semantic search
  - Perplexity integration for document analysis
  - Token counting and optimization

- **Financial Tools**
  - Invoice generation and management
  - Financial data extraction
  - Subsidy processing

- **Legal Document Management**
  - Contract processing
  - Legal document templates
  - Agreement generation

## 🛠 Setup

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Unix/macOS
   # or
   .\venv\Scripts\activate  # On Windows
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   - Copy `.env.example` to `.env`
   - Add required API keys and configurations

## 💻 Usage

### Document Conversion
```python
from src.document.core.markdown import convert_markdown_to_pdf

# Convert markdown to PDF
convert_markdown_to_pdf(
    input_path="docs/example.md",
    output_path="docs/example.pdf"
)
```

### AI Document Analysis
```python
from src.ai.core.jina import JinaClient

# Initialize Jina client
client = JinaClient()

# Search documents
results = client.search("your query here")
```

### Invoice Generation
```python
from src.document.core.markdown import convert_markdown_to_pdf

# Generate invoice
convert_markdown_to_pdf(
    input_path="docs/invoices/template.md",
    output_path="docs/invoices/invoice.pdf"
)
```

## 📚 Documentation

- [API Documentation](docs/api/README.md)
- [User Guide](docs/user_guide/README.md)
- [Development Guide](docs/guides/development.md)

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- WeasyPrint for PDF generation
- Jina AI for semantic search capabilities
- Perplexity for document analysis 