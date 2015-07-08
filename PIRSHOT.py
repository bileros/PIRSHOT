
import RPi.GPIO as GPIO
import time
import picamera

GPIO.setmode(GPIO.BCM)
GPIO_PIR = 4
GPIO.setup(GPIO_PIR,GPIO.IN)

Current_State  = 0
Previous_State = 0

try:

  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0

  print "  Ready"

  while True :

    Current_State = GPIO.input(GPIO_PIR)

    if Current_State==1 and Previous_State==0:
      print "  Motion detected!"
      with picamera.PiCamera() as camera:
          camera.resolution = (1920, 1080)
          camera.capture('../data/shot.jpg')
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      print "Ready"
      Previous_State=0

    time.sleep(0.01)

except KeyboardInterrupt:
  print "  Quit"

  GPIO.cleanup()
