# Repository Reorganization

This document outlines the restructuring of the repository to improve organization and maintainability.

## Directory Structure

The repository has been reorganized into the following structure:

```
agent_repo/
├── src/                      # All source code
│   ├── core/                 # Core business logic
│   │   ├── document/         # Document processing core functionality
│   │   ├── finance/          # Financial data processing
│   │   ├── legal/            # Legal document processing
│   │   └── ai/               # AI integration components
│   ├── utils/                # Utility functions
│   │   ├── document/         # Document-specific utilities
│   │   ├── finance/          # Finance-specific utilities
│   │   ├── legal/            # Legal utilities
│   │   └── ai/               # AI-specific utilities
│   ├── common/               # Shared functionality
│   │   ├── config.py         # Configuration handling
│   │   └── cli.py            # CLI utilities
│   ├── scripts/              # Entry point scripts
│   │   ├── document/         # Document processing scripts
│   │   ├── finance/          # Financial scripts
│   │   └── ai/               # AI-related scripts
│   └── cli.py                # Main CLI entry point
├── data/                     # All data
│   ├── raw/                  # Raw, unprocessed data
│   │   ├── documents/        # Raw document files
│   │   ├── financial/        # Raw financial data
│   │   └── legal/            # Raw legal documents
│   ├── processed/            # Processed intermediate data
│   │   ├── documents/        # Processed document files
│   │   ├── financial/        # Processed financial data
│   │   └── legal/            # Processed legal documents
│   └── gold/                 # Final, ready-to-use datasets
├── docs/                     # Documentation
│   ├── api/                  # API documentation
│   ├── user/                 # User guides
│   ├── examples/             # Usage examples
│   └── research/             # Research papers and findings
├── tests/                    # Test suite
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   └── fixtures/             # Test fixtures
```

## Reorganization Strategy

### Source Code Organization

1. **Domain-Based Structure**: Code is organized by business domain (document, finance, AI, legal) to group related functionality.

2. **Responsibility Separation**:
   - `core/`: Contains core business logic and algorithms
   - `utils/`: Contains utility functions and helpers
   - `scripts/`: Contains entry point scripts and executables
   - `common/`: Contains shared functionality used across domains

### Data Organization

1. **Three-Stage Pipeline**:
   - `raw/`: Original, unmodified data
   - `processed/`: Intermediate processed data
   - `gold/`: Final, ready-to-use datasets

2. **Domain-Based Subdivision**:
   - Each stage is further subdivided by domain (documents, financial, legal)

### Import Structure

Import statements should follow the new structure. For example:
```python
# Old
from src.document.core import pdf_processor

# New
from src.core.document import pdf_processor
```

## Benefits of Reorganization

1. **Improved Maintainability**: Clearer organization makes it easier to find and maintain code.
2. **Better Code Reuse**: Properly organized utilities and core functions encourage reuse.
3. **Cleaner Data Pipeline**: The three-stage data pipeline provides a clear path for data processing.
4. **Easier Onboarding**: New team members can more easily understand the project structure.
5. **Extensibility**: The domain-based organization makes it easy to add new domains or extend existing ones.

## Future Maintenance Guidelines

1. **New Features**: When adding new features, first identify which domain they belong to and place them accordingly.
2. **New Domains**: If a new business domain is needed, follow the established pattern of core/utils/scripts subdirectories.
3. **Data Files**: Always place data files in the appropriate data subdirectory based on their processing stage and domain.
4. **Scripts**: Place executable scripts in the scripts directory, not at the repository root.