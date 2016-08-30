# Pizazz Motor Test 
# Moves: Forward, Reverse, turn Right, turn Left, Stop - then repeat
# Press Ctrl-C to stop
#
# To check wiring is correct ensure the order of movement as above is correct
# Run using: sudo python motorTest.py
import RPi.GPIO as GPIO
import time
from sonar import *
from motor import *
from camera import *

#use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# main loop

def OAS(Mid_threshold, Side_threshold):
    distL = getDistance(18,22)
    distM = getDistance(8,8)
    distR = getDistance(12,13)

    while ((distL >  Side_threshold) and (distM > Mid_threshold) and (distR > Side_threshold)):
        forward (40)
        print "moving forward"
        distL = getDistance(18,22)
        distM = getDistance(8,8)
        distR = getDistance(12,13) 
        
        print distL
        print distM
        print distR
    else:
        while (distL < Side_threshold):
            turnRight(distL, Side_threshold)
            distL = getDistance(18,22)
            distM = getDistance(8,8)
            distR = getDistance(12,13)

        while (distR < Side_threshold):
            turnLeft(distR, Side_threshold)
            distL = getDistance(18,22)
            distM = getDistance(8,8)
            distR = getDistance(12,13)	
        while(distM < Mid_threshold):
            if (distR > distL):
                turnRight(distL, Side_threshold) 
                distL = getDistance(18,22)
                distM = getDistance(8,8)
                distR = getDistance(12,13)                 
            elif (distL > distR): 
                turnLeft (distR, Side_threshold)
                distL = getDistance(18,22)
                distM = getDistance(8,8)
                distR = getDistance(12,13)
	  # while (distR < Side_threshold):
	#	turnLeft(distR, Side_threshold)
	#	distR = getDistance(12,13)
        #       distL = getDistance(18,22)
        #       distM = getDistance(8,8)	

def turnRight (distL, Side_threshold):
    turn(5,50)
    time.sleep(.25)
    stopall()
    print "moving right"         

def turnLeft (distR, Side_threshold):
    turn(50, 5)
    time.sleep(.25)
    stopall()
    print "moving left" 
       	

try:
    while (True):
        setupSonar()
        #DoILookPretty()
        OAS(25, 15)
        
    
except KeyboardInterrupt:
    GPIO.cleanup()
