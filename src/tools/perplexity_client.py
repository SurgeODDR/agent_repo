from typing import Optional, Dict, List
from perplexity import Perplexity
from ..config import PERPLEXITY_API_KEY

class PerplexityClient:
    def __init__(self):
        self.client = Perplexity(api_key=PERPLEXITY_API_KEY)
    
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
            response = self.client.search(query)
            results = []
            
            for i, result in enumerate(response):
                if i >= max_results:
                    break
                    
                results.append({
                    "text": result.text,
                    "source": result.source,
                    "relevance": result.relevance_score
                })
                
            return results
        except Exception as e:
            print(f"Error performing research query: {str(e)}")
            return [] 