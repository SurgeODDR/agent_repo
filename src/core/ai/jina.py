import requests
from typing import Optional, Dict
from src.config.settings import JINA_API_KEY, JINA_READER_ENDPOINT

class JinaReader:
    def __init__(self):
        self.api_key = JINA_API_KEY
        self.endpoint = JINA_READER_ENDPOINT
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
    
    def scrape_url(self, url: str) -> Optional[str]:
        """
        Scrape a URL using Jina Reader API and return markdown content.
        
        Args:
            url: The URL to scrape
            
        Returns:
            Optional[str]: Markdown content if successful, None if failed
        """
        try:
            response = requests.get(
                f"{self.endpoint}{url}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Error scraping URL {url}: {str(e)}")
            return None 