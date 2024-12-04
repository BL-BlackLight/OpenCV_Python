import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

i = cv.imread('images/hog.jpg')
img = cv.resize(i, [500,700], interpolation=cv.INTER_CUBIC)
#cv.imshow('img', img)

blank = np.zeros((400,400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (20,20), (370,370), 255, -1)
# here pt1 denotes the pic's left upper point and pt2 denotes right lower point
#rectangle2 = cv.rectangle(blank.copy(), (30,30), (390,390), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
#circle2 = cv.circle(blank.copy(), (200,200), 100, 255, -1)
# cv.imshow('rectangle', rectangle)
# cv.imshow('circle', circle)
# #cv.imshow('rectangle2', rectangle2)
# #cv.imshow('circle2', circle2)

bit_and = cv.bitwise_and(rectangle,circle)
cv.imshow('and', bit_and)

bit_or = cv.bitwise_or(rectangle, circle)
cv.imshow('or', bit_or)

bit_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('xor', bit_xor)

bit_not = cv.bitwise_not(rectangle, circle)
cv.imshow('not', bit_not)


cv.waitKey(0)
cv.destroyAllWindows()