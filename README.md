# Product Health Sandbox

A disposable repository for testing GitHub integrations in a
project health monitoring application.

## Features

- Python application
- Automated tests with pytest
- Linting with Ruff
- GitHub Actions CI
- CodeQL code scanning
- Dependabot configuration and alert testing
- Pull request and review lifecycle testing
- Release and tag testing

## Local Setup

Create and activate a Python virtual environment.

Install development dependencies:

    python -m pip install -r requirements-dev.txt

Run tests:

    python -m pytest -v

Run linting:

    python -m ruff check .

Run the application:

    python -m src.app

## Repository Safety

This repository is for testing only.

Never commit real credentials, production data, or confidential code.