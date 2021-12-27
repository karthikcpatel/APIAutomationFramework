import json

with open(r"C:\Miscellaneous\Software Testing Tutorials\Interview Questions & Answers\Miscellaneous Documents\samplejson.json") as file:
    file_dict = json.load(file)
    print(file_dict)
    file_list = file_dict['Geeks']
    for name in file_list:
        #print(name)
        if name['Geekname'] == "Pawan singh":
            assert name['subject'] == "Algorithms"
            print(name['subject'])