## Imports
import cv2 
import uuid
import os, sys
import time

## Labels
from labels import labels as lb
labels = lb
number_imgs = 5 #Quantity of labelled images per label

## Setup folders
added_path = os.path.join('Tensorflow','workspace', 'images', 'collectedimages')
IMAGES_PATH = os.path.abspath(f"../../{added_path}")
print(IMAGES_PATH)

if not os.path.exists(IMAGES_PATH):
    if os.name == 'posix': #For Linux, not sure if it will work
        os.makedirs(IMAGES_PATH)
    if os.name == 'nt': #For Windows, not sure if it will work
        os.makedirs(IMAGES_PATH)
for label in labels:
    path = os.path.join(IMAGES_PATH, label) #Folders with labels as name
    if not os.path.exists(path):
        os.makedirs(path)

## Capture images
for label in labels:
    cap = cv2.VideoCapture(0) #Camera config
    print('Collecting images for {}'.format(label))
    time.sleep(5) #5 secs to initiate
    for imgnum in range(number_imgs):
        print('Collecting image {}'.format(imgnum))
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2) #2 seconds to take another photo

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()