import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys and Credentials
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY", "jina_a429158666cb45578acd3b0cf0847fe7nMULcZ_1S2CPSsxAsagaJu2u_M8k")

# API Endpoints
JINA_READER_ENDPOINT = "https://r.jina.ai/"
DEEPSEEK_API_ENDPOINT = "https://api.deepseek.com/v3"

# Validation
if not all([PERPLEXITY_API_KEY, ANTHROPIC_API_KEY, JINA_API_KEY]):
    raise ValueError("Missing required API keys in environment variables") 
