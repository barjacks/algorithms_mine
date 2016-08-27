import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

filename = "obama.jpg"

# Show the original image
img = cv2.imread(filename)

# Convert to grayscale, show it
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
	print('found a face')

cv2.destroyAllWindows()