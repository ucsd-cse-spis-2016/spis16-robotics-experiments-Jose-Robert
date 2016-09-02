# This script is for continuous video capture
# In addition it uses opencv to transform
# the video frams to HSV and displays the video stream 
import cv2
import picamera
import picamera.array 
import time
import numpy as np

def nothing(x):
    pass


RedH_low, RedS_low, RedV_low = 109, 185, 82
RedH_high, RedS_high, RedV_high = 255, 255, 255
redthresh = 1500
#BlackH_low, BlackS_low, BlackV_low = 85, 83, 9
#BackH_high, BlackS_high, BlackV_high = (BlackH_low + 100), (BlackS_low + 100), (BlackV_low + 100)
img_low = np.zeros((15,512,3),np.uint8)

def findArrow():
        with picamera.PiCamera() as camera:
            camera.vflip = True
            camera.resolution=(640,480)
            camera.framerate = 32


            with picamera.array.PiRGBArray(camera, size=(640,480)) as stream:

                #capture to stream for use with opencv
                camera.capture(stream, format='bgr')
                image = stream.array
                hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

                # define the range of the blue color in hsv
                lower_Red = np.array([RedH_low, RedS_low, RedV_low])
                upper_Red = np.array([255, 255, 255])
                #  lower_Black = np.array([BlackH_low, BlackS_low, BlackV_low])
                # upper_Black = np.array([BackH_high, BlackS_high, BlackV_high])
                    
                # Threshold the hsv image to get only blue colors
                Redmask = cv2.inRange(hsv, lower_Red, upper_Red)
                # show the frame
                #cv2.imshow("Frame", image)
                #cv2.imshow("RedMask", Redmask)
                numwhiteRedmask = cv2.countNonZero(Redmask)
                print numwhiteRedmask
                    
                #Blackmask = cv2.inRange(hsv, lower_Black, upper_Black)
                    
                if numwhiteRedmask> redthresh:
                    return 1
                else:
                    return 0

##result = findArrow()
##if result == 1:
##    print "red arrow found"
##             
##else:       
##    print "No arrow found"


