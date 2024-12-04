import cv2 as cv
import numpy as np

img = cv.imread('images/eye.jpg')

cv.imshow('eye', img)

# translation: (mainly moves the pic depending on x, y value
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]]) #transformation matrix
    dimensions = (img.shape[1], img.shape[0]) #here dimensions reffers to the size width, height...
    return cv.warpAffine(img, transMat, dimensions)
# The cv.warpAffine function is used to apply a 2D affine transformation to an image. This transformation can include translations, rotations, scaling, shearing, or any combination of these, depending on the transformation matrix provided.

# -x = left
# -y = up
# x = right
# y = down

translated = translate(img, -100, -100)
#cv.imshow('Translated', translated)

# Rotation : (it will rotate the pic)
def rotate(img, angle, rotPoint:None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45, None)
cv.imshow("rotated", rotated)
r_rotated = rotate(rotated, 45, None)
cv.imshow("double rotation",r_rotated)

# Resizing :
resized = cv.resize(img, (1260, 720), interpolation=cv.INTER_LINEAR)
cv.imshow('resized', resized)

# flipping:
flip = cv.flip(img, 0)
cv.imshow('flipped', flip)
#here flipCode:0 , flipps the pic vertically , 1 flipps the pic horizontally and -1 flipps it in both

# Cropping :
cropped = img[100:200, 300:400]
cv.imshow('cropped', cropped)
cv.waitKey(0)



