#切り替えスイッチなしver.

import RPi.GPIO as GPIO
import time

# デバイスの接続先
led = 23
btn1 = 17

# GPIOの初期化
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(btn1, GPIO.IN)

# 時間計測用変数
lead_time = time.time()

# btn2の入力により記録モード、入力モードを切り替える
count = 0
data = []


#　スタンバイモード
def ready():
    num = 0
    while (num <= 1):
        GPIO.output(led, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led, GPIO.LOW)
        time.sleep(1)
        num = num + 1

#　記録モード
def btn_read():
    while time.time() - lead_time < 10:
        data.append(GPIO.input(btn1))
        time.sleep(0.1)
    


# 点灯モード
def led_on():
    for i in data:
        time.sleep(0.1)
        if(i == 1):
            GPIO.output(led,GPIO.HIGH)
        else:
            GPIO.output(led,GPIO.LOW)


ready()
btn_read()
print("入力モード終了")
time.sleep(1)
led_on()

GPIO.cleanup()




