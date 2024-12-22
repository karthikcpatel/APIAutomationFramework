import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver

scenarios('test_example.feature')

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@given("I am on the Google search page")
def open_google(browser):
    browser.get("https://www.google.com")

@when('I search for "<search_term>"')
def search_term(browser, search_term):
    search_box = browser.find_element("name", "q")
    search_box.send_keys(search_term)
    search_box.submit()

@then('the title should contain "<expected_result>"')
def verify_title(browser, expected_result):
    assert expected_result in browser.title
