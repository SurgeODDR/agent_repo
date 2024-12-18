import httpx
from typing import Optional, Dict, List
from ..config import PERPLEXITY_API_KEY

class PerplexityClient:
    def __init__(self):
        self.api_key = PERPLEXITY_API_KEY
        self.base_url = "https://api.perplexity.ai/chat/completions"
        
    def research_query(self, query: str, max_results: int = 5) -> List[Dict]:
        """
        Perform a research query using Perplexity API.
        
        Args:
            query: The research query
            max_results: Maximum number of results to return
            
        Returns:
            List[Dict]: List of research results with sources
        """
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": "llama-3.1-sonar-huge-128k-online",  # Using online model for research
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a research assistant. Please provide detailed information with sources."
                    },
                    {
                        "role": "user",
                        "content": query
                    }
                ],
                "max_tokens": 5000,
                "temperature": 0.7,
                "include_citations": True,
                "include_related_questions": True
            }
            
            with httpx.Client() as client:
                response = client.post(
                    self.base_url,
                    headers=headers,
                    json=payload,
                    timeout=30.0
                )
                response.raise_for_status()
                
                data = response.json()
                results = []
                
                # Extract main response and citations
                if "choices" in data and len(data["choices"]) > 0:
                    main_response = data["choices"][0]["message"]["content"]
                    citations = data.get("citations", [])
                    
                    # Format the results
                    results.append({
                        "text": main_response,
                        "source": "Perplexity AI",
                        "relevance": 1.0,
                        "citations": citations[:max_results]
                    })
                
            return results
                
        except Exception as e:
            print(f"Error performing research query: {str(e)}")
            return [] 