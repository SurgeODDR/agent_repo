#!/usr/bin/env python3

"""
Script to filter Billit documentation JSON files by:
1. Removing HTML content (keeping only markdown)
2. Cleaning up markdown content by removing non-matching URLs and escape characters
3. Keeping only essential metadata (sourceURL, title, description)
"""

import json
import os
import re
from pathlib import Path
from typing import List, Dict, Any
from urllib.parse import urlparse

def clean_markdown_content(markdown: str, source_url: str) -> str:
    """
    Clean markdown content by:
    1. Removing URLs that don't match the base source URL
    2. Removing escape characters and excessive newlines
    3. Cleaning up markdown formatting
    """
    if not markdown:
        return markdown

    # Get the base domain from source URL
    source_domain = urlparse(source_url).netloc
    
    # Remove escaped characters and normalize newlines
    cleaned = markdown.replace('\\\\', '').replace('\\n', '\n').replace('\\', '')
    
    # Fix code blocks
    cleaned = re.sub(r'```rdmd-code.*?theme-light', '```', cleaned)
    cleaned = re.sub(r'```\s*$', '```\n', cleaned)
    
    # Remove URLs that don't match the source domain
    # Keep the link text if it exists
    def replace_url(match):
        full_match = match.group(0)
        url = match.group(2) if match.group(2) else ''
        link_text = match.group(1)
        
        if source_domain in url:
            return full_match
        return link_text if link_text else ''

    # Handle markdown links [text](url)
    cleaned = re.sub(r'\[([^\]]*)\]\(([^)]*)\)', replace_url, cleaned)
    
    # Remove any remaining URLs
    cleaned = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', cleaned)
    
    # Fix broken markdown links (empty parentheses)
    cleaned = re.sub(r'\[([^\]]+)\]\(\s*\)', r'\1', cleaned)
    
    # Remove empty markdown elements
    cleaned = re.sub(r'\[\s*\]\(\s*\)', '', cleaned)
    cleaned = re.sub(r'\[\s*\]', '', cleaned)
    
    # Remove "Updated X time ago" lines
    cleaned = re.sub(r'Updated.*?ago', '', cleaned)
    
    # Remove "Did this page help you?" section and responses
    cleaned = re.sub(r'Did this page help you\?.*?(Yes|No)', '', cleaned)
    
    # Remove horizontal rules
    cleaned = re.sub(r'\*\s*\*\s*\*', '', cleaned)
    
    # Fix list formatting
    lines = cleaned.split('\n')
    formatted_lines = []
    in_list = False
    
    for line in lines:
        # Handle bullet points
        if re.match(r'^[-*]\s', line):
            if not in_list and formatted_lines:
                formatted_lines.append('')  # Add space before list starts
            in_list = True
            formatted_lines.append(line)
        # Handle numbered lists
        elif re.match(r'^\d+\.\s', line):
            if not in_list and formatted_lines:
                formatted_lines.append('')  # Add space before list starts
            in_list = True
            formatted_lines.append(line)
        else:
            if in_list and line.strip():
                formatted_lines.append('  ' + line)  # Indent continuation lines
            else:
                in_list = False
                formatted_lines.append(line)
    
    cleaned = '\n'.join(formatted_lines)
    
    # Fix multiple newlines
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    
    # Fix spacing around headers
    cleaned = re.sub(r'([^\n])(#+ )', r'\1\n\n\2', cleaned)
    
    # Remove trailing "No" from feedback section
    cleaned = re.sub(r'\s*No\s*$', '', cleaned)
    
    cleaned = cleaned.strip()
    
    # Return None if the content is empty after cleaning
    if not cleaned:
        return None
        
    return cleaned

def clean_metadata(obj: Dict[str, Any]) -> Dict[str, Any]:
    """
    Keep only essential metadata fields:
    - sourceURL (for reference)
    - title (for context)
    - description (for summary)
    """
    metadata = obj.get('metadata', {})
    cleaned = {
        'sourceURL': metadata.get('sourceURL', ''),
        'title': metadata.get('title', ''),
        'description': metadata.get('description', '')
    }
    return {k: v for k, v in cleaned.items() if v}  # Remove empty values

def process_json_file(file_path: Path) -> None:
    """
    Process a single JSON file by:
    1. Removing HTML content
    2. Cleaning markdown content
    3. Keeping only essential metadata
    """
    try:
        print(f"\nProcessing {file_path}...")
        
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            print(f"Warning: File does not contain a list of objects. Skipping.")
            return
        
        original_count = len(data)
        print(f"Found {original_count} objects in file")
        
        # Filter and clean objects
        filtered_data = []
        cleaned_count = 0
        removed_count = 0
        
        for i, obj in enumerate(data, 1):
            if i % 100 == 0:
                print(f"Processed {i}/{original_count} objects...")
            
            new_obj = {}
            
            # Keep only markdown content, remove HTML
            if 'markdown' in obj:
                source_url = obj.get('metadata', {}).get('sourceURL', '')
                original_markdown = obj['markdown']
                cleaned_markdown = clean_markdown_content(original_markdown, source_url)
                
                if cleaned_markdown is not None:
                    new_obj['markdown'] = cleaned_markdown
                    cleaned_count += 1
                else:
                    removed_count += 1
                    continue
            
            # Clean metadata
            if 'metadata' in obj:
                new_obj['metadata'] = clean_metadata(obj)
            
            filtered_data.append(new_obj)
        
        # Calculate statistics
        kept_count = len(filtered_data)
        removed_count = original_count - kept_count
        
        print(f"\nProcessing complete:")
        print(f"- Original objects: {original_count}")
        print(f"- Objects kept: {kept_count}")
        print(f"- Objects removed: {removed_count}")
        print(f"- Objects with cleaned markdown: {cleaned_count}")
        
        # Write filtered data back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, indent=2, ensure_ascii=False)
        print("Changes saved to file")
    
    except Exception as e:
        print(f"Error processing file: {str(e)}")

def main():
    # Directory containing the JSON files
    billit_dir = Path("/Users/olivierdebeufderijcker/Documents/GitHub/agent_repo/data/raw/json_data/billit_docs")
    
    if not billit_dir.exists():
        print(f"Error: Directory {billit_dir} does not exist")
        return
    
    # Process all JSON files in the directory
    json_files = list(billit_dir.glob("*.json"))
    
    if not json_files:
        print(f"No JSON files found in {billit_dir}")
        return
    
    print(f"Found {len(json_files)} JSON files to process")
    
    for file_path in json_files:
        process_json_file(file_path)
    
    print("\nAll processing complete")

if __name__ == "__main__":
    main() 
