import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	img = frame.copy()

	cv2.imshow("Image", img)
		
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
