import base64
import httpx
import os
from typing import Optional, Dict, List, Union
import anthropic
from ..config import ANTHROPIC_API_KEY

class PDFProcessor:
    MAX_PDF_SIZE_MB = 32
    MAX_PAGES_PER_REQUEST = 100
    
    def __init__(self):
        self.client = anthropic.Client(api_key=ANTHROPIC_API_KEY)
    
    def _validate_pdf(self, pdf_data: bytes) -> bool:
        """
        Validate PDF size constraints.
        
        Args:
            pdf_data: Raw PDF data
            
        Returns:
            bool: True if valid, False otherwise
        """
        size_mb = len(pdf_data) / (1024 * 1024)
        if size_mb > self.MAX_PDF_SIZE_MB:
            print(f"PDF exceeds maximum size limit of {self.MAX_PDF_SIZE_MB}MB")
            return False
        return True
    
    def _encode_pdf(self, pdf_path: str) -> Optional[str]:
        """
        Load and encode a PDF file to base64.
        
        Args:
            pdf_path: Local path or URL to the PDF
            
        Returns:
            Optional[str]: Base64 encoded PDF data
        """
        try:
            if pdf_path.startswith(('http://', 'https://')):
                pdf_data = httpx.get(pdf_path).content
            else:
                with open(pdf_path, 'rb') as f:
                    pdf_data = f.read()
                    
            if not self._validate_pdf(pdf_data):
                return None
                
            return base64.b64encode(pdf_data).decode('utf-8')
        except Exception as e:
            print(f"Error encoding PDF: {str(e)}")
            return None
    
    def analyze_pdf_content(
        self, 
        pdf_path: str, 
        analysis_prompt: str,
        use_cache: bool = False,
        max_tokens: int = 4096
    ) -> Optional[str]:
        """
        Analyze PDF content using Claude's native PDF support.
        
        Args:
            pdf_path: Path or URL to the PDF file
            analysis_prompt: Prompt for analysis
            use_cache: Whether to use Claude's PDF caching
            max_tokens: Maximum tokens for response
            
        Returns:
            Optional[str]: Analysis results if successful, None if failed
        """
        try:
            pdf_data = self._encode_pdf(pdf_path)
            if not pdf_data:
                return None
            
            # Place PDF before text in the content array for optimal performance
            content: List[Dict[str, Union[str, Dict]]] = [
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_data
                    }
                }
            ]
            
            if use_cache:
                content[0]["cache_control"] = {
                    "type": "ephemeral",
                    "ttl": 3600  # Cache for 1 hour
                }
                
            content.append({
                "type": "text",
                "text": analysis_prompt
            })
            
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=max_tokens,
                messages=[{
                    "role": "user",
                    "content": content
                }]
            )
            
            return message.content
        except anthropic.APIError as e:
            print(f"Claude API error: {str(e)}")
            return None
        except Exception as e:
            print(f"Error analyzing PDF content: {str(e)}")
            return None
            
    def batch_process_pdfs(
        self,
        pdf_paths: List[str],
        analysis_prompt: str,
        use_cache: bool = False,
        max_tokens: int = 4096
    ) -> Dict[str, Optional[str]]:
        """
        Process multiple PDFs in batch using Claude's batch API.
        
        Args:
            pdf_paths: List of PDF paths or URLs
            analysis_prompt: Prompt for analysis
            use_cache: Whether to use Claude's PDF caching
            max_tokens: Maximum tokens per response
            
        Returns:
            Dict[str, Optional[str]]: Results keyed by PDF path
        """
        try:
            requests = []
            for i, pdf_path in enumerate(pdf_paths):
                pdf_data = self._encode_pdf(pdf_path)
                if not pdf_data:
                    continue
                    
                # Place PDF before text in content for optimal performance
                content = [
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": pdf_data
                        }
                    }
                ]
                
                if use_cache:
                    content[0]["cache_control"] = {
                        "type": "ephemeral",
                        "ttl": 3600  # Cache for 1 hour
                    }
                
                content.append({
                    "type": "text",
                    "text": analysis_prompt
                })
                
                requests.append({
                    "custom_id": f"doc{i}",
                    "params": {
                        "model": "claude-3-5-sonnet-20241022",
                        "max_tokens": max_tokens,
                        "messages": [{
                            "role": "user",
                            "content": content
                        }]
                    }
                })
            
            batch = self.client.messages.batches.create(requests=requests)
            
            results = {}
            for i, pdf_path in enumerate(pdf_paths):
                doc_id = f"doc{i}"
                if doc_id in batch:
                    results[pdf_path] = batch[doc_id].content
                else:
                    results[pdf_path] = None
                    
            return results
        except anthropic.APIError as e:
            print(f"Claude API error in batch processing: {str(e)}")
            return {path: None for path in pdf_paths}
        except Exception as e:
            print(f"Error in batch processing: {str(e)}")
            return {path: None for path in pdf_paths}