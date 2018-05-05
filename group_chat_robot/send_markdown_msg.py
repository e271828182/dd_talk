# -*- coding: utf-8 -*-
import requests
import json


def send_msg(title, t, url, mobiles=[]):
    dd_content = {
        "msgtype": "markdown",
        "at": {
            "atMobiles": [str(m) for m in list(mobiles)],
            "isAtAll": False
        },
        "markdown": {
            "title": title,
            "text": "%s" % t
        }
    }
    print(dd_content)
    print(requests.post(url, data=json.dumps(dd_content), headers={'content-type': 'application/json'}).text)


if __name__ == '__main__':
    dd_robot_url = 'https://oapi.dingtalk.com/robot/send?access_token=33e573e59594249cdbbdf854a3e2d6326e155e3df811c2fc5191cd8041ba337e'
    text = u'消息主体  \n# 标题  \n**加粗**  \n*斜体*  \n[链接](https://www.dingtalk.com/)  \n- item1\n- item2'
    send_msg(title=u'消息来了', t=text, url=dd_robot_url, mobiles=['15150375379'])