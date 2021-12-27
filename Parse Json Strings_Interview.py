import json

zipcode = '{"post code": "90210", "country": "United States", "country abbreviation": "US", "places": [{"place name": "Beverly Hills", "longitude": "-118.4065", "state": "California", "state abbreviation": "CA", "latitude": "34.0901"}]}'
dict_zipcode = json.loads(zipcode)
print(dict_zipcode)
list_places = dict_zipcode['places']
print(list_places)
dict_places = (list_places[0])
final_place = dict_places['place name']
print(final_place)