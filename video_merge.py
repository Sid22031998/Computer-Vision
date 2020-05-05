import cv2
import numpy as np

video1 = cv2.VideoCapture('output.avi')
video2 = cv2.VideoCapture('output1.avi')

while True:

	ret1, frame1 = video1.read()
	ret2, frame2 = video2.read()
	if ret1==False or ret2==False:
		break

	frame1=cv2.resize(frame1, (240,320))
	frame2=cv2.resize(frame2, (240,320))

	dst = cv2.addWeighted(frame1,0.3,frame2,0.7,0)
	cv2.imshow('dst',dst)
	key = cv2.waitKey(1)
	if key==ord('q'):
		break

cv2.destroyAllWindows()