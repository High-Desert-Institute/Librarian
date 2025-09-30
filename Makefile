# Librarian Makefile
# Simple build automation following CLI-first development practices

.PHONY: help install test clean run dev

# Default target
help:
	@echo "Librarian Development Commands"
	@echo "============================="
	@echo "install    - Install dependencies"
	@echo "test       - Run tests"
	@echo "clean      - Clean build artifacts"
	@echo "run        - Run the application"
	@echo "dev        - Run in development mode"
	@echo "format     - Format code with black"
	@echo "lint       - Run linting checks"

# Install dependencies
install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

# Run tests
test:
	python -m pytest tests/ -v

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf __pycache__/
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete

# Run the application
run:
	python -m app --help

# Development mode
dev:
	python -m app --verbose

# Format code
format:
	black app/ tests/

# Lint code
lint:
	flake8 app/ tests/
	mypy app/

# Test mode
test-mode:
	python -m app --test --verbose
