# Pizazz Motor Test
# Moves: Forward, Reverse, turn Right, turn Left, Stop - then repeat
# Press Ctrl-C to stop
#
# To check wiring is correct ensure the order of movement as above is correct
# Run using: sudo python motorTest.py
import RPi.GPIO as GPIO, time
from sonar import *
from motor import *

#use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# main loop


def sonar_test_01(threshold):
    dist = getDistance()
    for i in range (10):
        while (dist > threshold):
            forward (40)
            print "moving forward"
            dist = getDistance()
            print dist
        else:
            turn(0,50)
            print "moving right"
            dist = getDistance()
            print dist
            

try:
    setupSonar(sonarPin = 8)
    sonar_test_01(30)
    
except KeyboardInterrupt:
    GPIO.cleanup()
