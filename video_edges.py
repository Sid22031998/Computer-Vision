import cv2
import numpy as np

video = cv2.VideoCapture(0)

key=1
while True:
	check, frame = video.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,100,200)

	key = cv2.waitKey(1)
	cv2.imshow('frame', edges)
	if key==ord('q'):
		break

video.release()

cv2.destroyAllWindows()