import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)

lead_time = time.time()

data = []

while time.time() - lead_time < 10:
    data = []
    print(GPIO.input(17))
    time.sleep(0.5)
    data.append(GPIO.input(17))


for i in data:
    print(i)


GPIO.cleanup()