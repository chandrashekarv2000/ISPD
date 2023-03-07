import numpy as np
import cv2
def findFace(img):
    faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(imgGray,1.2,8)
    myFaceList=[]
    myFaceListArea=[]
    #for (x,y,w,h) in faces:
    if faces!=():
        x=faces[0][0]
        y=faces[0][1]
        w=faces[0][2]
        h=faces[0][3]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cx=x+w//2
        cy=y+h//2
        area=w*h
        cv2.circle(img,(cx,cy),5,(0,255,0),2)
        myFaceList.append([cx,cy])
        myFaceListArea.append(area)
    if len(myFaceListArea)!=0:
        i=myFaceListArea.index(max(myFaceListArea))
        return img,[myFaceList[i],myFaceListArea[i]]
    else:
        return img,[[0,0],0]

def trackFace(info,w,pid,pError,fbRange):
    area = info[1]
    x,y=info[0]
    fb=0
    error=x-w//2
    speed=pid[0]*error+pid[1]*(error-pError)
    speed=int(np.clip(speed,-50,50))
    if area > fbRange[0] and area< fbRange[1]:
        fb=0
    elif area > fbRange[1]:
        fb=-20
    elif area<fbRange[0] and area!=0:
        fb=20
    if x==0:
        speed=0
        error=0
    return error ,[0,fb,0,speed]