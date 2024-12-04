import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/p1.jpg')
#cv.imshow('img',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked', masked)


# for grayscale img :
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])
#
# # plt.figure() #This ensures the histogram is plotted on a fresh canvas.
# # plt.title('calculate histogram')
# # plt.xlabel('Bins')
# # plt.ylabel('# of hist')
# # plt.plot(gray_hist) #Plots the histogram data (gray_hist)
# # plt.xlim([0,256]) #Sets the range of the x-axis to [0, 256]
# # plt.show()


# for colour image :
plt.figure() #This ensures the histogram is plotted on a fresh canvas.
plt.title('calculate histogram')
plt.xlabel('Bins')
plt.ylabel('# of hist')

colors = ('b', 'g', 'r')
for i,col in enumerate(colors) :
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)
cv.destroyAllWindows()