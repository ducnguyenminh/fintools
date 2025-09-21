# FinTools Development Environment Setup

This directory contains the FinTools project - a Python library for financial calculations.

## Quick Start

1. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux
```

2. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

3. Install the package in development mode:
```bash
pip install -e .
```

4. Run tests:
```bash
pytest
```

5. Try the examples:
```bash
python examples/basic_usage.py
```

## Project Structure

```
fintools/
├── src/fintools/           # Main package code
├── tests/                  # Test files
├── examples/              # Usage examples
├── pyproject.toml         # Modern Python project config
├── requirements*.txt      # Dependencies
├── README.md             # Project documentation
├── LICENSE               # MIT License
├── CONTRIBUTING.md       # Contribution guidelines
└── .gitignore           # Git ignore rules
```
