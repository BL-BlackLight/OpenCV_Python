import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
#cv.imshow('blank', blank)

# img = cv.imread('images/p1.jpg')
# # cv.imshow('image', img)
#painting a certain area:
#blank[200:300, 300:400] = 0,0,255
#cv.imshow('Red',blank)


#now drawing a rectangle:
cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=2,) #if we set { thickness=cv.FILLED or thickness=1 } then it will fill the rectangle with that given color
#cv.imshow('rectangle', blank)

# draw a square:
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
#cv.imshow('square', blank)

# draw a circle:
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=3)
#cv.imshow('circle',blank)

# draw a line:
cv.line(blank, (100,200), (300,400), (0,0,255), thickness=10)
#cv.imshow('line', blank)

# put a text:
cv.putText(blank, 'hello everyone', (100,490), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2, )
cv.imshow('text', blank)
cv.waitKey(0)
