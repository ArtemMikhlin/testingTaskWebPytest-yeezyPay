## Purpose: Tests for web aplication
## Project environment:  PageObject, Selenium, Python, Pytest, Allure
### Windows
 Install project
 Install all requirements from requirements.txt (pip install -r requirements.txt)
 Start all tests from terminal "pytest -v tests -s --tb=line --reruns 1 --alluredir=data/allure-results"
 Start mark tests from terminal "pytest -v -m "mark" -s --tb=line --reruns 1 --alluredir=data/allure-results"
 Generate allure report "allure generate -c -o allure-reports data/allure-results/"
 Open allure report, after generation, in browser allure-reports/index.html
