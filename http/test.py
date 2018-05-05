# -*- coding: utf-8 -*-
import requests
import json

# 带参数的get请求
url_3 = u'http://www.sina.com.cn/mid/search.shtml?range=all&c=news&q=钉钉'
req = requests.get(url=url_3)
if req.status_code == 200:
    info = req.text
    print(info)


# post请求 json格式数据
dd_url = 'https://oapi.dingtalk.com/robot/send?access_token=33e573e59594249cdbbdf854a3e2d6326e155e3df811c2fc5191cd8041ba337e'
dd_content = {
    "msgtype": "markdown",
    "at": {
        "atMobiles": [],
        "isAtAll": True
    },
    "markdown": {
        "title": u"告警机器人测试",
        "text": "%s" % u'消息通知'
    }
}
print(dd_content)
req = requests.post(url=dd_url, data=json.dumps(dd_content), headers={'content-type': 'application/json'})
if req.status_code == 200:
    info = req.text
    print(info)
