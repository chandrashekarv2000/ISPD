import cv2
cap=cv2.VideoCapture(0)
re="yes/no"
def findFace(img):
    faceCascade=cv2.CascadeClassifier("C:\\Users\\cs_loneranger_\\Downloads\\haarcascade_frontalface_alt.xml")
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(imgGray,1.2,8)
    if faces!=():
        re ="yes"
    else:
        re= "no"
    return re
while True:
    ret, frame = cap.read()
    cv2.imshow('img1',frame)
    ans=findFace(frame)
    if ans=="yes":
        cv2.imwrite('C://Users//cs_loneranger_//OneDrive//Desktop//police//c1.png',frame)
        cv2.destroyAllWindows()
        break
    cv2.waitKey(1)
cap.release()