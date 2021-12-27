import requests, json
from utilities.configurations import *
from utilities.resources import *

url = get_config()['API']['endpoint_usa']
response = requests.get(url+'us/90210',verify=False)
response_dict = response.json()
print(response_dict)

print("*************************************************************************")

url = get_config()['API']['endpoint_usa']+APIResources.country+APIResources.zipcode
response = requests.get(url,verify=False)
response_dict = response.json()
print(response_dict)

print("****************************************************************************")

for endpoint in endpoints:
    print("Test for :-", endpoint)
    url = get_config()['API'][endpoint]+APIResources.api_resources.__getitem__(endpoint)
    response = requests.get(url,verify=False)
    response_dict = response.json()
    print(response_dict)

    print("Service Response:-", response.json())
    print("Expected Response:-", APIResources.expected_response.__getitem__(endpoint))

    assert response.json() == APIResources.expected_response.__getitem__(endpoint)