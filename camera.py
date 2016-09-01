from picamera import PiCamera
from time import sleep

def DoILookPretty():
        camera = PiCamera()
        camera.start_preview()
        sleep(60)
        camera.stop_preview()
#try:
   #     while (True):
  #              DoILookPretty()
#
#except KeyboardInterrupt:
#        print "whoops"
