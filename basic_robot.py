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

#use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# main loop


def sonar_test_01(threshold):
    distL = getDistance(18,22)
    distM = getDistance(8,8)
    distR = getDistance(12,13)

    while ((distL > threshold) and (distM > threshold) and (distR > threshold)):
        forward (40)
        print "moving forward"
        distL = getDistance(18,22)
        distM = getDistance(8,8)
  	distR = getDistance(12,13) 
        
        print distL
        print distM
        print distR
    else:
        while (distL < threshold):
            turnRight(distL, threshold)
            distL = getDistance(18,22)
	    print distL 

	while(distM < threshold):
	    if (distR > distL):
                turnRight(distL, threshold) 
        	distL = getDistance(18,22)
       		distM = getDistance(8,8)
        	distR = getDistance(12,13)                 
	    elif (distL > distR): 
                turnLeft (distR, threshold) 
                distL = getDistance(18,22)
                distM = getDistance(8,8)
                distR = getDistance(12,13)
	    while (distR < threshold):
		turnLeft(distR, threshold)
		distR = getDistance(12,13)
                distL = getDistance(18,22)
                distM = getDistance(8,8)	

def turnRight (distL, threshold):
    turn(0,50)
    time.sleep(1)
    stopall()
    print "moving right"         

def turnLeft (distR, threshold):
    turn(50,0)
    time.sleep(1)
    stopall()
    print "moving left" 
       	
            

try:
    while (True):
        setupSonar()
        sonar_test_01(25)
    
except KeyboardInterrupt:
    GPIO.cleanup()
