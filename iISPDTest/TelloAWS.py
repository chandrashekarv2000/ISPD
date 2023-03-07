import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import time
import json
import sys
import ast
from datetime import datetime
from djitellopy import tello
ENDPOINT="a1js75eqrqf7rt-ats.iot.ap-south-1.amazonaws.com"
CLIENT_ID="Test-Thing"
PATH_TO_CERTIFICATE="iot-test-publish/certificates/12f93d6e44b4d7ab8b75f8508205c80d583f54da5f3f1f3bb3a9f870b54cf912-certificate.pem.crt"
PATH_TO_PRIVATE_KEY="iot-test-publish/certificates/12f93d6e44b4d7ab8b75f8508205c80d583f54da5f3f1f3bb3a9f870b54cf912-private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1="iot-test-publish/certificates/AmazonRootCA1.pem"
TOPIC="test/testing"
RANGE=20

myAWSIoTMQTTClient=AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT,8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_AMAZON_ROOT_CA_1,PATH_TO_PRIVATE_KEY,PATH_TO_CERTIFICATE)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)
myAWSIoTMQTTClient.configureDrainingFrequency(2)
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)
myAWSIoTMQTTClient.connect()
me=tello.Tello()
def answer(a):
      b = a.split("\\")
      c = b[1].split()
      try :
            d,e = c[2],c[3]
            return d+" "+e
      except IndexError:
            return c[2]
def customCallback(client,userdata,message):
      a=str(message.payload)
      ans=answer(a)
      if ans=="battery":
           bat=me.get_battery()
           print(bat)
      else:
            me.send_control_command(ans)

myAWSIoTMQTTClient.subscribe(TOPIC,1,customCallback)
while True:
      time.sleep(1)