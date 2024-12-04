import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

i = cv.imread('images/hog.jpg')
img = cv.resize(i, [500,700])
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Laplacian:
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel :
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.Sobel(gray, cv.CV_64F, 1, 1)
combined_sobel2 = cv.bitwise_and(sobelx, sobely)
combined_sobel3 = cv.bitwise_or(sobelx, sobely)

cv.imshow('sobel x', sobelx)
cv.imshow('sobel y', sobely)
cv.imshow('c1', combined_sobel)
cv.imshow('c2', combined_sobel2)
cv.imshow('c3', combined_sobel3)

canny = cv.Canny(gray, 100, 200)
cv.imshow('canny', canny)

cv.waitKey(0)
cv.destroyAllWindows()