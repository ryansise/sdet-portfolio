# SDET Portfolio

## Overview
A portfolio of Python test automation projects covering UI and API testing. The repo demonstrates pytest-based test design, Playwright browser automation, and Requests-based API validation.

## What’s included
- UI validation tests using Playwright and pytest.
- API testing using Requests and environment-based configuration.
- A simple TodoMVC test showing basic end-to-end automation.

## Tech stack
- Python
- pytest
- Playwright
- Requests
- python-dotenv

## Quick start
```bash
git clone https://github.com/ryansise/sdet-portfolio
cd sdet-portfolio
python3 -m venv .venv
source .venv/bin/activate    # Linux/Mac
# .venv\Scripts\activate     # Windows
pip install -r requirements.txt
playwright install --with-deps
pytest tests/
```

## Notes
- API tests use environment variables stored in a local `.env` file.
- Browser tests are configured to retain videos on failure.
- This repo is a work in progress and will continue to expand with additional automation examples.