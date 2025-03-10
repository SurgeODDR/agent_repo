#!/usr/bin/env python3

"""
Unified module for converting JSON documentation to markdown format with various cleaning options.
Supports multiple JSON formats including Crew AI docs, Databricks docs, and general documentation files.
"""

import json
import os
import re
from pathlib import Path
import logging
from typing import Dict, List, Any, Optional, Callable, Union

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MarkdownCleaner:
    """Class to handle markdown cleaning and formatting operations."""
    
    def __init__(self, aggressive_clean: bool = True):
        """
        Initialize the markdown cleaner.
        
        Args:
            aggressive_clean (bool): If True, removes more metadata and redundant content
        """
        self.aggressive_clean = aggressive_clean
    
    def clean_code_blocks(self, content: str) -> str:
        """Clean and format code blocks."""
        # Remove empty code blocks and artifacts
        content = re.sub(r'\`\`\`\s*\n\s*\`\`\`', '', content)
        content = re.sub(r'\`\`\`.*?<br>.*?<br>\`\`\`', '', content, flags=re.DOTALL)
        
        # Fix code block language specification
        def fix_code_block(match):
            code = match.group(1).strip()
            if not code:
                return ''
            
            # If there's no language specified, check first line for common extensions
            first_line = code.split('\n')[0].strip()
            if not first_line.startswith(('python', 'json', 'bash', 'typescript')):
                if '.py' in first_line:
                    return f'```python\n{code}\n```'
                elif '.json' in first_line:
                    return f'```json\n{code}\n```'
                elif '.ts' in first_line:
                    return f'```typescript\n{code}\n```'
                else:
                    return f'```\n{code}\n```'
            return f'```{code}\n```'
            
        content = re.sub(r'\`\`\`(.*?)\`\`\`', fix_code_block, content, flags=re.DOTALL)
        
        # Remove single-line code blocks that are just type hints
        content = re.sub(r'\`\`\`\n[^`\n]*?:\s*[^`\n]*?\n\`\`\`', '', content)
        
        return content
    
    def clean_headers(self, content: str) -> str:
        """Clean and format headers."""
        # Remove backticks and type annotations from headers
        content = re.sub(r'(#+)\s*([^`\n]+)`([^`\n]+)`(\s*`[^`\n]+`)*', r'\1 \2\3', content)
        content = re.sub(r'(###?\s*\w+)`([^`]+)`', r'\1 \2', content)
        content = re.sub(r'(####?\s*[^`\n]+)`([^`\n]+)`', r'\1 \2', content)
        
        # Clean up header suffixes
        content = re.sub(r'(#+ [^\n]+)(module-attribute|instance-attribute|property|dataclass|abstractmethod|async)', r'\1', content)
        
        # Ensure proper header spacing
        content = re.sub(r'\n(#+)', r'\n\n\1', content)
        content = re.sub(r'(#+.*?)\n(?!\n)', r'\1\n\n', content)
        
        # Remove redundant header markers
        content = re.sub(r'`module-attribute`|`instance-attribute`|`property`|`dataclass`|`abstractmethod`|`async`', '', content)
        
        return content
    
    def clean_links_and_references(self, content: str) -> str:
        """Clean and format links and references."""
        # Remove navigation links
        content = re.sub(r'\[Skip to content\].*?\n', '', content)
        
        # Clean up reference links
        content = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', lambda m: f'[{m.group(1).strip()}]({m.group(2).strip()})', content)
        
        # Remove version notices and other metadata
        content = re.sub(r'Version Notice.*?(?=\n#|\Z)', '', content, flags=re.DOTALL)
        
        return content
    
    def clean_lists_and_spacing(self, content: str) -> str:
        """Clean and format lists and spacing."""
        # Fix list formatting
        content = re.sub(r'\n\s*[-\*]\s', '\n* ', content)  # Standardize list markers
        
        # Fix nested list indentation
        lines = content.split('\n')
        fixed_lines = []
        in_list = False
        
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('*'):
                in_list = True
                indent = len(line) - len(line.lstrip())
                fixed_lines.append('  ' * (indent // 2) + '* ' + stripped[2:])
            else:
                if in_list and stripped:
                    # Add extra newline when leaving a list
                    fixed_lines.append('')
                    in_list = False
                fixed_lines.append(line)
        
        content = '\n'.join(fixed_lines)
        
        # Normalize spacing
        content = re.sub(r'\n{3,}', '\n\n', content)
        content = re.sub(r'(?<=\n\n)[ \t]+(?=\S)', '', content)
        content = re.sub(r'\n\s*\|\s*\|\s*\n', '\n\n', content)  # Remove empty table rows
        
        return content
    
    def clean_metadata(self, content: str) -> str:
        """Clean metadata and redundant content."""
        if self.aggressive_clean:
            # Remove various metadata sections
            patterns = [
                r'Source code in.*?\n',
                r'Bases:.*?\n',
                r'Returns:.*?(?=\n\n|\Z)',
                r'Parameters:.*?(?=\n\n|\Z)',
                r'\| Name \| Type \| Description \| Default \|.*?(?=\n\n|\Z)',
                r'@.*?(?=\n#|\n\n|\Z)',
                r'Example:\s*\n\s*\w+\.py\s*\n',
                r'\[pip\].*?\[uv\].*?\n',  # Remove tabbed navigation
                r'\(or.*?\.\.\..*?\)\n',   # Remove version notes
            ]
            for pattern in patterns:
                content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        # Remove HTML tables and remaining artifacts
        content = re.sub(r'\|.*?\|.*?\|.*?\n', '', content)
        content = re.sub(r'\n\s*\|.*?\|.*?\n', '\n', content)
        
        return content
    
    def clean_content(self, content: str) -> str:
        """
        Main method to clean and format markdown content.
        
        Args:
            content (str): Raw markdown content
        Returns:
            str: Cleaned and formatted markdown content
        """
        content = self.clean_links_and_references(content)
        content = self.clean_code_blocks(content)
        content = self.clean_headers(content)
        content = self.clean_metadata(content)
        content = self.clean_lists_and_spacing(content)
        
        # Final cleanup
        content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
        return content.strip()

def clean_crew_ai_content(content: str) -> str:
    """
    Clean up Crew AI markdown content by removing navigation elements and unnecessary sections.
    
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

def clean_databricks_content(content: str) -> str:
    """Clean and organize Databricks markdown content."""
    # Remove repeated empty lines
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    # Process each line
    lines = content.split('\n')
    processed_lines = []
    in_api_section = False
    
    for i, line in enumerate(lines):
        # Skip navigation elements and empty lines
        if any(x in line.lower() for x in ['documentation', 'support', 'feedback', 'ctrl + p']):
            continue
        if line.strip() in ['AWSGCPAzure', 'WorkspaceAccount']:
            continue
        if not line.strip():
            continue
            
        # Check if we're entering an API section
        if '`' in line and '/api/' in line:
            in_api_section = True
            continue
            
        # Extract text from links if present, otherwise keep the line as is
        link_matches = re.findall(r'\[([^\]]+)\]\([^)]+\)', line)
        if link_matches:
            # Only keep the link text if it's meaningful (not just a reference)
            meaningful_texts = [text for text in link_matches 
                             if not any(x in text.lower() for x in ['documentation', 'support', 'feedback'])]
            if meaningful_texts:
                for text in meaningful_texts:
                    if text.strip() and len(text.split()) > 1:  # Only add non-trivial content
                        processed_lines.append(text)
        else:
            # Skip lines that are just single words or very short phrases unless they're headings
            if line.startswith('#') or len(line.split()) > 2:
                # Convert any line that looks like a heading but doesn't have # to proper heading
                if re.match(r'^[A-Z][^a-z\n]{2,}$', line.strip()):
                    processed_lines.append(f"## {line}")
                else:
                    processed_lines.append(line)
    
    # Clean up the processed content
    content = '\n'.join(processed_lines).strip()
    # Remove any remaining markdown link references
    content = re.sub(r'^\[[^\]]+\]:\s*http.*$', '', content, flags=re.MULTILINE)
    # Remove consecutive empty lines
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    return content

def convert_json_to_md(
    json_file_path: str,
    output_file_path: Optional[str] = None,
    doc_type: str = "general",
    aggressive_clean: bool = True,
    include_metadata: bool = False
) -> None:
    """
    Convert a JSON file containing documentation to markdown format.
    
    Args:
        json_file_path (str): Path to the input JSON file
        output_file_path (str, optional): Path to save the output markdown file
        doc_type (str): Type of documentation ("general", "crew_ai", "databricks")
        aggressive_clean (bool): Whether to perform aggressive cleaning of metadata
        include_metadata (bool): Whether to include metadata in the output (source, description, etc.)
    """
    try:
        # Validate input file
        if not os.path.exists(json_file_path):
            raise FileNotFoundError(f"Input file not found: {json_file_path}")
        
        # Set output path
        if output_file_path is None:
            output_file_path = os.path.splitext(json_file_path)[0] + '.md'
        
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_file_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        
        # Read and process JSON
        with open(json_file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON file: {str(e)}")
        
        # Select cleaner function based on doc_type
        cleaner = MarkdownCleaner(aggressive_clean=aggressive_clean)
        
        # Process based on document type
        if doc_type == "crew_ai":
            convert_crew_ai_to_md(data, output_file_path, include_metadata)
        elif doc_type == "databricks":
            convert_databricks_to_md(data, output_file_path, include_metadata)
        else:
            # Generic document processing
            markdown_content = []
            for doc in data:
                if isinstance(doc, dict) and 'markdown' in doc:
                    cleaned_content = cleaner.clean_content(doc['markdown'])
                    if cleaned_content.strip():
                        markdown_content.append(cleaned_content)
                        markdown_content.append('\n---\n')
            
            # Ensure we have content
            if not markdown_content:
                raise ValueError("No valid markdown content found in JSON file")
            
            # Write output
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(markdown_content))
        
        logger.info(f"Conversion complete! Markdown file saved to: {output_file_path}")
        
    except Exception as e:
        logger.error(f"Error during conversion: {str(e)}")
        raise

def convert_crew_ai_to_md(data: List[Dict[str, Any]], output_path: str, include_metadata: bool) -> None:
    """
    Convert Crew AI documentation to markdown format.
    
    Args:
        data: List of document dictionaries
        output_path: Path where the markdown file will be saved
        include_metadata: Whether to include source and description metadata
    """
    markdown_sections = []
    
    for doc in data:
        if 'markdown' not in doc or not doc['markdown'].strip():
            continue
        
        # Clean up the markdown content
        cleaned_markdown = clean_crew_ai_content(doc['markdown'])
        
        section = []
        if include_metadata and 'source_url' in doc:
            section.append(f"# {doc['source_url']}")
        
        if include_metadata and 'description' in doc and doc['description'].strip():
            section.append(f"## Description\n{doc['description']}")
        
        section.append(f"{cleaned_markdown}")
        markdown_sections.append("\n\n".join(section))
    
    if not markdown_sections:
        raise ValueError("No valid markdown content found in Crew AI data")
    
    markdown_content = "\n\n---\n\n".join(markdown_sections)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

def convert_databricks_to_md(data: List[Dict[str, Any]], output_path: str, include_metadata: bool) -> None:
    """
    Convert Databricks documentation to markdown format.
    
    Args:
        data: List of document dictionaries
        output_path: Path where the markdown file will be saved
        include_metadata: Whether to include API endpoint information
    """
    # Process and deduplicate content
    unique_contents = set()
    api_docs = []
    general_docs = []
    
    for entry in data:
        if 'markdown' not in entry or not entry['markdown'].strip():
            continue
            
        content = clean_databricks_content(entry['markdown'])
        if not content:
            continue
        
        content_hash = hash(content.strip())
        if content_hash in unique_contents:
            continue
        
        unique_contents.add(content_hash)
        
        # Check if it's an API endpoint documentation
        if include_metadata:
            api_heading, api_description = extract_api_info(entry['markdown'])
            if api_heading:
                if api_description:
                    api_docs.append((api_heading, api_description))
                continue
                
        # Only add to general docs if it contains meaningful content
        if len(content.split()) > 3:  # Skip very short content
            general_docs.append(content)
    
    # Write the combined markdown file
    with open(output_path, 'w', encoding='utf-8') as f:
        # Write title
        f.write("# Databricks API Documentation\n\n")
        
        # Write table of contents
        f.write("## Table of Contents\n\n")
        if api_docs:
            f.write("1. [API Endpoints](#api-endpoints)\n")
            f.write("2. [General Documentation](#general-documentation)\n\n")
        else:
            f.write("1. [General Documentation](#general-documentation)\n\n")
        
        # Write API documentation
        if api_docs:
            f.write("# API Endpoints\n\n")
            for heading, description in sorted(api_docs):
                f.write(f"{heading}\n\n")
                if description:
                    f.write(f"{description}\n\n")
        
        # Write general documentation
        f.write("# General Documentation\n\n")
        for content in general_docs:
            f.write(f"{content}\n\n")

def extract_api_info(content: str) -> tuple:
    """Extract API endpoint information and documentation."""
    # Look for API endpoint patterns
    endpoint_match = re.search(r'`\n([A-Z]+)/api/([^`]+)`', content, re.MULTILINE | re.DOTALL)
    if endpoint_match:
        method = endpoint_match.group(1)
        endpoint = endpoint_match.group(2)
        
        # Extract the description that follows the endpoint
        parts = content.split('`\n' + method + '/api/')
        if len(parts) > 1:
            description = parts[1].split('`', 1)[1].strip()
            return f"## {method} /{endpoint}", description
    return None, None

# Functions for specific use cases that will be called from scripts
def clean_databricks_docs(
    input_file: Optional[Path] = None,
    output_file: Optional[Path] = None,
    include_metadata: bool = False
) -> int:
    """
    Extract and clean markdown from Databricks documentation JSON.
    
    Args:
        input_file: Path to input JSON file (defaults to standard location)
        output_file: Path to output JSON file (defaults to standard location)
        include_metadata: Whether to include metadata in the output
        
    Returns:
        int: Number of documents processed
    """
    # Use default paths if not provided
    if input_file is None:
        input_file = Path('data/documents/raw/Databricks_docs.json')
    if output_file is None:
        output_file = Path('data/documents/cleaned/Databricks_docs_cleaned.json')
    
    # Create output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Read the original JSON file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract only the markdown fields
    cleaned_data = []
    for item in data:
        if 'markdown' in item:
            # Include only markdown or add other fields based on include_metadata
            if include_metadata:
                cleaned_data.append(item)
            else:
                cleaned_data.append({'markdown': item['markdown']})
    
    # Write the cleaned data to a new file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, indent=2, ensure_ascii=False)
    
    return len(cleaned_data)

def convert_databricks_docs_to_md(
    input_file: Optional[Path] = None,
    output_file: Optional[Path] = None
) -> None:
    """
    Convert Databricks cleaned JSON to markdown.
    
    Args:
        input_file: Path to input JSON file (defaults to standard location)
        output_file: Path to output markdown file (defaults to standard location)
    """
    # Use default paths if not provided
    if input_file is None:
        input_file = Path('data/documents/cleaned/Databricks_docs_cleaned.json')
    if output_file is None:
        output_file = Path('data/documents/databricks_documentation.md')
    
    # Call the main converter with Databricks-specific settings
    convert_json_to_md(
        str(input_file),
        str(output_file),
        doc_type="databricks",
        aggressive_clean=True,
        include_metadata=True
    )