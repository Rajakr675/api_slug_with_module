import json


with open("raja.json","r") as f1:
    data=json.load(f1)
    for i in data["availableCourses"]:
        print(i["id"],i["name"])