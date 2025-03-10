"""
Centralized configuration settings for the application.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Base directories
BASE_DIR = Path(__file__).parent.parent.parent.absolute()
SRC_DIR = BASE_DIR / "src"
DATA_DIR = BASE_DIR / "data"
DOCS_DIR = BASE_DIR / "docs"

# Data directories
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
GOLD_DATA_DIR = DATA_DIR / "gold"

# Document directories
RAW_DOCUMENTS_DIR = RAW_DATA_DIR / "documents"
PROCESSED_DOCUMENTS_DIR = PROCESSED_DATA_DIR / "documents"

# Financial directories
RAW_FINANCIAL_DIR = RAW_DATA_DIR / "financial"
PROCESSED_FINANCIAL_DIR = PROCESSED_DATA_DIR / "financial"

# Legal directories
RAW_LEGAL_DIR = RAW_DATA_DIR / "legal"
PROCESSED_LEGAL_DIR = PROCESSED_DATA_DIR / "legal"

# API keys
JINA_API_KEY = os.getenv("JINA_API_KEY", "")
JINA_READER_ENDPOINT = os.getenv("JINA_READER_ENDPOINT", "https://api.jina.ai/v1/reader/")
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY", "")

# Application settings
DEFAULT_LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DEFAULT_PDF_PASSWORD = os.getenv("PDF_PASSWORD", "teamheretics")

# Financial settings
FINANCIAL_PLAN_TEMPLATE = os.getenv("FINANCIAL_PLAN_TEMPLATE", "FinancialPlan.xlsx")