# CLAUDE.md - Agent Reference Guide

## Build/Test/Lint Commands
- Run all tests: `pytest tests/`
- Run single test: `pytest tests/path/to/test_file.py::test_function_name`
- Format code: `black src/ tests/`
- Sort imports: `isort src/ tests/`
- Type checking: `mypy src/ tests/`

## Code Style Guidelines
- **Imports**: Standard library first, third-party second, local imports last with blank line separations
- **Formatting**: Use Black with default settings
- **Type Annotations**: Required for all function parameters and return values
- **Docstrings**: Triple-quoted docstrings for modules, classes, and functions with detailed descriptions
- **Naming**: `snake_case` for functions/variables, `PascalCase` for classes
- **Error Handling**: Use specific exception types, include descriptive error messages, and proper logging
- **Logging**: Configure per module with appropriate log levels (INFO, WARNING, ERROR)
- **File Structure**: Maintain logical organization in src/ (by domain) and tests/ (unit/integration)
- **Testing**: Use pytest fixtures and parameterized tests where appropriate

This project processes various document types including PDFs, Excel files, and markdown documents, organizing data into raw, processed, and gold directories.