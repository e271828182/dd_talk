#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import print_function
import websocket, time, json


def on_message(ws, message):
    stdmsg = json.loads(message)[1]
    if type(stdmsg) is not dict:
        print(stdmsg, end='')


def on_error(ws, error):
    print(error)
    ws.close()


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send(json.dumps(["set_size", 54, 132, 869, 636]))
    ws.send(json.dumps([u"stdin", u"cd /home/yangyang04/notebooks\r"]))
    ws.send(json.dumps([u"stdin",
                        u"jupyter nbconvert --ExecutePreprocessor.timeout=600  --execute 钉钉机器人2.ipynb --to notebook --inplace\r"]))
    ws.send(json.dumps([u"stdin", u"exit\r"]))


if __name__ == '__main__':
    token = 'xxx'
    url = "ws://jupyter.nidianwo.com/user/yangyang04/terminals/websocket/pao%d?token=%s" % (int(time.time()), token)
    ws = websocket.WebSocketApp(url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
