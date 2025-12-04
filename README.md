# Selenium Python Work

This repository contains an example of a clean, maintainable UI test automation framework built with **Python, Selenium WebDriver**, and **Pytest**.
It demonstrates the **Page Object Model (POM)** pattern and includes automated tests for validating search functionality on **DuckDuckGo**.

## 🚀 Features

* **Python + Selenium WebDriver**
* **Pytest** as the test runner
* **Page Object Model (POM)** design
* **Config-driven browser setup**
* **Headless Chrome support**
* **Explicit & implicit waits**
* **Parallel test execution (pytest-xdist)**
* **HTML reporting (pytest-html)**

## 📁 Project Structure

selenium-python-work/\
│\
├── pages/\
│   ├── search.py               # DuckDuckGo search page object\
│   └── result.py               # Results page object\
│\
├── tests/\
│   └── test_search.py          # Parametrized UI tests\
│\
├── conftest.py                 # Fixtures: browser + config\
├── config.json                 # Browser settings\
└── README.md

## ⚙️ Installation
### 1. Clone the repository
**git clone** https://github.com/VitaliiKoliuka/selenium-python-work \
**cd** selenium-python-work

## 2. Create & activate a virtual environment
python -m venv .venv\
.venv\Scripts\activate   # Windows\
source .venv/bin/activate  # macOS / Linux\

## 3. Install dependencies

If your repo includes <ins>requirements.txt<ins>:

`pip install -r requirements.txt`

Minimum required packages:

selenium\
pytest\
pytest-html\
pytest-xdist

## 🛠️ Fix for Common Pytest Error

If you get this error:

ERROR: unrecognized arguments: --html=report.html --self-contained-html


It means the plugin pytest-html is not installed.

### ✅ Install required plugins
`pip install pytest-html`\
`pip install pytest-xdist`

(Parallel execution `-n 3` requires `pytest-xdist`.)

## 🧪 Running Tests
Standard run\
`pytest -v`

Run with parallel workers\
`pytest -n 3 -v`

Generate a self-contained HTML report\
`pytest -n 3 --html=report.html --self-contained-html`

## ⚙️ Browser Configuration
Modify the browser settings inside config.json:

{\
  "browser": "Headless Chrome",\
  "implicit_wait": 10\
}

Supported browsers:

"Chrome"\
"Firefox"\
"Headless Chrome"

## 🧩 Test Overview

`test_basic_duckduckgo_search` verifies:
* DuckDuckGo homepage loads
* Search phrase is submitted
* Search results contain titles related to the phrase
* Page title includes the searched text
* Input field retains the search value
  
All tests use Page Object Model for clean separation of concerns.

## 🧱 Page Objects
`DuckDuckGoSearchPage`
* Loads DuckDuckGo homepage
* Sends a search query

`DuckDuckGoResultPage`
* Waits for result links
* Extracts link titles
* Retrieves search input value
* Returns document title
