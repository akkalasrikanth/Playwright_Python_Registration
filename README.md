# QA Automation Registration

## 1. Project Overview
This project is a Python-based UI automation framework for testing the registration flow of a web application using Playwright and Pytest. It validates page navigation, UI elements, input validation, registration behavior, and successful login flow.

The suite includes tests for:
- Home page UI checks
- Login page verification
- Product page interactions
- Registration page functionality
- Registration form data validation
- End-to-end registration flow coverage

## 2. Technologies Used
- Python 3
- Pytest
- Playwright for browser automation
- Page Object Model (POM)
- JSON for test data
- pytest-playwright plugin

## 3. Project Structure
```text
qa-automation-registration/
├── .venv/                        # Virtual environment
├── .pytest_cache/                # Pytest cache files
├── .playwright-mcp/              # Playwright-related metadata/logs
├── pages/                        # Page Object Model classes
│   ├── base_page.py
│   ├── cart_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── products_page.py
│   └── registration_page.py
├── tests/                        # Test suites
│   ├── test_home_page.py
│   └── ui/
│       ├── test_login.py
│       ├── test_products_page.py
│       ├── test_registration.py
│       └── test_registration_all.py
├── testData/                     # JSON test data files
│   └── registration.json
├── conftest.py                   # Shared fixtures and browser setup
├── pytest.ini                   # Pytest configuration
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
├── pytest-output.txt             # Captured pytest output
├── test_execution_report.txt     # Latest generated test execution report
└── .vscode/                      # Editor workspace settings
```

## 4. Installation Instructions
1. Open a terminal in the project root.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - Windows PowerShell:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - Windows Command Prompt:
     ```bat
     .\.venv\Scripts\activate.bat
     ```
4. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Install the Playwright browser binaries if they are not already installed:
   ```bash
   playwright install
   ```

## 5. Virtual Environment Activation (Windows)
Use the following commands depending on your shell:

PowerShell:
```powershell
cd D:\Projects\qa-automation-registration
.\.venv\Scripts\Activate.ps1
```

Command Prompt:
```bat
cd /d D:\Projects\qa-automation-registration
.\.venv\Scripts\activate.bat
```

If the script is blocked in PowerShell, run:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## 6. How to Execute All Tests
From the project root, activate the virtual environment and run:

```bash
pytest -q
```

Or using the Python interpreter directly:

```bash
python -m pytest -q
```

This runs the full project test suite across all test files.

## 7. How to Execute Individual Test Files
Run a specific test file by path:

```bash
pytest tests/ui/test_registration.py -q
```

Run a specific test module or file in the root tests folder:

```bash
pytest tests/test_home_page.py -q
```

Run a specific test by name:

```bash
pytest tests/ui/test_registration.py -k registration_page_ui -q
```

## 8. How to Generate and View Test Reports
This project supports standard pytest output generation and can also write a saved test execution summary report.

To generate console output only:
```bash
pytest -q
```

To save output to a file:
```bash
pytest -q > pytest-output.txt
```

To generate a saved pass/fail summary file:
```bash
python -m pytest -q > test_execution_report.txt
```

You can view the saved output/report files in the project root:
- pytest-output.txt
- test_execution_report.txt

To display the content of the report in the terminal:
```bash
type test_execution_report.txt
```

or:
```bash
Get-Content test_execution_report.txt
```

This project is configured to run browser automation tests with a headless Chromium instance via Playwright and a centralized fixture setup in conftest.py.
