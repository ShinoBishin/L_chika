# ボタンからの入力データを配列に記録する
# 配列に記録したデータを取り出してLEDを点灯する
# 切り替え用ボタンを使って記録、点灯モードを切り替える

import RPi.GPIO as GPIO
import time

# デバイスの接続先
led = 23
btn1 = 17
btn2 = 27

# GPIOの初期化
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(btn1, GPIO.IN)
GPIO.setup(btn2, GPIO.IN)

# 時間計測用変数
lead_time = time.time()

# btn2の入力により記録モード、入力モードを切り替える
mode = 0
count = 0
data = []

i = 0


def btn_read():
    GPIO.output(led, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led,GPIO.LOW)
    while time.time() - lead_time < 10:
        data.append(GPIO.input(btn1))
        time.sleep(0.1)

#　for文でdata内のデータを最後まで調べる
#　入ってる値を取り出す
#　１ならLチカ
def led_on():
    GPIO.output(led,GPIO.LOW)
    for i in data:
        time.sleep(0.1)
        if(i == 1):
            GPIO.output(led,GPIO.HIGH)
        else:
            GPIO.output(led,GPIO.LOW)

btn_read()
led_on()


# while True:
#     if(GPIO.input(btn2) == 1):
#         count = count + 1
#         print(str(count))
#         while(GPIO.input(btn2) == 1):
#             time.sleep(0.1)
#             if (count >= 3 ):
#                 count = 0

# if(count == 1):
#     time.sleep(0.1)
#     GPIO.output(led, GPIO.HIGH)
# elif(count == 2):
#     btn_read()
# else:
#     led_on()


GPIO.cleanup()

