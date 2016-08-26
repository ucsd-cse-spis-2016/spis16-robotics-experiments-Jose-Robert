import RPi.GPIO as GPIO, time

# By default uses pin 8
#SonarMid = 8
def setupSonar():
   #use physical pin numbering
   GPIO.setmode(GPIO.BOARD)
   # Define Sonar Pin for Trigger and Echo to be the same
   #SONAR = sonarPin


def getDistance(trig, echo):

   GPIO.setup(trig, GPIO.OUT)
   GPIO.output(trig, True)
   time.sleep(0.00001)
   
   GPIO.output(trig, False)
   start = time.time()
   count = time.time()
   GPIO.setup(echo, GPIO.IN)
   
   while GPIO.input(echo)==0 and time.time()-count<0.1:
         start = time.time()
   stop=time.time()
   while GPIO.input(echo)==1:
         stop = time.time()
   # Calculate pulse length
   elapsed = stop-start
   # Distance pulse travelled in that time is time
   # multiplied by the speed of sound (cm/s)
   distance = elapsed * 34000
   # That was the distance there and back so halve the value
   distance = distance / 2
   return distance

def TestSonar ():
   setupSonar()
   while True:
      print "left" , str(getDistance(18, 22))
      print "Mid" , str(getDistance(8, 8))
      print "right" , str(getDistance(12, 13))
      time.sleep(1)
                        
                         
