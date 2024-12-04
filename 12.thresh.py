import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

i= cv.imread('images/hog.jpg')
img = cv.resize(i, [500,700])

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('simple thresh', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('threshold inverse', thresh_inv)

# Adaptive threshold:
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 0)
cv.imshow('adaptive threshold ', adaptive_thresh)

adaptive_guassian_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 0)
cv.imshow('adaptive GAUSIIAN threshold ', adaptive_guassian_thresh)


cv.waitKey(0)
cv.destroyAllWindows()