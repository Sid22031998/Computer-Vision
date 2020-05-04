import cv2, time
import numpy as np 

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("C:\\Users\\Sushim\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml")

a=1

while True:
	a=a+1
	check, frame = video.read()
	print(frame)
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors=5)
	
	for x,y,w,h in faces:
		gray  = cv2.rectangle(gray, (x,y), (x+w,y+h), (0,255,0),3)
	
	cv2.imshow('Capture',gray)
	key = cv2.waitKey(1)
	if key==ord('q'):
		break

print(a)

video.release()

cv2.destroyAllWindows()