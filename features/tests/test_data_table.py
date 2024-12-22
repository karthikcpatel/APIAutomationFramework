import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver

scenarios('test_data_table.feature')

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@given("I am on the form page")
def open_form_page(browser):
    browser.get("https://example.com/form")

@when("I fill in the form with the following details:")
def fill_form(browser, table):
    for row in table:
        field = row["field"]
        value = row["value"]
        input_box = browser.find_element("name", field)
        input_box.send_keys(value)

@then("the form should be submitted successfully")
def verify_submission(browser):
    submit_button = browser.find_element("name", "submit")
    submit_button.click()
    success_message = browser.find_element("id", "success-message")
    assert "Form submitted successfully!" in success_message.text
