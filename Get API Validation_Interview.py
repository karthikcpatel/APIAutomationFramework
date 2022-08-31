import json, requests

response = requests.get("https://api.zippopotam.us/us/90210")
print(response)
print(response.text)
print(type(response.text))
response_dict = json.loads(response.text)
print(response_dict)
assert response.status_code == 200
assert response.headers['content-type']=='application/json'
print("**********************************************************************")
json_response = response.json()
print(json_response)
print(type(json_response))
print("Hello")