import requests,json


data = requests.get('http://saral.navgurukul.org/api/courses').json()
with open("raja.json","w") as f:
    json.dump(data,f,indent=4)
    print("done")