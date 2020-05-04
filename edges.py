import cv2
import numpy as np

img = cv2.imread('SIDDHARTH SINGH_UEM.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,200)
key=1
while key:
	key = cv2.waitKey(1)
	cv2.imshow('frame', edges)
	if key==ord('q'):
		break
