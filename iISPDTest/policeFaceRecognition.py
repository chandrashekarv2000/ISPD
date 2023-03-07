import numpy as np
import cv2
import face_recognition
import os
path="C://Users//Diwakar//PycharmProjects//ISPD//police"
images=[]
className=[]
myList=os.listdir(path)
name=""
for cls in myList:
    curImg=cv2.imread((f'{path}/{cls}'))
    images.append(curImg)
    className.append(os.path.splitext(cls)[0])
def findEncodings(images):
    encodeList=[]
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
def BoundingBox(img,encodeListKnown,name):
    imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    facesCurFrame = face_recognition.face_locations(imgs)
    encodeCurFrame = face_recognition.face_encodings(imgs, facesCurFrame)
    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = className[matchIndex]
            '''y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 240), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 240), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)'''
            if len(name)>0:
                return name
    cv2.destroyAllWindows()
    return "None"