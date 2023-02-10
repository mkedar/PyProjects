import numpy as np
import cv2

fire_cascade = cv2.CascadeClassifier('fire_cascade.xml')

#8/15/22

capture = cv2.VideoCapture(0)

while(True):
    ret, FireFinder = capture.read()
    gray = cv2.cvtColor(FireFinder, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(FireFinder, 1.2, 5)

    for (x,y,w,h) in fire:
        cv2.rectangle(FireFinder,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = FireFinder[y:y+h, x:x+w]
        print("Fire detected")


    cv2.imshow('FireFinder', FireFinder)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
