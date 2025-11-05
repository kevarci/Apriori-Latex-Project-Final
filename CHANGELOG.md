# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-10-22

### Added
- Complete implementation of `utils/data_loader.py` module with comprehensive data loading functions
- Complete implementation of `utils/visualization.py` module with multiple plotting functions
- Configuration management with `config.py` and `.env.example`
- Package structure with `__init__.py` files
- Comprehensive test suite with pytest
  - Unit tests for data_loader module
  - Unit tests for visualization module
  - Test fixtures and edge case coverage
- CI/CD pipeline with GitHub Actions
  - Automated testing on multiple Python versions
  - Code linting with flake8
  - Code formatting checks with black and isort
  - Coverage reporting
- Project documentation
  - Improved README.md with detailed setup instructions
  - CONTRIBUTING.md with contribution guidelines
  - CHANGELOG.md for tracking changes
  - setup.py for package distribution
  - pytest.ini for test configuration
- Enhanced Streamlit application with:
  - Better error handling
  - Dynamic path resolution
  - Interactive metrics display
  - Multiple visualization tabs
  - Improved UI/UX

### Changed
- Fixed corrupted `requirements.txt` (was UTF-16LE, now UTF-8)
- Cleaned up dependencies in requirements.txt (removed unnecessary packages)
- Updated app.py to use relative paths instead of hardcoded paths
- Enhanced .gitignore for Python projects
- Improved code documentation with comprehensive docstrings
- Added logging throughout the application

### Fixed
- Empty utility modules that were causing import errors
- Hardcoded paths in app.py that prevented running in different environments
- Missing error handling in data loading functions
- Lack of input validation in utility functions

### Security
- Added input validation to prevent potential security issues
- Implemented proper error handling to avoid information disclosure
- Added .env support for sensitive configuration

## [1.0.0] - 2024

### Added
- Initial project structure
- LaTeX presentation (main.tex)
- Jupyter notebook with Apriori implementation (hibridApriori.ipynb)
- Basic Streamlit app structure
- Project documentation in docs/
- Sample data files (TransactionsInstacart.csv, products.csv, order_products__train.csv)

---

## Contributing

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## Authors

- **Fernanda Flores**
- **Kevin Arciniegas**
- **Giussepe Marreros**

**Institution:** 4Geeks Academy
