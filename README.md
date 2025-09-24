# GitHub Class Demo Project

This repository is a **demonstration project** designed to showcase modern Python development practices, CI/CD pipelines, and Git workflows. It serves as a hands-on example for learning about code quality tools, automated testing, and GitHub Actions.

## 🎯 Purpose

This project demonstrates:
- **Python development best practices** with type hints and documentation
- **Pre-commit hooks** for automated code quality checks
- **GitHub Actions CI/CD** pipeline for continuous integration
- **Code quality tools** integration (linting, formatting, security scanning)
- **Git workflow** with feature branches and pull requests

## 📁 Project Structure

```
github-class-demo/
├── tax_calculator.py          # Main Python application
├── requirements.txt           # Production dependencies (currently empty)
├── requirements-dev.txt       # Development tools and dependencies
├── pyproject.toml            # Tool configurations (black, isort, mypy, etc.)
├── .pre-commit-config.yaml   # Pre-commit hooks configuration
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions CI/CD pipeline
├── SETUP.md                  # Detailed development setup instructions
└── README.md                 # This file
```

## 🚀 The Demo Application

The main application (`tax_calculator.py`) is a Python tax calculation system that demonstrates:

- **Object-oriented programming** with the `AdvancedTaxCalculator` class
- **Type hints** for better code documentation and IDE support
- **Complex business logic** with regional tax rates, discounts, and categories
- **Time-based features** (happy hour discounts)
- **Data processing** with dictionaries and structured output

### Key Features
- Regional tax calculation (default: California)
- Premium customer discounts
- Time-based promotional discounts (2-4 PM happy hour)
- Category-based tax rules (luxury surcharge, exemptions)
- Comprehensive transaction processing

## 🛠️ Development Tools & Automation

This project showcases a comprehensive development toolchain:

### Pre-commit Hooks
Automatically run before each commit to ensure code quality:

| Tool | Purpose |
|------|---------|
| **black** | Code formatting with consistent style |
| **isort** | Import sorting and organization |
| **flake8** | Python linting for style and errors |
| **mypy** | Static type checking |
| **bandit** | Security vulnerability scanning |
| **pydocstyle** | Docstring style checking (Google convention) |
| **autoflake** | Remove unused imports and variables |
| **pyupgrade** | Upgrade Python syntax to newer versions |

### GitHub Actions CI/CD
The CI pipeline (`/.github/workflows/ci.yml`) demonstrates:

- **Multi-version testing** (Python 3.8, 3.9, 3.10, 3.11)
- **Dependency caching** for faster builds
- **Parallel job execution** (test, pre-commit, build-check)
- **Code quality gates** that must pass before merging
- **Security scanning** with bandit
- **Build verification** to ensure the application runs

### Configuration Management
- **pyproject.toml**: Centralized tool configuration
- **requirements files**: Separate production and development dependencies
- **Git hooks**: Automated quality checks

## 📚 Learning Objectives

This demo teaches:

1. **Modern Python Development**
   - Type hints and documentation
   - Code organization and structure
   - Error handling and edge cases

2. **Code Quality Automation**
   - Pre-commit hooks setup and usage
   - Automated formatting and linting
   - Security scanning integration

3. **CI/CD Best Practices**
   - GitHub Actions workflow design
   - Multi-environment testing
   - Automated quality gates

4. **Git Workflow**
   - Feature branch development
   - Pull request process
   - Code review automation

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone <repository-url>
cd github-class-demo

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or .venv\Scripts\activate  # Windows

# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

### 2. Run the Demo Application
```bash
python tax_calculator.py
```

Expected output demonstrates the tax calculation system with:
- Regional tax processing
- Premium customer discounts
- Time-based promotions
- Detailed transaction breakdown

### 3. Test the Development Workflow
```bash
# Make a small change to the code
# Try to commit - pre-commit hooks will run automatically
git add .
git commit -m "test commit"

# Run hooks manually on all files
pre-commit run --all-files
```

## 🔄 CI/CD Pipeline

The GitHub Actions pipeline automatically:

1. **Tests** the code on multiple Python versions
2. **Runs** all pre-commit hooks
3. **Verifies** the application builds and runs successfully
4. **Blocks** merging if any checks fail

This ensures that all code in the main branch meets quality standards.

## 📖 Detailed Setup

For complete development environment setup instructions, see [SETUP.md](SETUP.md).

## 🎓 Educational Value

This project demonstrates real-world development practices used in professional software development:

- **Automated quality assurance** reduces bugs and improves maintainability
- **CI/CD pipelines** enable confident, frequent deployments
- **Type checking** catches errors before runtime
- **Security scanning** identifies potential vulnerabilities
- **Consistent formatting** improves code readability and team collaboration

## 🤝 Contributing

This is a demo project, but you can practice the workflow by:

1. Creating a feature branch: `git checkout -b feature/your-feature`
2. Making changes to the code
3. Committing (pre-commit hooks will run)
4. Pushing and creating a pull request
5. Observing the CI/CD pipeline in action

## 📝 Next Steps

To extend this demo, consider adding:
- Unit tests with pytest
- Code coverage reporting
- Integration tests
- Automated releases
- Documentation generation
- Docker containerization

---

**Note**: This is a demonstration project for educational purposes. The tax calculation logic is simplified and should not be used for actual financial calculations.
