from djitellopy import tello
from time import sleep
import cv2
me=tello.Tello()
me.connect()
me.streamon()
def pic():
    me.takeoff()
    count=0
    while True:
        img=me.get_frame_read().frame
        cv2.imshow("Image",img)
        cv2.waitKey(1)
        print(me.get_battery())
        if count==100000:
            break
        else:
            count=count+1
    me.land()


    return

pic()

