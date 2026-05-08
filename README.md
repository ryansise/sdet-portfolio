# SDET Portfolio

## Description
This is a collection of automated tests on publicly-available APIs that don't require account login.  This will be done using Python automation test frameworks, and I will update this readme with the tech as I build them.

## Quick Start (Any Clone)
```bash
git clone https://github.com/ryansise/sdet-portfolio
cd sdet-portfolio
# 1. Python venv (30 seconds)
python3 -m venv .venv && source .venv/bin/activate # Linux/Mac
# .venv\Scripts\activate
# Windows
# 2. Install exact deps
pip install -r requirements.txt
playwright install --with-deps
# 3. Run tests + watch videos
pytest tests/