# Contributing to Apriori Recommendation System

Thank you for your interest in contributing to the Apriori Recommendation System! This document provides guidelines for contributing to this project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)

## 🤝 Code of Conduct

This project adheres to a code of conduct that all contributors are expected to follow. Please be respectful and constructive in your interactions.

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Apriori-Latex-Project-Final.git
   cd Apriori-Latex-Project-Final
   ```

3. **Add the upstream repository** as a remote:
   ```bash
   git remote add upstream https://github.com/kevarci/Apriori-Latex-Project-Final.git
   ```

## 💻 Development Setup

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install development dependencies:**
   ```bash
   pip install black isort flake8 pytest pytest-cov
   ```

4. **Set up pre-commit hooks (optional but recommended):**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## 🔧 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- A clear, descriptive title
- Detailed steps to reproduce the bug
- Expected vs actual behavior
- Your environment (OS, Python version, etc.)
- Screenshots if applicable

### Suggesting Enhancements

For feature requests:
- Use a clear, descriptive title
- Provide a detailed description of the proposed feature
- Explain why this feature would be useful
- Include examples if possible

### Contributing Code

1. **Create a new branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. **Make your changes** following the coding standards below

3. **Write or update tests** for your changes

4. **Run tests** to ensure everything passes:
   ```bash
   pytest tests/ -v
   ```

5. **Commit your changes** with a descriptive commit message:
   ```bash
   git add .
   git commit -m "Add feature: description of your changes"
   ```

6. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request** on GitHub

## 📝 Coding Standards

### Python Style Guide

We follow PEP 8 style guide with some modifications:

- **Line length:** Maximum 100 characters
- **Indentation:** 4 spaces (no tabs)
- **Imports:** Organize imports using `isort`
- **Formatting:** Use `black` for automatic formatting

### Code Formatting

Format your code before committing:

```bash
# Format code with black
black utils/ tests/ app.py config.py

# Sort imports with isort
isort utils/ tests/ app.py config.py

# Check with flake8
flake8 utils/ tests/ app.py config.py --max-line-length=100
```

### Documentation

- Add docstrings to all functions, classes, and modules
- Use Google-style docstrings
- Include type hints where applicable
- Update README.md if adding new features

Example docstring:

```python
def function_name(param1, param2):
    """
    Brief description of the function.
    
    Args:
        param1 (type): Description of param1
        param2 (type): Description of param2
        
    Returns:
        type: Description of return value
        
    Raises:
        ExceptionType: Description of when this exception is raised
    """
    pass
```

## 🧪 Testing

### Writing Tests

- Write tests for all new features and bug fixes
- Place tests in the `tests/` directory
- Use descriptive test names that explain what is being tested
- Follow the Arrange-Act-Assert pattern

Example test:

```python
def test_function_name():
    """Test that function_name does what it should."""
    # Arrange
    input_data = create_test_data()
    
    # Act
    result = function_name(input_data)
    
    # Assert
    assert result == expected_result
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ -v --cov=utils --cov-report=html

# Run specific test file
pytest tests/test_data_loader.py -v

# Run specific test
pytest tests/test_data_loader.py::TestDataLoader::test_function_name -v
```

## 🔄 Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new functionality
3. **Ensure all tests pass** locally
4. **Update CHANGELOG.md** with your changes
5. **Create a Pull Request** with:
   - Clear title describing the changes
   - Detailed description of what and why
   - Reference to related issues (e.g., "Fixes #123")
   - Screenshots for UI changes

### PR Review Process

- At least one maintainer must review and approve
- All CI checks must pass
- Code must meet quality standards
- Documentation must be updated

### After Your PR is Merged

1. **Delete your branch** (if using GitHub, this is automatic)
2. **Update your local repository:**
   ```bash
   git checkout main
   git pull upstream main
   ```

## 📞 Getting Help

If you need help:
- Check existing issues and discussions
- Ask questions in issue comments
- Contact the maintainers

## 🙏 Thank You!

Your contributions make this project better. Thank you for taking the time to contribute!

---

**Maintainers:**
- Fernanda Flores
- Kevin Arciniegas
- Giussepe Marreros

**Institution:** 4Geeks Academy
