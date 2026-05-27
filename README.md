[![CI](https://github.com/ryansise/sdet-portfolio/actions/workflows/github-actions.yml/badge.svg)](https://github.com/ryansise/sdet-portfolio/actions/workflows/github-actions.yml)

# SDET Portfolio

This repository showcases practical test automation work built with Python. It includes UI automation, API validation, and a small end-to-end browser test, all organized to demonstrate the kind of automation skills used in real SDET roles.

## What’s included

- Playwright-based form validation tests.
- Requests-based API tests using environment-driven configuration.
- A simple TodoMVC browser test that demonstrates pytest and Playwright fundamentals.

## Tech stack

- Python
- pytest
- Playwright
- Requests
- python-dotenv
- pytest-playwright
- pytest-base-url

## Why these tests are written this way

- `test_form_entry.py` uses the browser’s native validation state through the `:invalid` pseudo-class because the practice site does not expose a stable error locator. That keeps the test aligned with what the user actually experiences in the browser.
- `test_api.py` reads the base URL and API key from a local `.env` file so private values stay out of version control. The fixture also fails fast if required variables are missing, which makes setup issues easy to spot.
- The TodoMVC test is intentionally lightweight and serves as a clean example of browser automation, fixture usage, and test organization.

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

## Environment setup

Create a local `.env` file for API tests:

```bash
REQRES_BASE_URL=your_api_url_here
REQRES_API_KEY=your_api_key_here
```

This file is ignored by Git and used only on the local machine.

## Test layout

- `test_form_entry.py` — UI validation tests for required inputs and invalid values.
- `test_api.py` — API tests covering authenticated requests, response checks, and negative coverage.
- `test_todomvc.py` — Simple browser automation example using Playwright and pytest.

## Continuous Integration

This repository uses GitHub Actions to run the test suite on push and pull request events with Python 3.12.

The workflow installs dependencies, installs Playwright browsers, runs the tests, and uploads an HTML report artifact for review.

## Repository hygiene

- Generated caches such as `.pytest_cache` and `__pycache__` are ignored.
- Playwright reports are excluded from version control.
- The repo will continue to expand as additional automation examples are added.