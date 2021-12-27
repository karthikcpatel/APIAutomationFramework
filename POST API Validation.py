import requests, json

reponse = requests.post("https://reqres.in/api/users")
dict_response = reponse.json()
print(dict_response)

assert reponse.status_code == 201

assert reponse.headers['content-type'] == "application/json; charset=utf-8"

