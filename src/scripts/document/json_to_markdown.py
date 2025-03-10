import json
import os
import re
from pathlib import Path

def clean_content(content):
    """Clean and organize the markdown content."""
    # Remove repeated empty lines
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    # Process each line
    lines = content.split('\n')
    processed_lines = []
    in_api_section = False
    
    for line in enumerate(lines):
        line = line[1]  # Get the actual line from enumerate tuple
        
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

def extract_api_info(content):
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

def get_content_hash(content):
    """Get a simple hash of the content for comparison."""
    return hash(content.strip())

def convert_json_to_markdown():
    # Read the cleaned JSON file
    input_file = 'data/documents/cleaned/Databricks_docs_cleaned.json'
    output_file = 'data/documents/databricks_documentation.md'
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Read the JSON file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Process and deduplicate content
    unique_contents = set()
    api_docs = []
    general_docs = []
    
    for entry in data:
        content = clean_content(entry['markdown'])
        if not content:
            continue
        
        content_hash = get_content_hash(content)
        if content_hash in unique_contents:
            continue
        
        unique_contents.add(content_hash)
        
        # Check if it's an API endpoint documentation
        api_heading, api_description = extract_api_info(entry['markdown'])
        if api_heading:
            if api_description:
                api_docs.append((api_heading, api_description))
        else:
            # Only add to general docs if it contains meaningful content
            if len(content.split()) > 3:  # Skip very short content
                general_docs.append(content)
    
    # Write the combined markdown file
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write title
        f.write("# Databricks API Documentation\n\n")
        
        # Write table of contents
        f.write("## Table of Contents\n\n")
        f.write("1. [API Endpoints](#api-endpoints)\n")
        f.write("2. [General Documentation](#general-documentation)\n\n")
        
        # Write API documentation
        f.write("# API Endpoints\n\n")
        for heading, description in sorted(api_docs):
            f.write(f"{heading}\n\n")
            if description:
                f.write(f"{description}\n\n")
        
        # Write general documentation
        f.write("# General Documentation\n\n")
        for content in general_docs:
            f.write(f"{content}\n\n")
            
        print(f"Created: {output_file}")

if __name__ == '__main__':
    convert_json_to_markdown() 