# Development Setup Guide

This guide will help you set up the development environment with pre-commit hooks and understand the CI/CD pipeline.

## Prerequisites

- Python 3.8 or higher
- Git

## Initial Setup

### 1. Create and Activate Virtual Environment

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate     # On Windows
```

### 2. Install Development Dependencies

```bash
# Install development dependencies (with virtual environment activated)
pip install -r requirements-dev.txt
```

### 2. Install Pre-commit Hooks

```bash
# Install pre-commit hooks
pre-commit install

# (Optional) Run hooks on all files to test setup
pre-commit run --all-files
```

## Pre-commit Hooks

The following hooks will run automatically before each commit:

### Code Quality
- **black**: Formats Python code with consistent style
- **isort**: Sorts and organizes imports
- **flake8**: Lints Python code for style and errors
- **mypy**: Performs static type checking
- **autoflake**: Removes unused imports and variables
- **pyupgrade**: Updates Python syntax to newer versions

### Security & Documentation
- **bandit**: Scans for security vulnerabilities
- **pydocstyle**: Checks docstring style (Google convention)

### General
- **trailing-whitespace**: Removes trailing whitespace
- **end-of-file-fixer**: Ensures files end with newline
- **check-yaml**: Validates YAML syntax
- **check-json**: Validates JSON syntax
- **debug-statements**: Prevents debug statements in commits

## GitHub Actions CI/CD

The CI pipeline runs on:
- Push to `main`, `develop`, or `feature/*` branches
- Pull requests to `main` or `develop`

### CI Jobs

1. **Test Matrix**: Runs tests on Python 3.8, 3.9, 3.10, and 3.11
2. **Pre-commit**: Runs all pre-commit hooks
3. **Build Check**: Verifies the application runs successfully

### What Gets Checked
- Code formatting (black, isort)
- Linting (flake8)
- Type checking (mypy)
- Security scanning (bandit)
- Application execution test

## Manual Commands

You can run these commands manually during development:

```bash
# Format code
black .
isort .

# Lint code
flake8 .
mypy .

# Security check
bandit -r .

# Run pre-commit hooks manually
pre-commit run --all-files

# Test the application
python tax_calculator.py
```

## Configuration Files

- `.pre-commit-config.yaml`: Pre-commit hooks configuration
- `pyproject.toml`: Tool configurations (black, isort, mypy, etc.)
- `.github/workflows/ci.yml`: GitHub Actions CI pipeline
- `requirements.txt`: Production dependencies
- `requirements-dev.txt`: Development dependencies

## Troubleshooting

### Pre-commit Hook Failures
If pre-commit hooks fail:
1. Review the error messages
2. Fix the issues manually or let the hooks auto-fix them
3. Stage the changes: `git add .`
4. Commit again: `git commit -m "your message"`

### CI/CD Failures
If GitHub Actions CI/CD fails:
1. Check that you're not committing the `.venv` directory
2. Ensure all dependencies are in `requirements.txt` and `requirements-dev.txt`
3. The CI excludes `.venv` from linting to avoid false positives

### Skipping Hooks (Not Recommended)
In emergencies, you can skip hooks with:
```bash
git commit --no-verify -m "emergency commit"
```

### Updating Hooks
To update pre-commit hooks to latest versions:
```bash
pre-commit autoupdate
```

### Virtual Environment Issues
If you encounter issues with the virtual environment:
```bash
# Clean and recreate virtual environment
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pre-commit install
```

## Best Practices

1. **Commit Often**: Small, focused commits are easier to review
2. **Write Tests**: Add tests for new functionality (coming soon)
3. **Type Hints**: Use type hints for better code documentation
4. **Docstrings**: Follow Google-style docstrings
5. **Security**: Never commit secrets or sensitive data

## Next Steps

Consider adding:
- Unit tests with pytest
- Integration tests
- Code coverage reporting
- Automated releases
- Documentation generation
