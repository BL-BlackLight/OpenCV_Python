import cv2 as cv

#reading image
img = cv.imread('images/p1.jpg') #cv.imread() it reads a file

cv.imshow('Product1', img) #cv.imshow() it show the file

cv.waitKey(0) #this fixes how many seconds we will see the image or video, putting 0 in it lets to see the file for infinite time

#playing video

capture = cv.VideoCapture('videos/car.mp4') #cv.VideoCapture() mainly captures videos from camera or file, cv2.VideoCapture(0) if we push 0 here then it will capture from the default camera...

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
       break
capture.release() #it releases all the frames and lets other videos to be captured
cv.destroyAllWindows() #lets close all the files correctly
