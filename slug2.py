# from slug1 import course
# from slug import file
import slug
import slug1
import requests,json
from pprint import pprint

# file()
# course()


def slug_inf(lis,n):
    m=int(input("enter the slug no: "))
    z= requests.get(f"http://saral.navgurukul.org/api/courses/{n}/exercise/getBySlug?slug="+str(lis[m])).json()
    pprint(z)

n=int(input("Enter the id: "))
data1=requests.get(f"http://saral.navgurukul.org/api/courses/{n}/exercises").json()
pprint(data1)
with open("course.json","w") as f2:
    json.dump(data1,f2,indent=4)
    

def slug():
    with open("course.json","r") as f3:
        slug=json.load(f3)
        a=1
        b=[]
        for i in slug["data"]:
            print(a,i["slug"])
            a+=1
            b.append(i["slug"])
        slug_inf(b,n)


slug()

