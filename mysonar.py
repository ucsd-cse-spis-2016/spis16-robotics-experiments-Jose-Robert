import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BOARD)

def getDistance(echoPin=8, trigPin=8):

   GPIO.setup(trigPin, GPIO.OUT)
   GPIO.output(trigPin, True)
   time.sleep(0.00001)
   GPIO.output(trigPin, False)
   start = time.time()
   count = time.time()
   GPIO.setup(echoPin, GPIO.IN)
   while GPIO.input(echoPin)==0 and time.time()-count<0.1:
         start = time.time()
   stop=time.time()
   count = time.time()
   while GPIO.input(echoPin)==1 and time.time()-count<0.1:
         stop = time.time()
   # Calculate pulse length
   elapsed = stop-start
   # Distance pulse travelled in that time is time
   # multiplied by the speed of sound (cm/s)
   distance = elapsed * 34000
   # That was the distance there and back so halve the value
   distance = distance / 2
   return distance

