def ispd():
    import pyGames as kp
    import FaceRecognition as fr
    import violaJones as jones
    from djitellopy import tello
    import cv2
    import for_example1 as example
    from datetime import date
    sample=example.myresult[0][1]+str(example.myresult[0][0])
    pid,fbRange=[0.4,0.4,0],[6200,6800]
    pError,w,h=0,360,240
    tF=0
    a="None"
    manual,name=1,""
    temp,barometer=0,0
    encodeListKnown=fr.findEncodings(fr.images)
    print("Encoding complete")
    kp.init()
    me=tello.Tello()
    me.connect()
    me.streamon()
    frame_read=me.get_frame_read()
    height,width,_=frame_read.frame.shape
    video=cv2.VideoWriter('Videos//'+sample+'.avi',cv2.VideoWriter_fourcc(*'XVID'),70,(360,240))
    while True:
        v = kp.getKeyBoardInput(tF)
        if v[9]==1:
            temp=me.get_temperature()
            barometer=me.get_barometer()
            print("Temperature :",temp)
            print("Barometer :", barometer)
            print("battery", me.get_battery())
        if v[10]==1:
            ans=example.capture()
            capture = ans[0][1] + str(ans[0][0])
            cv2.imwrite('ispd_pictures//'+ capture + '.png', img)

        if v[7]:me.takeoff()
        if v[8]:me.land()
        if manual:
            val=kp.getKeyBoardInput(tF)
            if val[4]==1:
                print("saved video")
                video.release()
                break
            me.send_rc_control(val[0],val[1],val[2],val[3])
        img=cv2.resize(frame_read.frame,(360,240))
        if v[5]:
            tF,manual=1,0
            img, info = jones.findFace(img)
            pError,val1=jones.trackFace(info,w,pid,pError,fbRange)
            me.send_rc_control(val[0], val1[1], val[2], val1[3])
        else:
            manual,tF=1,0
        cv2.imshow("Intelligent Surveillance Patrolling Drone1", img)
        video.write(img)
        if v[6]:
            a= fr.BoundingBox(img, encodeListKnown,"")
            if a!="None":
                try:
                    pic = cv2.imread("Criminals/"+a+".jpeg")
                    cv2.imshow("criminal image", cv2.resize(pic,(500,500)))
                    result=example.criminal_details(a)
                    print("\n")
                    print("\t\t 1) CRIMINAL NAME " + result[0][0] + "\n \t\t 2) CRIMINAL AGE " + str(
                        result[0][1]) + "\n \t\t 3) CRIMINAL GENDER " + result[0][2] + "\n \t\t "
                                                                                       "4) NUMBER OF CRIMINAL CASES " + str(
                        result[0][3]) + "\n \t\t 5) CRIMINAL NUMBER " + str(
                        result[0][4]) + "\n \t\t 6) STATION NUMBER " + str(result[0][5]) + "\n"
                                                                                       " \t\t 7)STATION ID " + str(
                        result[0][6]) + "\n \t\t 8) CRIMINAL ID " + result[0][7])
                    print("\n")
                except:
                    pic = cv2.imread("Criminals/" + a + ".jpg")
                    cv2.imshow("criminal image", cv2.resize(pic,(500,500)))
                    result = example.criminal_details(a)
                    print("\n")
                    print("\t\t 1) CRIMINAL NAME "+result[0][0]+"\n \t\t 2) CRIMINAL AGE "+str(result[0][1])+"\n \t\t 3) CRIMINAL GENDER "+result[0][2]+"\n \t\t "
                    "4) NUMBER OF CRIMINAL CASES "+str(result[0][3])+"\n \t\t 5) CRIMINAL NUMBER "+str(result[0][4])+"\n \t\t 6) STATION NUMBER "+str(result[0][5])+"\n"
                    " \t\t 7)STATION ID "+str(result[0][6])+"\n \t\t 8) CRIMINAL ID "+result[0][7])
                    print("\n")
        cv2.waitKey(1)
    me.streamoff()
    cv2.destroyAllWindows()
    kp.quit()