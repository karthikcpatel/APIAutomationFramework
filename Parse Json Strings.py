import json

courses = '{"name":"Kartik Patel","languages":["Java","Python"]}'
dict_courses = json.loads(courses)
print(dict_courses)
print(dict_courses['name'])
list_language = dict_courses['languages']
print(list_language)
print(list_language[1])