import wiringpi as pi
import time

led = 23
cds = 17

pi.wiringPiSetupGpio()
pi.pinMode(led,1)
pi.pinMode(cds,0)

while True:
    if(pi.digitalRead(cds) == 1):
        pi.digitalWrite(led, 0)
    else:
        pi.digitalWrite(led, 1)

