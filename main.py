import os

import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgBackground = cv2.imread('Resources\\background.png')

Image_folder = 'C:\\Users\\test\\Desktop\\face recognition\\Resources\\Modes'
Images = os.listdir(Image_folder)
Imagelist = []

for path in Images:
    Imagelist.append(cv2.imread(os.path.join(Image_folder,path)))
print(len(Imagelist))

while True:
    success, img = cap.read()

    imgBackground[162:162+480,55:55+640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = Imagelist[2]
    #cv2.imshow("Webcam", img)
    cv2.imshow("Face attendance", imgBackground)
    cv2.waitKey(1)