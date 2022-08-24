### References

1) Generate allure reports using below commands:
    a) python -m pytest --alluredir=reports/allure-reports
    b) allure serve reports/allure-reports

2) Pytest commands
pytest: to run all test cases
pytest -v: v stands for verbose that shows more information
pytest '.py file name' to run a specific python file
pytest -k creditcard -v -s: to run all tests based on specific keyword
pytest --html=reports/report.html --self-contained-html: to generate html reports in pytest

#24th August, 2022