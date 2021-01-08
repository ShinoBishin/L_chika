import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)

GPIO.output(23,GPIO.LOW)