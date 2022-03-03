import pyGames as kp
import  keyBoardControl as kb
def getKeyBoardInput(me):
    lr,fb,ud,yv=0,0,0,0

    speed=50
    if kp.getKey("LEFT"):        lr=-speed
    elif kp.getKey("RIGHT"):        lr=speed
    if kp.getKey("UP"):fb=speed
    elif kp.getKey("DOWN"):fb=-speed
    if kp.getKey("w"):ud=speed
    elif kp.getKey("s"):ud=-speed
    if kp.getKey("a"):yv=speed
    elif kp.getKey("c"):fb=-speed
    if kp.getKey("t"):me.takeoff()
    elif kp.getKey("l"):me.land()
    return [lr,fb,ud,yv]