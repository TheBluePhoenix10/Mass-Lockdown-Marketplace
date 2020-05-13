import Adafruit_BBIO.PWM as PWM
import time
servoPin="P9_14"
PWM.start(servoPin,2,50)
#while(1):
time.sleep(3)
dutyCycle=1./18.*0 + 2
PWM.set_duty_cycle(servoPin,dutyCycle)
dutyCycle=1./18.*90 + 2
PWM.set_duty_cycle(servoPin,dutyCycle)
time.sleep(25)
dutyCycle=1./18.*0 + 2
PWM.set_duty_cycle(servoPin,dutyCycle)