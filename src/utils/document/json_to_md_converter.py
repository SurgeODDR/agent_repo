import json
import os
import re
from typing import List, Optional, Dict

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

def convert_json_to_md(
    json_file_path: str,
    output_file_path: Optional[str] = None,
    aggressive_clean: bool = True
) -> None:
    """
    Convert a JSON file containing documentation to a clean markdown format.
    
    Args:
        json_file_path (str): Path to the input JSON file
        output_file_path (str, optional): Path to save the output markdown file
        aggressive_clean (bool): Whether to perform aggressive cleaning of metadata
    """
    try:
        # Validate input file
        if not os.path.exists(json_file_path):
            raise FileNotFoundError(f"Input file not found: {json_file_path}")
        
        # Set output path
        if output_file_path is None:
            output_file_path = os.path.splitext(json_file_path)[0] + '.md'
        
        # Create cleaner instance
        cleaner = MarkdownCleaner(aggressive_clean=aggressive_clean)
        
        # Read and process JSON
        with open(json_file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON file: {str(e)}")
        
        # Process each document
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
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(markdown_content))
        
        print(f"Conversion complete! Markdown file saved to: {output_file_path}")
        
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        raise

if __name__ == "__main__":
    input_file = "/Users/olivierdebeufderijcker/Documents/GitHub/agent_repo/data/raw/json_data/pydanticAI_docs/documents_1 (5).json"
    convert_json_to_md(input_file) 