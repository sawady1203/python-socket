# -*- coding: utf-8 -*-
"""
データを継続して受け付けるserver
50000番ポートで待ち受け
"""

import socket
import datetime
import sys
import json
import traceback

# グローバル変数
PORT = 50000
BUFSIZE = 4096  # 受信バッファの大きさ

# ソケット作成
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# アドレスの設定
server.bind(("", PORT))
# 接続の待ち受け
server.listen()
print("Now server is listening..")

def data_to_mysql():
    pass

def time_counter():
    pass

def send_UDP(udp_ip, udp_port, data):
    """
    通知先のラズパイにはclient接続なしに任意のタイミングで送りたいので
    UDPで送る。
    - upd_ip
        : 通知先のIPアドレス。
    - upd_port
        : 通知先のポート。
    - data
        : 送るデータ
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(data, (udp_ip, udp_port))
    res = client.recv(BUFSIZE)
    client.close()
    return res

def main():
    try:
        while True:
            client, addr = server.accept()
            now = datetime.datetime.now()
            print(now, "接続要求あり")
            # print(client)
            print("*"*50)
            print(addr)

            try:
                # while True:
                _data = client.recv(BUFSIZE)
                # print(data)
                data = _data.decode("utf-8")
                # print(data)
                try:
                    data = json.loads(data)
                    data_to_mysql()
                    time_counter()
                    ans = send_UDP("localhost", 30000, _data)
                    print(ans)
                except:
                    traceback.print_exc()
                print("クライアントからのメッセージ")
                print(data)
                print(type(data))
                msg = "success!"
                client.sendall(msg.encode("UTF-8"))

            except:
                sys.exit()

            client.close()
    except:
        traceback.print_exc()

if __name__ == "__main__":
    main()
