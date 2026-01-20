Tech stack:
- Python
- pytest
- pytest-bdd
- Playwright

Run tests:
```bash
pytest -m basic_search

## Run tests in Docker

Build image:
docker build -t kiwi-tests .

Run tests:
docker run --rm kiwi-tests

## CI/CD

Automated tests are executed using GitHub Actions.

Pipeline is triggered on:
- push to main branch
- pull request to main branch

Workflow file: `.github/workflows/tests.yml`

Steps:
- checkout repository
- setup Python 3.12
- install dependencies
- install Playwright browsers
- run pytest tests

