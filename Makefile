.PHONY: help install test lint format clean run docs

# Default target
help:
	@echo "Apriori Recommendation System - Makefile Commands"
	@echo "=================================================="
	@echo ""
	@echo "Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make test       - Run tests with pytest"
	@echo "  make lint       - Run code linting"
	@echo "  make format     - Format code with black and isort"
	@echo "  make clean      - Clean temporary files"
	@echo "  make run        - Run the Streamlit application"
	@echo "  make docs       - Generate documentation"
	@echo "  make coverage   - Run tests with coverage report"
	@echo ""

# Install dependencies
install:
	@echo "📦 Installing dependencies..."
	pip install --upgrade pip
	pip install -r requirements.txt
	@echo "✅ Dependencies installed"

# Install development dependencies
install-dev: install
	@echo "📦 Installing development dependencies..."
	pip install black isort flake8 pytest pytest-cov
	@echo "✅ Development dependencies installed"

# Run tests
test:
	@echo "🧪 Running tests..."
	pytest tests/ -v

# Run tests with coverage
coverage:
	@echo "🧪 Running tests with coverage..."
	pytest tests/ -v --cov=utils --cov-report=html --cov-report=term-missing
	@echo "📊 Coverage report generated in htmlcov/"

# Lint code
lint:
	@echo "🔍 Linting code..."
	flake8 utils/ tests/ app.py config.py --max-line-length=100 --exclude=venv,env,.git

# Format code
format:
	@echo "✨ Formatting code..."
	black utils/ tests/ app.py config.py
	isort utils/ tests/ app.py config.py
	@echo "✅ Code formatted"

# Clean temporary files
clean:
	@echo "🧹 Cleaning temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache htmlcov .coverage 2>/dev/null || true
	@echo "✅ Cleaned"

# Run the Streamlit application
run:
	@echo "🌐 Starting Streamlit application..."
	streamlit run app.py

# Generate documentation
docs:
	@echo "📚 Documentation is available in:"
	@echo "  - README.md"
	@echo "  - CONTRIBUTING.md"
	@echo "  - ANALYSIS.md"
	@echo "  - CHANGELOG.md"

# Check code quality
quality: lint test
	@echo "✅ Code quality check passed"

# Setup development environment
setup: install-dev
	@echo "🔧 Setting up development environment..."
	@echo "✅ Development environment ready"
