# API Automation Framework

This project is a modular, reusable Python-based REST API automation framework designed for enterprise-level API testing across multiple environments and projects.

## Overview

The framework includes:
- Multiple environment support: DEV, QA, UAT, PROD
- Configurable base URLs and credentials
- Reusable API client utilities
- Request/response payload management
- Response validation
- Test data management
- Logging and exception handling
- CI/CD-ready project structure
- Python + pytest-based test execution
- Reusable service-level endpoint patterns

## Tech Stack

- Python 3.11+
- pytest
- requests
- python-dotenv
- pytest-xdist (optional for parallel runs)
- Allure (optional, if added later by the team)

## Project Structure

```text
API-AUTOMATION/
├── .github/
│   └── workflows/
│       └── api-tests.yml
├── tests/
│   ├── api/
│   │   ├── test_posts_api.py
│   │   └── ...
│   ├── conftest.py
│   └── __init__.py
├── config/
│   ├── environments/
│   │   ├── dev.json
│   │   ├── qa.json
│   │   ├── uat.json
│   │   └── prod.json
│   ├── settings.py
│   └── __init__.py
├── src/
│   ├── api/
│   │   ├── clients/
│   │   ├── endpoints/
│   │   ├── payloads/
│   │   ├── validators/
│   │   └── auth/
│   ├── core/
│   │   ├── config.py
│   │   ├── logger.py
│   │   ├── exceptions.py
│   │   └── utils.py
│   ├── data/
│   │   ├── test_data.py
│   │   └── factories.py
│   └── __init__.py
├── .env.example
├── .gitignore
├── [pytest.ini](http://_vscodecontentref_/0)
├── [requirements.txt](http://_vscodecontentref_/1)
├── [README.md](http://_vscodecontentref_/2)
└── run_tests.py
```
