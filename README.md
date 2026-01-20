This repository contains an automated QA test suite for Kiwi.com built with Python, Playwright, and pytest,
following the Page Object Model (POM) and Gherkin-style BDD practices.

The automation task focuses on verifying flight search functionality, including a "one-way flight search" scenario.

## Tech stack:
- Python 3.11+
- pytest
- pytest-bdd
- Playwright
- Docker

## Setup
Clone the repo:
git clone https://github.com/AngelinaBGit/kiwi_playwrigt.git
cd kiwi_playwrigt

Install Python dependencies:
python -m pip install --upgrade pip
pip install -r requirements.txt

Install Playwright browsers:
playwright install

## Running Tests
Run all tests:
pytest

Running Specific Test:
pytest -m basic_search

## Run tests in Docker
Build image:
docker build -t kiwi-tests .

Run tests:
docker run --rm kiwi-tests

## CI/CD
Automated tests are executed using GitHub Actions.

Install dependencies:
pip install -r requirements.txt
playwright install

Workflow file: `.github/workflows/tests.yml`

## Bot Protection Limitation

Kiwi.com is protected by Cloudflare anti-bot security.
The site blocks headless browsers, so tests running in headless mode will fail at the homepage.
For stable execution, tests are run in headed mode (headless=False), both locally and in CI.
In CI (GitHub Actions), Xvfb is used to provide a virtual display for the headed browser.
Note: This is expected behavior for production travel websites and does not indicate an issue with the test implementation.


