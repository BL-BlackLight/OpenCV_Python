import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

i = cv.imread('images/hog.jpg')
img = cv.resize(i, [500,700])
#cv.imshow('img', img)

blank = np.zeros(img.shape[:2], dtype='uint8')


circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)


wired_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('wired', wired_shape)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('mask', mask)

masked_img = cv.bitwise_and(img, img, mask=wired_shape)
cv.imshow('masked img', masked_img)

cv.waitKey(0)
cv.destroyAllWindows()

#(img.shape[1]//2, img.shape[0]//2) : here it outputs the center of the image ; 0 = height, 1 = width and ( //2 = divide by 2 and return integer value;)