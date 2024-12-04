import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

i = cv.imread('images/hog.jpg')
img = cv.resize(i, (500,700), interpolation=cv.INTER_CUBIC)
cv.imshow('image', img)
#pixel = img[100,100]
#print(pixel)
# print(pixel): This prints the intensity value(s) of the accessed pixel.

#channels:
b, g, r = cv.split(img) #split separates the image into 3 channels blue, green and red

blank = np.zeros(img.shape[:2], dtype='uint8') #img.shape has 3 value but now we only give blank img the height and width , so we put img.shape[:2]

cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
# shape provides height, width and channels
merged = cv.merge([b, g, r])
cv.imshow('merged', merged)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue 2', blue)
cv.imshow('green 32', green)
cv.imshow('red 2', red)
#color speces:
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

cv.waitKey(0)
cv.destroyAllWindows()

