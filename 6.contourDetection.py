import cv2 as cv
import numpy as np

img = cv.imread('images/p1.jpg')
# img = cv.resize(img, (300,300))
# cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)
#
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', img)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blured', blur)
#
# canny = cv.Canny(img, 125, 175)
# cv.imshow('canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

# cv.threshold :  separating objects from the background, creating masks, or preparing images for contour detection

# cv.THRESH_BINARY is a type of thresholding in OpenCV that converts an image into a binary image based on a specified threshold value

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')
# cv.findContours is an OpenCV function used to detect contours in a binary image. Contours are the boundaries or outlines of objects within an image, and they are extremely useful in tasks like shape analysis, object detection, and image recognition.

# cv.CHAIN_APPROX_NONE: Stores all contour points. This results in a more detailed contour.

# cv.CHAIN_APPROX_SIMPLE: Removes all redundant points and compresses the contour, storing only the endpoints of lines. This uses less memory and simplifies the contour data.

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('drawn contours', blank)
cv.waitKey(0)

