###



# DC motor blinking Tutorial 

# developed By Ashish vara
# Engineersgarage
 
import Adafruit_BBIO.GPIO as GPIO
 
import time
 
motor_p1 = "P8_8"
motor_n1 = "P8_9"
motor_p2 = "P8_10"
motor_n2 = "P8_11"
 
BUTTON = "P9_30"
 
GPIO.setup(motor_p1,GPIO.OUT)
GPIO.setup(motor_n1,GPIO.OUT)
GPIO.output(motor_p1, GPIO.LOW)
GPIO.output(motor_n1, GPIO.LOW)
GPIO.setup(motor_p2,GPIO.OUT)
GPIO.setup(motor_n2,GPIO.OUT)
GPIO.output(motor_p2, GPIO.LOW)
GPIO.output(motor_n2, GPIO.LOW) 
GPIO.setup(BUTTON,GPIO.IN)

def left_side_forward():
    #print "FORWARD LEFT"
    GPIO.output(motor_p2 , GPIO.HIGH)
    GPIO.output(motor_n2 , GPIO.LOW)
    time.sleep(1.05)
    GPIO.output(motor_p1 , GPIO.HIGH)
    GPIO.output(motor_n1 , GPIO.LOW)

def right_side_forward():
   #print "FORWARD RIGHT"
   GPIO.output(motor_p1 , GPIO.HIGH)
   GPIO.output(motor_n1 , GPIO.LOW)
   time.sleep(1.05)
   GPIO.output(motor_p2 , GPIO.HIGH)
   GPIO.output(motor_n2 , GPIO.LOW)

def forward():
   #print "FORWARD"
   GPIO.output(motor_p1 , GPIO.HIGH)
   GPIO.output(motor_n1 , GPIO.LOW)
   GPIO.output(motor_p2 , GPIO.HIGH)
   GPIO.output(motor_n2 , GPIO.LOW)

def left_side_reverse():
   #print "BACKWARD LEFT"
   GPIO.output(motor_p2 , GPIO.LOW)
   GPIO.output(motor_n2 , GPIO.HIGH)
   time.sleep(1.05)
   GPIO.output(motor_p1 , GPIO.HIGH)
   GPIO.output(motor_n1 , GPIO.LOW)

def right_side_reverse():
   #print "BACKWARD RIGHT"

   GPIO.output(motor_p2 , GPIO.LOW)
   GPIO.output(motor_n2 , GPIO.HIGH)
   time.sleep(1.25)
   GPIO.output(motor_p1 , GPIO.LOW)
   GPIO.output(motor_n1 , GPIO.HIGH)

def reverse():
   #print "BACKWARD"
   GPIO.output(motor_p1 , GPIO.LOW)
   GPIO.output(motor_n1 , GPIO.LOW)
   GPIO.output(motor_p2 , GPIO.LOW)
   GPIO.output(motor_n2 , GPIO.HIGH)

def stop():
   #print "STOP"
   GPIO.output(motor_p1 , GPIO.LOW)
   GPIO.output(motor_n1 , GPIO.LOW)
   GPIO.output(motor_p2 , GPIO.LOW)
   GPIO.output(motor_n2 , GPIO.LOW)

time.sleep(7)
forward()
time.sleep(1)
stop()
left_side_forward()
time.sleep(1)
stop()
forward()
time.sleep(1)
stop()
left_side_forward()
time.sleep(1)
stop()

while True:

      Button_State = GPIO.input (BUTTON)

      if Button_State == 1:
            right_side_reverse()
            time.sleep(1)
            stop()
            right_side_forward()
            time.sleep(1)
            stop()
            forward()
            time.sleep(1)
            stop()
            break   

      else:
            stop()

while True:

      Button_State = GPIO.input (BUTTON)

      if Button_State == 0: 
               right_side_forward()
               time.sleep(1)
               stop()
               break
      else:
               stop()
stop()