## Purpose: Tests for web aplication
## Project environment:  PageObject, Selenium, Python, Pytest, Allure
### Windows
1. Install project
2. Install all requirements from requirements.txt (pip install -r requirements.txt)
3. Start all tests from terminal "pytest -v tests -s --tb=line --reruns 1 --alluredir=data/allure-results"
4. Start mark tests from terminal "pytest -v -m "mark" -s --tb=line --reruns 1 --alluredir=data/allure-results"
5. Generate allure report "allure generate -c -o allure-reports data/allure-results/"
6. Open allure report, after generation, in browser allure-reports/index.html
