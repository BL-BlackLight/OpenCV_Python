import cv2 as cv

img = cv.imread('images/p1.jpg')
cv.imshow('Product', img)

# grey effect on pic:
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey', grey)
#cv.cvtColor it converts an image from one color space to another and cv.COLOR_BG2GRAY is a color code just

# blur effect on pic:
blur = cv.GaussianBlur(img, (0,0), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)
#it helps to blur the pic,


# black sketch effect on pic ( Edge Cascade ) : a popular edge detection function
canny = cv.Canny(grey , 100, 255)
cv.imshow('canny', canny)

# dilated effect on pic : it just changes the light off the pic
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('dilated', dilated)

# eroded effect : lighter than dilated and canny, enhances the orginal pic
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('eroded', eroded)

# resizing :
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# cropping :
crop = img[50:200, 300:400]
cv.imshow('crop', crop)


cv.waitKey(0)