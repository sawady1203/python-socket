# -*- coding: utf-8 -*-
"""
データを継続して受け付けるserver
50000番ポートで待ち受け
"""

import socket
import datetime
import traceback

# グローバル変数
PORT = 30000
BUFSIZE = 4096  # 受信バッファの大きさ

# ソケットの作成
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# アドレス設定
server.bind(("", PORT))

try:
    while True:
        data, client = server.recvfrom(BUFSIZE)
        msg = str(datetime.datetime.now())
        server.sendto(msg.encode("utf-8"), client)
        print(data)
        print(msg, "接続要求あり")
        print(client)
except:
    traceback.print_exc()
