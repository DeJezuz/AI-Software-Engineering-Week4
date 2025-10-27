# Week 4 — AI in Software Engineering

## Overview
This repository contains the Week 4 assignment focused on building intelligent software solutions using AI. It includes theoretical analysis, practical implementations, and ethical reflections.

## Repository Structure
- `code/`  
  Contains all task scripts:  
  - `task1_sorting.py` and `task1_sorting_manual.py` (sorting implementations)  
  - `task1_tests.py` (unit tests for Task 1)  
  - `task2_selenium_login.py` (automated login tests)  
  - `task3_predictive.py` (predictive analytics demo)  
- `report/`  
  - `week4_report.md` (assignment report)  
  - `figures/` (screenshots and generated images)  
- `docs/`  
  - `theoretical_answers.md`  
  - `bonus_proposal.md`  
- `.gitignore`  
- `requirements.txt`  
- `ci/`
  - `python-app.yml`

## Setup Instructions
```bash
git clone <your-repo-url>
cd <repo-folder>
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
pip install -r requirements.txt

Running the Tasks
Task 1: Sorting Tests
python code/task1_tests.py

Task 2: Automated Login Tests

Note: Update LOGIN_URL, selectors, and credentials in code/task2_selenium_login.py before running.

python code/task2_selenium_login.py

Task 3: Predictive Analytics
python code/task3_predictive.py

Generating the Report PDF

Convert the markdown report to PDF using:

pandoc report/week4_report.md -o report/week4_report.pdf


Or print to PDF from any Markdown viewer.

Notes
Task 3 uses a synthetic 3-class priority mapping for demonstration; this is documented in the report.
Selenium tests require proper configuration of URL and selectors.
Placeholder images are included in report/figures/ if Selenium tests were not run.
License

Add a LICENSE file if you wish to specify reuse terms.

Prepared for Week 4 AI in Software Engineering Assignment.
