#!/bin/bash

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install base requirements
pip install -r requirements/base.txt

# Install dev requirements if in development mode
if [ "$1" = "--dev" ]; then
    pip install -r requirements/dev.txt
fi

# Install test requirements if running tests
if [ "$1" = "--test" ]; then
    pip install -r requirements/test.txt
fi

# Create necessary directories if they don't exist
mkdir -p data/{raw,processed,gold}
mkdir -p docs/{api,guides,examples}

echo "Setup complete!" 