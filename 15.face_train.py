#my code:
""""
import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

people = ['Alia Vhatt', 'Billie Ellish', 'Emma Watson', 'Kartik Aryan', 'Shruti Hassan', 'Sita Mahalaxmi']

# p = []
# for i in os.listdir(r'F:\Pycharm\OpenCV\faces') :
#     p.append(i)
# print(p)

DIR = r'F:\Pycharm\OpenCV\faces'
haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        #os.path.join: Combines the base directory DIR with each person folder name to form the full path.
        label = people.index(person)

    for img in os.listdir(path):
        img_path = os.path.join(path, img)
        img_array = cv.imread(img_path)
        if img_array is None:
            continue
        gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
        faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

        for(x,y,w,h) in faces_rect:
            faces_roi = gray[y:y+h, x:x+w]
            #roi provides the box length
            features.append(faces_roi)
            #Add the extracted face to the features list
            labels.append(label)
create_train()
print('training complete.....')

# print(f'lenghth of features: {len(features)}')
# print(f'length of labels: {len(labels)}')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create() # LBPH is a robust algorithm for facial recognition

#train the recognizer to feature and labels list:
face_recognizer.train(features, labels)
face_recognizer.save('faces_trained.yml')
np.save('features.npy',features)
np.save('labels.npy', labels)
"""






# pylint:disable=no-member

import os
import cv2 as cv
import numpy as np

people = ['Alia_Vhatt', 'Billie_Ellish', 'Emma_Watson', 'Kartik_Aryan', 'Shruti_Hassan', 'Sita_Mahalaxmi']
DIR = r'F:\Pycharm\OpenCV\faces'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            if img_array is None:
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y + h, x:x + w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print('Training done ---------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)


