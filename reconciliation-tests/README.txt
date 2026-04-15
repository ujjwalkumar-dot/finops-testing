README — Playwright + Pytest Automation Setup

This project contains end-to-end automated tests for the Finance Ops
Pipeline & Reconciliation workflow using Python, Pytest, and Playwright.

The test suite includes: - Login automation - Pipeline creation - File
uploads - Column configuration - Field mapping - Pipeline execution -
Auto-handling refreshed pipelines - Support for dynamic pipeline
names/codes

1. System Requirements

Required Software: - Python 3.x - Node.js (only for npm scripts) -
Playwright (Python) - Playwright browsers - Git (optional)

2. Install Dependencies

Install Python dependencies: pip install pytest pip install
pytest-playwright pip install playwright

Install Playwright browsers: playwright install

3. Project Structure

. ├── new.py ├── TO_CREATE_PIPELINE.py ├── conftest.py ├── package.json
├── reconciliation-tests/ └── README.txt

4. Test Files Overview

new.py: Main E2E test conftest.py: pytest options package.json: npm
scripts

5. Required Test Files

C:-testsMicrosoft Excel Worksheet.xlsx C:-testsMicrosoft Excel
Worksheet - Copy.xlsx

6. Running the Tests

Option A – Using npm: npm run new npm run CP

Option B – Using pytest: pytest new.py -v pytest new.py -v
–pipeline_name TEST123 –pipeline_code PC001

Option C – Using python module: python -m pytest new.py -v

7. Authentication Notes

Email: vibhu@gmail.com Password: Test@123#

8. Common Issues & Fixes

-   Increase wait times if UI loads slowly
-   Ensure file paths exist for uploads
-   Update selectors after UI changes

9. Updating Pipeline Name/Code

pytest new.py -v –pipeline_name ABC –pipeline_code PC999

10. You’re Ready!

Run automated tests via: npm run new pytest new.py -v
