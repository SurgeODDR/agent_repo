from typing import List, Dict, Optional
from .tools.jina_reader import JinaReader
from .tools.perplexity_client import PerplexityClient
from .tools.pdf_processor import PDFProcessor

class ResearchAgent:
    def __init__(self):
        self.jina_reader = JinaReader()
        self.perplexity = PerplexityClient()
        self.pdf_processor = PDFProcessor()
        
    def research_topic(self, 
                      query: str,
                      urls: List[str] = None,
                      pdfs: List[str] = None,
                      max_results: int = 5) -> Dict:
        """
        Perform comprehensive research on a topic using all available tools.
        
        Args:
            query: The research query
            urls: List of URLs to scrape
            pdfs: List of PDF files to analyze
            max_results: Maximum number of results per source
            
        Returns:
            Dict: Combined research results from all sources
        """
        results = {
            "perplexity_results": [],
            "web_content": [],
            "pdf_analysis": []
        }
        
        # Perplexity API research
        results["perplexity_results"] = self.perplexity.research_query(
            query, max_results=max_results
        )
        
        # Web scraping with Jina Reader
        if urls:
            for url in urls:
                content = self.jina_reader.scrape_url(url)
                if content:
                    results["web_content"].append({
                        "url": url,
                        "content": content
                    })
        
        # PDF analysis
        if pdfs:
            for pdf_path in pdfs:
                analysis = self.pdf_processor.analyze_pdf_content(
                    pdf_path,
                    f"Analyze this document in the context of the following query: {query}"
                )
                if analysis:
                    results["pdf_analysis"].append({
                        "file": pdf_path,
                        "analysis": analysis
                    })
        
        return results
    
    def investigate_entity(self, 
                         entity_name: str,
                         context: str,
                         urls: List[str] = None,
                         pdfs: List[str] = None) -> Dict:
        """
        Investigate a specific entity (person, company, etc.) using all available tools.
        
        Args:
            entity_name: Name of the entity to investigate
            context: Additional context about the investigation
            urls: List of URLs to scrape
            pdfs: List of PDF files to analyze
            
        Returns:
            Dict: Investigation results
        """
        query = f"Investigate {entity_name} in the context of {context}"
        return self.research_topic(query, urls, pdfs) 