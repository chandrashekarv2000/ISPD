import pyGames as kp
from djitellopy import tello
import cv2
from time import sleep
kp.init()
me=tello.Tello()
me.connect()
print("battery",me.get_battery())
me.streamon()

def getKeyBoardInput():
    lr,fb,ud,yv,Break=0,0,0,0,0
    speed=50
    if kp.getKey("LEFT"):        lr=-speed
    elif kp.getKey("RIGHT"):        lr=speed
    if kp.getKey("UP"):fb=speed
    elif kp.getKey("DOWN"):fb=-speed
    if kp.getKey("w"):ud=speed
    elif kp.getKey("s"):ud=-speed
    if kp.getKey("a"):yv=speed
    elif kp.getKey("c"):yv=-speed
    if kp.getKey("t"):me.takeoff()
    elif kp.getKey("l"):me.land();sleep(3)
    if kp.getKey("q"):Break=1
    return [lr,fb,ud,yv,Break]
frame_read=me.get_frame_read()
height,width,_=frame_read.frame.shape
video=cv2.VideoWriter('C://Users//cs_loneranger_//Videos//Captures//Totorial1.avi',cv2.VideoWriter_fourcc(*'XVID'),30,(width,height))
while True:

    val=getKeyBoardInput()
    if val[4]==1:
        video.release()
        print("saved video")
        break
    me.send_rc_control(val[0],val[1],val[2],val[3])
    img=frame_read.frame
    img=cv2.resize(img,(360,240))
    cv2.imshow("img",img)
    video.write(img)
    cv2.waitKey(1)
video.release()
me.streamoff()