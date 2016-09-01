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
from camera import *

#use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# main loop
#counter = -1 
def OAS(Mid_threshold, Side_Min):
    distL = getDistance(22,18)
    distM = getDistance(8,8)
    distR = getDistance(13,12)
    print distL, distM, distR
    
#    while (distM > Mid_threshold):
 #       distL = getDistance(22,18)
  #      distM = getDistance(8,8)
   #     distR = getDistance(13,12)

    if (distL < Side_Min):
        turnRight(.25)
	# was .25 
        print "turn right"
    elif (distR < Side_Min):
        turnLeft(.25)
        print "turn left"
    elif (distM < Mid_threshold):# delete the below block for running the while loop 
	stopall()
        if (distR > distL):
            turnRight(.25)
            distL = getDistance(18,22)
            distM = getDistance(8,8)
            distR = getDistance(12,13)
        elif (distL > distR):
            turnLeft (.25)
            distL = getDistance(18,22)
            distM = getDistance(8,8)
            distR = getDistance(12,13)
# //////////////////////////////////////
    else: 
        forward(30)
        print "forward"
   # stopall()
   # print "dead end" 

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

#def Counter():
 #   global counter
  #  counter += 1 
   # print counter
    #return counter 	

try:
    state = 0
    M= 20
    S = 15
    while (True):
        distM = getDistance(8,8)
        if (state == 0 and distM < M):
            state = 1
        elif (state == 0):
            stopall()
        if (state == 1):
            OAS(M,S)
#            turnCount = Counter()
 #           if (turnCount == 0 or turnCount == 3 or turnCount == 4 or turnCount == 5):
  #              turnRight(.25)
#		print "turning right"
 #           elif (turnCount == 1 or turnCount == 2):
  #              turnLeft(.25)
#		print "turning left"
        else:
            state = 0
	
        
    
except KeyboardInterrupt:
    GPIO.cleanup()

