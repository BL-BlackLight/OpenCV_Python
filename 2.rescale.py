import cv2 as cv

img = cv.imread('images/p1.jpg')
cv.imshow('Product', img)

#this method is for saved videos or images:
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

#this method is to set resoulution while live video:
# def changeRes(width,height):
#     capture.set(3,width)
#     capture.set(4,height)
#

rescaled_img = rescaleFrame(img)
cv.imshow('rescaled image', rescaled_img)
cv.waitKey(0)
#playing video

capture = cv.VideoCapture('videos/car.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)


    if cv.waitKey(20) & 0xFF==ord('d'): #here, 0xFF==ord('d') forces the windows to be closed just after pressing 'd'
       break
capture.release()
cv.destroyAllWindows()
