# Pizazz Motor Test 
# Moves: Forward, Reverse, turn Right, turn Left, Stop - then repeat
# Press Ctrl-C to stop
#
# To check wiring is correct ensure the order of movement as above is correct
# Run using: sudo python motorTest.py
import RPi.GPIO as GPIO
import time
from mysonar import *
from motor import *
import cv2
import picamera
import picamera.array
import time

#use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# main loop
#counter = -1 
def OAS(Mid_threshold, Side_Min):
    distL = getDistance(22,18)
    distM = getDistance(8,8)
    distR = getDistance(13,12)
    print distL, distM, distR
    
    while (distM > Mid_threshold):
        distL = getDistance(22,18)
        distM = getDistance(8,8)
        distR = getDistance(13,12)

        if (distL < Side_Min):
            turnRight(.25)
	# was .25 
            print "turn right"
        elif (distR < Side_Min):
            turnLeft(.25)
            print "turn left"
        else:
            forward(30)

    stopall()
    return 

def turnRight (TSleep):
    turn(0,20)
    time.sleep(TSleep)
    stopall()
    #print "moving right"         

def turnLeft (TSleep):
    turn(20, 0)
    time.sleep(TSleep)
    stopall()
    #print "moving left" 
 	

try:
    state = 0
    M= 15
    S = 15
    while (True):
        distM = getDistance(8,8)
        if (state == 0 and distM < M):
            state = 1
        elif (state == 0):
            stopall()
        if (state == 1):
            OAS(M,S)
            result =0
            with picamera.PiCamera() as camera:
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
                
            
                
                if numwhiteRedmask> redthresh:
                    result=1
                else:
                    result=0
       
            if result == 1:
                print "red arrow found"
                turnLeft(.25)
            else:
                distL = getDistance(18,22)
                distM = getDistance(8,8)
                distR = getDistance(12,13)
                print "No arrow found"
                if (distR > distL):
                    turnRight(.25)                  
                elif (distL > distR):
                    turnLeft(.25)           
        else:
            state = 0
	
        
    
except KeyboardInterrupt:
    GPIO.cleanup()

