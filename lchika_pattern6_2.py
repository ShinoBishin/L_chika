import wiringpi as pi
import time

blank_time = 10

led_pin = 23
sw_pin1 = 17
sw_pin2 = 27

pi.wiringPiSetupGpio()
pi.pinMode(led_pin, 1)

pi.pinMode(sw_pin1, 0)
pi.pinMode(sw_pin2, 0)
pi.pullUpDnControl(sw_pin1, 2)
pi.pullUpDnControl(sw_pin2, 2)

mode = 0
sw_mode = 1
data = [1, blank_time]

count = 0

while True:
    
    if (pi.digitalRead(sw_pin1) == 0):
        pi.digitalWrite(led_pin, 1)
        while(pi.digitalRead(sw_pin1) == 0):
            time.sleep(0.1)
    else:
        pi.digitalWrite(led_pin, 0)
        time.sleep(0.1)
