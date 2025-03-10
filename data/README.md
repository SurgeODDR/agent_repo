# Data Directory

This directory contains all data files used by the Document Processing and Management System.

## Directory Structure

- **raw/** - Raw, unprocessed data
  - **documents/** - Raw document files (PDF, Markdown, etc.)
  - **financial/** - Raw financial data (JSON, CSV, Excel, etc.)
  - **legal/** - Raw legal documents

- **processed/** - Processed intermediate data
  - **documents/** - Processed document files
  - **financial/** - Processed financial data
  - **legal/** - Processed legal documents

- **gold/** - Final, ready-to-use datasets

## Data Flow

Data typically flows through the system in the following manner:

1. Raw data is placed in the `raw/` directory (or subdirectories)
2. Processing scripts transform the data and place it in the `processed/` directory
3. Further refinement creates "gold" datasets in the `gold/` directory

## Adding New Data

When adding new data to the repository, please follow these guidelines:

1. Place raw data in the appropriate subdirectory of `raw/`
2. Use the data organization tools in `src/utils/data_organizer.py` to help organize data
3. Document the source and purpose of the data

## Handling Large Files

GitHub has limits on file sizes. For large data files:

1. Consider using Git LFS (Large File Storage)
2. Add large data files to `.gitignore`
3. Provide a script or instructions for downloading large data files