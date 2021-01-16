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
count = 0
data = []
i = 0
select = 0

#　スタンバイモード
def ready():
    while (i < 1):
        GPIO.output(led, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led, GPIO.LOW)
        time.sleep(1)
        i = i + 1

#　記録モード
def btn_read():
    print("記録モード開始")
    while time.time() - lead_time < 10:
        data.append(GPIO.input(btn1))
        time.sleep(0.1)
        if(time.time() - lead_time < 10):
            print("記録モード終了")
            if(GPIO.input(btn2) == 1):
                select = 2
    


# 点灯モード
def led_on():
    for i in data:
        time.sleep(0.1)
        if(i == 1):
            GPIO.output(led,GPIO.HIGH)
        else:
            GPIO.output(led,GPIO.LOW)


# スイッチの状態を監視、count変数の状態を判定してモードチェンジする


try:
    while True:
        if(GPIO.input(btn2) == 1):
            time.sleep(0.01)
            if(select == 0):
                select = 1
                print("スタンバイ")
            elif(select == 1):
                print("記録モード展開")
                while time.time() - lead_time < 10:
                    data.append(GPIO.input(btn1))
                    time.sleep(0.1)
                    if (time.time() - lead_time) == 1:
                        print("記録モード終了")
            elif(select == 2):
                print("点灯モード展開")
            while(GPIO.input(btn2) == 1):
                time.sleep(0.01)

    
except KeyboardInterrupt:
    pass
finally:
    print("終了処理中・・・\n終了しました")
    GPIO.cleanup()
