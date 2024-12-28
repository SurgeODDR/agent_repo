import os
import sys
from pathlib import Path
from typing import Dict, List, Optional
import json

# Add src directory to Python path
sys.path.append(str(Path(__file__).parent.parent / "src"))
from tools.jina_reader import JinaReader

class RepoDocumenter:
    """Class to document a repository's structure and contents using Jina Reader."""
    
    DEFAULT_EXCLUDE_DIRS = {
        "venv", "__pycache__", "node_modules", ".git", ".idea", ".vscode",
        "dist", "build", "env", ".env", "logs", "cache", "temp"
    }
    
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
        self.jina_reader = JinaReader()
        if not self.repo_path.exists():
            raise ValueError(f"Directory {repo_path} does not exist")
    
    def _should_exclude(self, path: Path) -> bool:
        """Check if a path should be excluded from documentation."""
        # Exclude hidden files/directories and default exclude dirs
        if any(part.startswith('.') for part in path.parts):
            return True
        return path.name in self.DEFAULT_EXCLUDE_DIRS
    
    def _get_repo_structure(self) -> Dict[str, List[str]]:
        """Get the repository structure as a dictionary."""
        structure = {}
        for root, dirs, files in os.walk(self.repo_path):
            # Filter out excluded directories
            dirs[:] = [d for d in dirs if not self._should_exclude(Path(root) / d)]
            
            relative_path = str(Path(root).relative_to(self.repo_path))
            if relative_path == '.':
                relative_path = ''
            
            structure[relative_path] = files
        
        return structure
    
    def _get_file_summary(self, file_path: Path) -> str:
        """Get a summary of a file's contents using DeepSeek Chat."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if not content.strip():
                return "Empty file"
            
            # Use Jina Reader to generate a summary
            prompt = f"Please provide a concise summary of this code file:\n\n{content}"
            response = self.jina_reader.scrape_url(f"https://api.deepseek.com/v3/analyze?text={prompt}")
            if response:
                return response
            return "Unable to generate summary"
        except Exception as e:
            return f"Error reading file: {str(e)}"
    
    def document_repository(self) -> Dict:
        """Generate comprehensive documentation for the repository."""
        documentation = {
            "repository_path": str(self.repo_path),
            "structure": {},
            "file_descriptions": {}
        }
        
        # Get repository structure
        structure = self._get_repo_structure()
        documentation["structure"] = structure
        
        # Generate descriptions for each file
        for directory, files in structure.items():
            for file in files:
                file_path = self.repo_path / directory / file
                if self._should_exclude(file_path):
                    continue
                
                file_description = self._get_file_summary(file_path)
                relative_path = str(Path(directory) / file)
                documentation["file_descriptions"][relative_path] = file_description
        
        return documentation
    
    def save_documentation(self, output_path: str, format: str = "json"):
        """Save the repository documentation to a file."""
        documentation = self.document_repository()
        
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        if format == "json":
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(documentation, f, indent=2)
        else:
            raise ValueError(f"Unsupported format: {format}")

def document_repository(repo_path: str, output_path: str):
    """Convenience function to document a repository."""
    documenter = RepoDocumenter(repo_path)
    documenter.save_documentation(output_path)

if __name__ == "__main__":
    # Example usage
    repo_path = input("Enter repository path: ")
    output_path = input("Enter output file path: ")
    document_repository(repo_path, output_path)
