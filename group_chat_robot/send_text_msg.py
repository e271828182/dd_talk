# -*- coding: utf-8 -*-
import requests
import json


def send_msg(t, url, mobiles=[]):
    dd_content = {
        "msgtype": "text",
        "at": {
            "atMobiles": [str(m) for m in list(mobiles)],
            "isAtAll": False
        },
        "text": {
            "content": "%s" % t
        }
    }
    print(dd_content)
    print(requests.post(url, data=json.dumps(dd_content), headers={'content-type': 'application/json'}).text)


if __name__ == '__main__':
    dd_robot_url = 'https://oapi.dingtalk.com/robot/send?access_token=33e573e59594249cdbbdf854a3e2d6326e155e3df811c2fc5191cd8041ba337e'
    send_msg(t=u'消息主体', url=dd_robot_url, mobiles=['15150375379'])
