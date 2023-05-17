import uuid
import os
import time
import cv2

labels = ["glass","laptop","phone","Nagisa","Abhinav"]
num_images = 10

PATH = os.path.join("Tensorflow","Images","Collected_Images")

'''if not os.path.exists(PATH):
    if os.name == 'posix':
        os.system("mkdir -p {PATH}")
    if os.name == 'nt':
        os.system("mkdir " + PATH)

for label in labels:
    label_path = os.path.join(PATH,label)
    if not os.path.exists(label_path):
        os.system("mkdir "+ label_path)

#get actuall data
for label in labels:
    camera = cv2.VideoCapture(0)
    print('Collecting Image for ' + label + '\n')
    time.sleep(5)
    for i in range(num_images):
        print("Collecting Image for image: " + str(i))
        ret, frame = camera.read() #reads
        imagePath = os.path.join(PATH,label,str(uuid.uuid1()) +  "." + "jpg")
        print(imagePath)
        cv2.imwrite(imagePath,frame)
        cv2.imshow('frame',frame)
        print("3 seconds before the next picture is taken")
        time.sleep(3)

camera.release()
cv2.destroyAllWindows()'''

LABELPATH = os.path.join("Tensorflow","labelling")

if not os.path.exists(LABELPATH):
    os.system("mkdir " + LABELPATH)
    os.system("git clone https://github.com/heartexlabs/labelImg" + LABELPATH)

