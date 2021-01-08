#!/usr/bin/python3
import PIL
from PIL import Image
import os

def list(): #get file lst
    dir = os.getcwd()
    lst = os.listdir(dir)
    return lst
    

def final_lst(x): #get image lst
    final = []
    y = {'.png','.jpg'}
    for i in x:
        for j in y:
            if j in i:
                final.append(i)
                 
    return final


def pic(img): #all image related opertion 
    p = input("enter option between convert or rr (rotate and resize) or thumbnail : " )
    for i in img:
        im = Image.open(i)
        print(im.info) #give info.....
        if im.mode != 'RGB':
            im = im.convert('RGB')
        if p == "convert" :
            l = get_name(p)
            outfile = l + ".jpg"
            im.save(outfile)
        if p == "rr":
            if '.png' in i:
                im.resize((400,600)).save("1"+i, "PNG")
            if '.jpg' in i:
                im.resize((400,600)).save("1"+i, "JPEG")
            
        if p == "thumbnail":
            l = get_name(i)
            #outfile = l + ".thumbnail"
            outfile = l 
            size = (128, 128)
            try:
                im.thumbnail(size)
                #im.save("/abc/"+outfile, "JPEG")
                im.save("2"+outfile, "JPEG")
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
print(file)
print("\n\n-------------------------------------------------------------------\n")
print(img)
pic(img) #getting image work done
#print(file)

#print(img)

