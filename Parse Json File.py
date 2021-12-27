import json

with open(r"C:\Miscellaneous\Software Testing Tutorials\Interview Questions & Answers\Miscellaneous Documents\samplejson.json") as file:
    file_dict = json.load(file)
    print(file_dict)
    file_geek = file_dict['Geeks']
    print(file_geek)
    file_list = file_geek[1]
    print(file_list)
    geek_name = file_list['Geekname']
    print(geek_name)