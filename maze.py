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
import time
from ourballdetection import *

#use physical pin numbering
GPIO.setmode(GPIO.BOARD)
counter = -1
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
            forward(20)
    if (distM < 5):
        reverse (20)
    stopall()
    time.sleep(.5)
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
def turnSharpLeft (TSleep, speed):
    turn(speed, 0)
    time.sleep(TSleep)
    stopall()
def TimetoCount():
    global counter 
    counter = counter + 1 
        

try:
    state = 0
    M = 20
    S = 15

    while (True):
        distM = getDistance(8,8)
        if (state == 0 and distM < 5):
	    OAS(M,S)
            state = 1
        elif (state == 0):
            stopall()
        if (state == 1):
            OAS(M,S)
	    TimetoCount()
	    if (counter is not 0):
		    distL = getDistance(18,22)
                    distM = getDistance(8,8)
                    distR = getDistance(12,13)
                    if (distR > distL):
                        turnRight(.5)
                    elif (distL > distR):
                        turnLeft(.5)    
	    if (counter == 0):
                result = findArrow()
                if result == 1:
                    print "red arrow found"
                    forward(20)
                    time.sleep(.5)
                    turnSharpLeft(.5, 50)
                    forward(20)
                    time.sleep(2)
                else:
                    distL = getDistance(18,22)
                    distM = getDistance(8,8)
                    distR = getDistance(12,13)
                    print "No arrow found"
                    if (distR > distL):
                        turnRight(.5)                  
                    elif (distL > distR):
                        turnLeft(.5)
		TimetoCount()           
        else:
            state = 0
    
        
    
except KeyboardInterrupt:
    GPIO.cleanup()

