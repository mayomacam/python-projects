#!/usr/bin/python3

import os
import requests

data = []

def final_lst(x): #get image lst
    final = []
    y = ".jpeg"
    for i in x:
            if y in i:
                 final.append(i)
                 
    return final


def feed():
    a = os.listdir("supplier-data/images/")
    path = "supplier-data/images/"
    ab = final_lst(a)
    for i in ab:
        print(i)
        with open(path+i, 'rb') as rf:
            response = requests.post("http://localhost/upload/", files={'file': rf})
            response.raise_for_status()
            print(response.request.url)
        #print(response.request.body)
            

feed()


