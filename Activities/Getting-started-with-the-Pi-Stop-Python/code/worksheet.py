from RPi.GPIO import GPIO
import time

#Pins
RedLED = 26
AmberLED = 24
GreenLED = 22

GPIO.setup(RedLED, GPIO.OUT)
GPIO.setup(AmberLED, GPIO.OUT)
GPIO.setup(GreenLED, GPIO.OUT)

while True:

    GPIO.output(RedLED, True)
    GPIO.output(AmberLED, True)
    GPIO.output(GreenRED, True)

    time.sleep(1)

    GPIO.output(RedLED, False)
    GPIO.output(AmberLED, False)
    GPIO.output(GreenLED, False)

    time.sleep(1)
