
# Enterprise UI Automation Framework - Books to Scrape

[![Playwright UI Automation CI](https://github.com/sourav-islam/enterprise-book-ui-automation-sourav/actions/workflows/playwright.yml/badge.svg)](https://github.com/sourav-islam/enterprise-book-ui-automation-sourav/actions/workflows/playwright.yml)

## Project Overview
This repository contains a production-ready, highly modular UI Automation Framework designed for the **Books to Scrape** sandbox platform. Built using **Python**, **Playwright**, and **Pytest**, this enterprise framework establishes industry-standard quality assurance metrics by evaluating front-end integrity, data state consistency across contextual views, multi-page layout traversing mechanisms, asset rendering accessibility parameters, and hypermedia status codes.

The solution is natively integrated into an automated cloud pipeline via **GitHub Actions** and supports dual reporting engines (**Pytest-HTML** and **Allure Reports**) for actionable engineering insights.

---

## Features
- **Page Object Model (POM):** Complete decoupling of underlying page selectors and interaction code from explicit assertion test logic.
- **Single-Responsibility Separation:** Modular test suites split across 5 individual domain files adhering to standard **SOLID** coding practices.
- **Advanced Network Handling:** Integrated enterprise proxy-bypass configurations with customized timeouts to guarantee execution stability under restrictive networks.
- **Auto-Waiting Synchronization:** Eliminates brittle, hardcoded `time.sleep()` blocks completely by using Playwright's native auto-waiting lifecycle and explicit DOM predicates.
- **Dynamic Data Validation:** Run-time subset extraction utilizing deterministic random samplings to guarantee wide regression coverage without exploding test runtimes.
- **Dual Reporting Layouts:** Seamless asset compilation into standalone, single-document static HTML pages as well as multi-dimensional Allure metric grids.

---

## Tech Stack
- **Core Engine:** Python 3.11 / 3.12
- **Automation Driver:** Playwright (Python Bindings)
- **Test Runner:** Pytest
- **Reporting Suites:** Pytest-HTML, Allure-Pytest, Urllib3
- **HTTP Engine:** Requests (for hypermedia scanning)
- **CI/CD Platform:** GitHub Actions

---

## Installation Guide

### Prerequisites
Ensure your local machine has Python installed (v3.11 or v3.12 recommended) and `pip` configured.

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sourav-islam/enterprise-book-ui-automation-sourav.git
   cd enterprise-book-ui-automation-sourav

```

2. **Initialize a Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install Requirements:**
```bash
pip install -r requirements.txt

```

---

## Environment Setup
Ensure your `pytest.ini` is present in the root folder to properly export your Python environment path namespace:

```ini
[pytest]
pythonpath = .
testpaths = tests

```

---

## Running Tests

You can execute the entire automated suite or pass specific configuration flags to isolate structural tests or view visual execution.

### Run All Tests (Headless Mode)

```bash
pytest -v

```

### Run Tests Visually (Headed Mode with Execution Slow Motion Delays)

```bash
pytest tests/test_image_validation.py --headed --slowmo 500

```

### Run a Single Target Test File Explicitly

```bash
pytest -v tests/test_homepage.py
pytest -v tests/test_broken_links.py

```

---

## Project Structure

```text
enterprise-book-ui-automation-sourav/
│
├── .github/
│   └── workflows/
│       └── playwright.yml       # Automated GitHub Actions Pipeline Workflow
│
├── pages/                       # Page Object Model Layer
│   ├── __init__.py
│   ├── base_page.py             # Global browser actions and explicit waits
│   ├── home_page.py             # Landing grid locators and pagination methods
│   └── product_page.py          # Detailed product view specifications
│
├── tests/                       # Modular Single-Responsibility Test Suites
│   ├── __init__.py
│   ├── conftest.py              # Centralized browser contexts and dynamic fixtures
│   ├── test_homepage.py         # Case 1: Structural landing layout checks
│   ├── test_navigation.py       # Case 2: Multi-view redirection path validation
│   ├── test_data_consistency.py # Case 3: Grid vs Details state text assertions
│   ├── test_broken_links.py     # Case 4: Hypermedia HTTP validation engine
│   └── test_image_validation.py # Case 5: Paginated media rendering checks
│
├── .gitignore
├── pytest.ini                   # Target runtime namespaces definitions
├── requirements.txt             # Framework ecosystem package mappings
└── README.md                    # Project Documentation

```

---

## Test Case Coverage

### Test Case 1: Homepage Validation (`tests/test_homepage.py`)

* Navigates to the platform base landing URL.
* Asserts explicit URL exact-match integrity and string headers.
* Iterates over all visible page heading hierarchies (`h1` through `h6`) ensuring none load blank text strings.
* Asserts visibility metrics and item populate count inside the main book grid catalog context.

### Test Case 2: Random Book Navigation (`tests/test_navigation.py`)

* Samples exactly 5 unique, randomly distributed book indicators across the initial viewport grid.
* Extracts item baseline structural references and performs click operations.
* Verifies that deep details view pages render correct specification profiles matching the correct book selection.

### Test Case 3: Book Data Consistency (`tests/test_data_consistency.py`)

* Tests data mapping across cross-functional viewport components.
* Extracts Title string text and Currency Prices directly from the grid interface card.
* Traverses into deep views to assert that deep page information matches surface metadata identically with zero data divergence.

### Test Case 4: Broken Link Validation (`tests/test_broken_links.py`)

* Extracts all explicit hypermedia link references (`href` attributes) across the DOM layout.
* Sanitizes and de-duplicates data points into unique target array indices.
* Dispatches fast HTTP requests (`HEAD` with fallback `GET`) to assert that all system paths return safe `HTTP 200 OK` responses.

### Test Case 5: Product Image Validation (`tests/test_image_validation.py`)

* Loops through paginated boundary containers up to exactly 5 consecutive result pages.
* Evaluates individual image attributes for every single item inside the catalog.
* Evaluates that `src` properties contain paths, `alt` descriptors contain accessible descriptive labels, and expected CSS structural class identifiers match specifications.

---

## Report Generation Guide

The framework is configured to produce detailed execution output formats simultaneously during execution.

### Execute and Capture Outputs Automatically

Run the following compilation command:

```bash
pytest --html=report.html --self-contained-html --alluredir=allure-results

```

---

## HTML Report Guide

The framework uses the `pytest-html` plugin to generate lightweight execution logs.

* **Local Viewing:** Open the root `report.html` file using any modern web browser.
* **Design Context:** The `--self-contained-html` command flag inline-injects all required cascading stylesheets (CSS) and assets straight into a single file document. This guarantees that reports open with zero rendering or font layout errors across any sharing channel.

---

## Allure Report Guide

Allure provides an interactive, rich graphical reporting dashboard that displays detailed execution timelines, step-by-step histories, and severity metrics.

1. **Compile & Server Local Dashboard:**
If you have the Allure CLI binaries installed on your workstation environment, launch the live tracking server:
```bash

allure serve allure-results

```


2. **Dashboard Review:** The command automatically opens a tab showing detailed test breakdowns, assertion exception messages, and test parameters.

---

## GitHub Actions Setup

The automated pipeline config file is located under `.github/workflows/playwright.yml`. It triggers on every code `push` or `pull_request` to the main repository development branch.

### Core CI Lifecycle Actions:

1. Provisions isolated environments running clean virtual machines (`ubuntu-latest`).
2. Configures a stable environment via Python standard setups.
3. Downloads specific runtime browser distributions (`playwright install chromium`).
4. Overrides environment network mappings (`HTTP_PROXY: ""`) to clear path traffic out of corporate network pipelines.
5. Generates the self-contained HTML report and saves it securely under the workflow run's **Artifacts** section for a 7-day retention period.
6. Automatically transforms raw JSON logs into web dashboard panels and deploys them live to the project’s **GitHub Pages** web portal branch (`gh-pages`).

---

## Design Decisions

* **Page Object Model (POM) Design Pattern:** Decoupling locator strings from test implementations prevents codebase breakage; if an HTML element class changes, it only needs to be updated once inside the Page class.
* **SOLID Design Principles (Single Responsibility):** Splitting the test suite across 5 granular test files rather than a single monolithic file avoids Git merge conflicts and allows developers to run targeted scopes.
* **Auto-Wait Sync Priority:** Eliminates brittle execution times by leveraging explicit selector states (`state="visible"`) to naturally follow application load speeds.
* **Environment Agnostic CLI Bindings:** Fixture factories utilize `request.config.getoption` lookups to handle visual debug loops seamlessly when CLI commands call for `--headed` or `--slowmo` steps.

---

## Known Limitations

* **External API Availability Dependencies:** `test_broken_links.py` performs external calls to live target endpoints. Occasional platform-side downtime or slow server responses from `books.toscrape.com` can induce false-negative network exceptions.
* **Single-Thread Browser Lock:** While playwright supports massive parallelization scaling out of the box via `pytest-xdist`, the randomized seed generator loops inside data integrity steps require single-thread state trackers to stay perfectly aligned across pagination jumps.
