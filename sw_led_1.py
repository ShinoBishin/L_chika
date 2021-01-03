import wiringpi as pi
import time
inv_time = 1
led_L = 23
led_R = 24
sw = 25

pi.wiringPiSetupGpio()
pi.pinMode(led_L,1)
pi.pinMode(led_R,1)
pi.pinMode(sw,0)

light = 0

while True:
    pi.digitalWrite(led_L,0)
    pi.digitalWrite(led_R,0)

    while(pi.digitalRead(sw) == 1):
        if(light == 0):
            pi.digitalWrite(led_L,1)
            pi.digitalWrite(led_R,0)
            light = 1
        else:
            pi.digitalWrite(led_L,0)
            pi.digitalWrite(led_R,1)
            light = 0
        time.sleep(inv_time)