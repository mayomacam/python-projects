#!/usr/bin/python3
import os
import requests
import re
data = []

def get_name(final):
    if type(final) is list:
        name = []
        for i in final:
            f,e = os.path.splitext(i)
            name.append(f)
        return name
    if type(final) is str:
        f, e = os.path.splitext(final)
        print(f)
        return f
        

def readfile():
    #ab = os.listdir("./test/")
    #path = "./test/"
    ab = os.listdir("supplier-data/descriptions/")
    path = "supplier-data/descriptions/"
    print(ab)
    for i in ab:
        print(i)
        dir={}
        with open(path+i, 'r') as rf:
            rf = rf.read().split("\n")[0:3]
            name, weight, description = rf
            j = get_name(i)
            dir["name"] = name.replace("\n", " ")
            dir["weight"] = int((re.search(r'\d+', weight)).group())
            dir["description"] = description.replace("\n", " ")
            dir["image_name"] = j+".jpeg"
        print(dir)
        data.append(dir)
    print(data)

def feed():
    for i in data:
        response = requests.post("http://localhost/fruits/", json=i)
        response.raise_for_status()
        print(response.request.url)
        print(response.request.body)
            
   
readfile()
feed()


