import requests
from utilities.configurations import *
from utilities.resources import *
from features.utils import utils as utils

class APIAutomation:

    def __init__(self):
        print("Constructor got initialized")

    def get_request(self):
        global response, endpoint
        for endpoint in endpoints:
            print("Test for :-", endpoint)
            #url = "https://api.zippopotam.us/us/90210"
            #url = get_config()['API']['endpoint_usa'] + APIResources.country+APIResources.zipcode
            #url = get_config()['API'][endpoint] + APIResources.api_resources.__getitem__(endpoint)
            url = utils.endpoint + APIResources.api_resources.__getitem__(endpoint)
            response = requests.get(url, verify=False)
            response_dict = response.json()
            print(response_dict)

    def request_is_successful(self):
        response_code = response.status_code
        if response_code == 200:
            return True
        else:
            return False

    def validate_response(self):
        actual = response.json()
        print(actual)
        expected = APIResources.expected_response.__getitem__(endpoint)
        print(expected)
        assert actual == expected