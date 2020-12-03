#!/usr/bin/python3
import PIL
from PIL import Image
import os

#dir = "/home/mayomacam/Music/google-python/course6/week4/images/"
dir = "supplier-data/images/"
def list(): #get file lst
    #dir = "/home/mayomacam/Music/google-python/course6/week4/images/"
    lst = os.listdir(dir)
    return lst
    

def final_lst(x): #get image lst
    final = []
    y = ".tiff"
    for i in x:
            if y in i:
                 final.append(i)
                 
    return final


def pic(img): #all image related opertion 
    for i in img:
        im = Image.open(dir+i)
        #print(im.info) #give info.....
        if im.mode != 'RGB':
            im = im.convert('RGB')
        print(i)
        l = get_name(i)
        outfile = l + ".jpeg"
        #im.save(outfile)
        size = (600, 400)
        try:
            im.thumbnail(size)
            im.save(dir+outfile, "JPEG")
            #im.save("/home/mayomacam/Music/google-python/course6/week4/images/new/"+outfile, "JPEG")
        except OSError:
            print("cannot create thumbnail for", i)

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




file = list()
img = final_lst(file)
pic(img) #getting image work done
print(file)
print("\n\n-------------------------------------------------------------------\n")
print(img)
