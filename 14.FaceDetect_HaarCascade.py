import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('images/people.jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# count face :
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 3)
print(f'number of the faces found {len(faces_rect)}')

# draw a rectangle over the face:
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 4)
cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()