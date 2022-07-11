from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from datetime import datetime
import time
from djitellopy import tello
me=tello.Tello()
me.send_read_command("command")
me.send_command_without_return("takeoff")
time.sleep(20)
me.send_command_without_return("land")