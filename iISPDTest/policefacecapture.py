def findFace(img):
    import cv2
    faceCascade=cv2.CascadeClassifier("C://Users//Diwakar//PycharmProjects//ISPD//haarcascade_frontalface_alt.xml")
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(imgGray,1.2,8)
    if faces!=():
        re ="yes"
    else:
        re= "no"
    return re
def findFace1(police_id):
    import cv2
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('img1', frame)
        ans = findFace(frame)
        if ans == "yes":
            break
        cv2.waitKey(1)
    cv2.imwrite('C://Users//Diwakar//PycharmProjects//ISPD//police//' + police_id + '.png', frame)
    cap.release()
    cv2.destroyAllWindows()
def choice1():
    import cv2
    import policeFaceRecognition as pfr
    encodeListKnown = pfr.findEncodings(pfr.images)
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        a = pfr.BoundingBox(frame, encodeListKnown, "")
        if a != 'None':
            x = [(2,)]
            break
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return x
