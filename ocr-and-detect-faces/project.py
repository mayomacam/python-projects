import math
import zipfile
from zipfile import ZipFile
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')


file_name = "readonly/small_img.zip"


images=[]
namefile={}
with ZipFile(file_name, 'r') as zip: 
    for info in zip.infolist():
        with zip.open(info) as file:
            inf = info.filename
            print(inf)
            img = Image.open(file)
            print(img.size, img.mode, len(img.getdata()))
            #display(img)
            images.append(img)
            namefile[inf] = img

print(images)


text_data = []
image_to_run = []
def get_text(word):
    for i in images:
        text = pytesseract.image_to_string(i)
        text_data.append(text)
        if word in text:
            image_to_run.append(i)
word = input("Enter Word: ")
get_text(word)



print(image_to_run)

def get_faces(images):
    face_image=[]
    imag = np.array(images)
    gray = cv.cvtColor(imag, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for x,y,w,h in faces:
        face = images.crop((x,y,x+w,y+h))
        face_image.append(face)
    return face_image

print('done!')



def contact_images(images):
    a = get_faces(images)
    first_image=a[0]
    for faces in a:
        faces.thumbnail((100,100),Image.ANTIALIAS)
    h = math.ceil(len(a)/5)
    contact_sheet=Image.new('RGB',(500, 100*h))
    x=0
    y=0
    for img in a:
        contact_sheet.paste(img, (x, y) )
        if x+100 == contact_sheet.width:
            x=0
            y=y+100
        else:
            x=x+100
    display(contact_sheet)
print('done')


print(image_to_run)
#print('\n')
#print(namefile)
print('\n')
for i in image_to_run:
    #print(i)
    for j,k in namefile.items():
        if i == k:
            print("Result found in file {}".format(j))
    contact_images(i)





