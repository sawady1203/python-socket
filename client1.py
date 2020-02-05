# -*- coding: utf-8 -*-
"""
データを継続して受け付けるserver
50000番ポートで待ち受け
"""

import socket
import datetime
import sys
import time
import random
import json


# グローバル変数
PORT = 50000
BUFSIZE = 4096  # 受信バッファの大きさ
TIME = 1

# メイン

# サーバーとの接続
# host = input("接続先さーば:")
host = "localhost"


def main():
    try:
        while True:
            # ソケットの作成
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                client.connect((host, PORT))

            except:
                print("接続できません")
                sys.exit()
            # data = input("なにか入力してください")
            # if data == "q":
            #     sys.exit()
            data = dict()
            log = random.randrange(1, 10, 1)
            data['time'] = str(datetime.datetime.now())
            data['log'] = log
            data = json.dumps(data)  # json化
            # 送信
            client.send(data.encode("utf-8"))
            # 返答(受信)
            response = client.recv(BUFSIZE)
            print("サーバーからのメッセージ")
            print(response.decode("UTF-8"))
            client.close()
            time.sleep(TIME)


    except:
        print("stoped")
        sys.exit()

    finally:
        client.close()

if __name__ == "__main__":
    main()
