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

#　スタンバイモード
def ready():
    for i in range(2):
        GPIO.output(led, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led, GPIO.LOW)
        time.sleep(1)

#　記録モード
def btn_read(data):
    # 時間計測用変数
    lead_time = time.time()
    print("記録モード開始")
    while time.time() - lead_time < 10:
        data.append(GPIO.input(btn1))
        time.sleep(0.1)

# 点灯モード
def led_on(data):
    print("点灯モード開始")
    for i in data:
        time.sleep(0.1)
        if(i == 1):
            GPIO.output(led,GPIO.HIGH)
        else:
            GPIO.output(led,GPIO.LOW)



# スイッチの状態を監視、count変数の状態を判定してモードチェンジする
try:
    data = []
    mode = 0
    while True:
        # モード切替をボタンを読み取って実施する
        if (GPIO.input(btn2) == 1):
            time.sleep(0.01)
            mode += 1
        print(mode)

        # モードごとの処理を実施する
        if(mode == 1):
            print("スタンバイを開始します")
            ready()
            mode += 1
            print("スタンバイを終了")
        elif(mode == 2):
            pass
        elif(mode == 3):
            print("記録モードを開始")
            btn_read(data)
            mode += 1
            print("点灯モードを終了します")
        elif(mode == 4):
            pass
        elif(mode == 5):
            print("点灯モードを開始します")
            led_on(data)
            # 各データを初期化
            data = []
            mode = 0
            print("点灯モードを終了します")
            print("再度初期状態へ戻ります")
        else:
            pass
        
        time.sleep(0.1)
    
except KeyboardInterrupt:
    pass
finally:
    print("終了処理中・・・\n終了しました")
    GPIO.cleanup()
