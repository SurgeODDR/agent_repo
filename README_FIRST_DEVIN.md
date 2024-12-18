# AI Research Agent - Comprehensive Guide

## Overview

This AI Research Agent is designed to perform comprehensive research and analysis using multiple tools:
- Jina Reader for web scraping
- Perplexity API for research queries
- Claude's native PDF support for document analysis

This guide focuses on the PDF processing capabilities, which use Claude's advanced PDF support for optimal results.

## PDF Processing Capabilities

### Native PDF Support
The agent uses Claude's native PDF support, which means:
1. PDFs are processed in their original form without pre-conversion
2. Both text and visual elements (charts, diagrams) are analyzed
3. Claude can understand and reference the document's layout and structure

### Key Features

1. **Single PDF Analysis**
```python
from src.agent import ResearchAgent

agent = ResearchAgent()
result = agent.research_topic(
    query="Analyze the financial performance for Q4 2023",
    pdfs=["path/to/quarterly_report.pdf"]
)
```

2. **Batch Processing**
```python
from src.tools.pdf_processor import PDFProcessor

processor = PDFProcessor()
results = processor.batch_process_pdfs(
    pdf_paths=[
        "path/to/report1.pdf",
        "path/to/report2.pdf"
    ],
    analysis_prompt="Extract key financial metrics"
)
```

3. **Cached Processing**
```python
result = agent.pdf_processor.analyze_pdf_content(
    pdf_path="path/to/doc.pdf",
    analysis_prompt="Summarize the main points",
    use_cache=True
)
```

## Best Practices

### 1. PDF Preparation
- Use standard fonts
- Ensure text is clear and legible
- Rotate pages to proper orientation
- Keep files under 32MB
- Limit to 100 pages per request

### 2. Cost Optimization
- Each page uses approximately 1,500-3,000 tokens
- Visual elements count as image tokens
- Use caching for repeated analysis
- Split large PDFs into chunks

### 3. Performance Optimization
- Place PDFs before text in requests
- Use batch processing for multiple files
- Enable caching for repeated queries
- Use logical page numbers in prompts

## Example Use Cases

### 1. Financial Analysis
```python
agent = ResearchAgent()
results = agent.investigate_entity(
    entity_name="Company XYZ",
    context="financial performance and market position",
    pdfs=[
        "annual_report_2023.pdf",
        "investor_presentation.pdf"
    ]
)
```

### 2. Research Paper Analysis
```python
results = agent.research_topic(
    query="What are the key findings and methodologies?",
    pdfs=["research_paper.pdf"],
    max_results=3
)
```

### 3. Batch Document Processing
```python
processor = PDFProcessor()
results = processor.batch_process_pdfs(
    pdf_paths=["doc1.pdf", "doc2.pdf", "doc3.pdf"],
    analysis_prompt="Extract and compare the main arguments"
)
```

## Error Handling

The agent includes robust error handling:
- PDF encoding errors
- API rate limits
- File size limits
- Invalid file formats

Error messages are logged and can be accessed through the return values.

## Token Usage and Costs

1. **Text Token Costs**
   - 1,500-3,000 tokens per page
   - Varies with content density
   - Standard API pricing applies

2. **Image Token Costs**
   - Each page counts as an image
   - Visual elements increase token usage
   - Consider when processing image-heavy PDFs

## Advanced Features

### 1. Custom Analysis
```python
# Detailed analysis with custom parameters
result = agent.pdf_processor.analyze_pdf_content(
    pdf_path="document.pdf",
    analysis_prompt="Perform a detailed SWOT analysis",
    max_tokens=8192,
    use_cache=True
)
```

### 2. Parallel Processing
```python
# Process multiple PDFs in parallel
results = agent.research_topic(
    query="Compare quarterly performance",
    pdfs=["Q1.pdf", "Q2.pdf", "Q3.pdf", "Q4.pdf"],
    max_results=10
)
```

## Troubleshooting

Common issues and solutions:
1. **File Too Large**
   - Split into smaller chunks
   - Use batch processing

2. **Rate Limits**
   - Implement exponential backoff
   - Use caching

3. **Memory Issues**
   - Process files sequentially
   - Reduce max_tokens

4. **Poor Analysis Quality**
   - Improve PDF quality
   - Make prompts more specific
   - Use proper page orientation

## Updates and Maintenance

The agent is regularly updated to use the latest Claude model versions and features. Check the documentation for:
- New model capabilities
- API changes
- Performance improvements
- Best practices updates 