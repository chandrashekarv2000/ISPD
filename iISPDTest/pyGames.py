import pygame
def init():
    pygame.init()
    win=pygame.display.set_mode((300,300))

def getKey(keyName):
    ans=False
    for eve in pygame.event.get():pass
    keyInput=pygame.key.get_pressed()
    myKey=getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans=True
    pygame.display.update()
    return ans
def getKeyBoardInput(tF):
    lr,fb,ud,yv,mT,t,l,Break,a,c=0,0,0,0,0,0,0,0,0,0
    speed=100
    if getKey("LEFT"):lr=-speed
    elif getKey("RIGHT"):lr=speed
    if getKey("UP"):fb=speed
    elif getKey("DOWN"):fb=-speed
    if getKey("w"):ud=speed
    elif getKey("s"):ud=-100
    if getKey("a"):yv=-speed
    elif getKey("c"):yv=speed
    if getKey("t"):t=1
    elif getKey("l"):l=1
    if getKey("q"):Break=1
    if getKey("f"): tF=1
    elif getKey("k"):tF=0
    if getKey("m"): mT=1
    if getKey("b"): a = 1
    if getKey("v"): c = 1
    return [lr,fb,ud,yv,Break,tF,mT,t,l,a,c]