
#!/usr/bin/python

# Import required Python libraries
import RPi.GPIO as GPIO
import time
import picamera
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_PIR = 7

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)

Current_State  = 0
Previous_State = 0

try:

  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0

  print "  Ready"

  # Loop until users quits with CTRL-C
  while True :

    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)

    if Current_State==1 and Previous_State==0:
      # PIR is triggered
      print "  Motion detected!"
      with picamera.PiCamera() as camera:
          camera.resolution = (640, 480)
          camera.capture('../data/image.jpg')
      # Record previous state
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
      print "Ready"
      Previous_State=0

    # Wait for 10 milliseconds
    time.sleep(0.01)

except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()
