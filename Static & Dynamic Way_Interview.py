import json, requests

json_string = '{"post code": "90210", "country": "United States", "country abbreviation": "US", "places": [{"place name": "Beverly Hills", "longitude": "-118.4065", "state": "California", "state abbreviation": "CA", "latitude": "34.0901"}]}'
parse_json_string = json.loads(json_string)
print(parse_json_string)
dict_parse_json_string = parse_json_string['places']
print(dict_parse_json_string)
for x in dict_parse_json_string:
    if x['place name'] == "Beverly Hills":
        assert x['state'] == "California"

print("***************************************************************************************************************************")

with open(r"C:\Miscellaneous\Software Testing Tutorials\Interview Questions & Answers\Miscellaneous Documents\zippopotam.json") as file:
    kpdict = json.load(file)
    if kpdict['post code'] == "90210":
        assert kpdict['country'] == "United States"
    us_state = kpdict['places']
    for x in us_state:
        if x['place name'] == "Beverly Hills":
            assert x['state'] == "California"

print("***************************************************************************************************************************")

response = requests.get("https://api.zippopotam.us/us/90210")
response_dict = response.json()
print(response_dict)
usa_places = response_dict['places']
print(usa_places)
for actual in usa_places:
    if actual['place name']=="Beverly Hills":
        print(actual)

expected = {"place name":"Beverly Hills","longitude":"-118.4065","state":"California","state abbreviation":"CA","latitude":"34.0901"}
assert actual == expected

print("22th June, 2022")