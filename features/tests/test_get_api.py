from pytest_bdd import scenario, given, when, then
from features.forms.test_steps import APIAutomation

api_automation = APIAutomation()

@scenario(r'get api.feature', 'Verify get requests')
def test_get_api_request():
    print("********** Scenario to verify get request from Zippopotam **********")

@given('user hits get request')
def user_hits_get_request():
    api_automation.get_request()
    print("Given got executed")

@when('user receives the response')
def user_receives_the_response():
    api_automation.request_successful()
    print("When got executed")

@then('the response should match')
def the_response_should_match():
    api_automation.validate_response()
    print("Then got executed")