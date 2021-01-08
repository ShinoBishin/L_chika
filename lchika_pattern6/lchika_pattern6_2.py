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

data = []

i = 0

# def led():
#     while True:
#         if(data == 1):
#             GPIO.output(led, GPIO.HIGH)
#             time.sleep(0.1)
#         else:
#             GPIO.output(led, GPIO.LOW)
#             time.sleep(0.1)


while time.time() - lead_time < 10:
    print(GPIO.input(btn1))
    time.sleep(0.1)
    data.append(GPIO.input(btn1))

#　for文でdata内のデータを最後まで調べる
#　入ってる値を取り出す
#　１ならLチカ

print(data)

for i in data:
    print(i)
    time.sleep(0.1)
    if(i == 1):
        GPIO.output(led,GPIO.HIGH)
    else:
        GPIO.output(led,GPIO.LOW)

GPIO.cleanup()

