import wiringpi as pi
import time
inv_time = 1
led_L = 23
sw = 17

pi.wiringPiSetupGpio()
pi.pinMode(led_L,1)
pi.pinMode(sw,0)
pi.pullUpDnControl(sw, PUD_DOWN)

light = 0

while True:
    pi.digitalWrite(led_L,0)

    while(pi.digitalRead(sw) == 1):
        if(light == 0):
            pi.digitalWrite(led_L,1)
            light = 1
        else:
            pi.digitalWrite(led_L,0)
            light = 0
        time.sleep(inv_time)