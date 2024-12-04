import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

i = cv.imread('images/hog.jpg')

img = cv.resize(i, [500,700], interpolation=cv.INTER_CUBIC)
cv.imshow('img', img)

average = cv.blur(img, (7,7))
cv.imshow('average blur', average)

gauss = cv.GaussianBlur(img, (7,7), 0) #overall blurr kinda
cv.imshow('gaussian blur', gauss)

median = cv.medianBlur(img, 7) #bllurry + magic effect , kinda clear
cv.imshow('median blur', median)

billa = cv.bilateralFilter(img, 9, 75, 75) #provides clear but cartoon type magic effect
cv.imshow('bilaterial blur', billa)

cv.waitKey(0)
cv.destroyAllWindows()