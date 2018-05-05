# -*- coding: utf-8 -*-
import requests
import json
import urllib
from secret_info import CORPSECRET

# 简单的get请求
req = requests.get(url='http://www.baidu.com')
if req.status_code == 200:
    info = req.text
    # print(info)


# 带参数的get请求
# 交给requests处理时，url中文可以加u，也可以不加
param = {
    'q': '钉钉',
    'range': 'all',
    'c': 'new'
}
content = urllib.urlencode(param)
url_1 = 'http://www.sina.com.cn/mid/search.shtml?' + content
url_2 = 'http://www.sina.com.cn/mid/search.shtml?range=all&c=news&q=%E9%92%89%E9%92%89'
url_3 = u'http://www.sina.com.cn/mid/search.shtml?range=all&c=news&q=钉钉'
req = requests.get(url=url_3)
if req.status_code == 200:
    info = req.text
    # print(info)


# post请求 json格式数据
dd_robot_url = 'https://oapi.dingtalk.com/robot/send?access_token=33e573e59594249cdbbdf854a3e2d6326e155e3df811c2fc5191cd8041ba337e'
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
req = requests.post(url=dd_robot_url, data=json.dumps(dd_content), headers={'content-type': 'application/json'})
if req.status_code == 200:
    info = req.text
    # print(info)


# post请求 表单格式数据
corpid = 'dingcd586d15e8bfef5d35c2f4657eb6378f'
# 填写企业号密码
corpsecret = CORPSECRET
req = requests.get("https://oapi.dingtalk.com/gettoken?corpid=%s&corpsecret=%s"%(corpid, corpsecret))
if req.status_code == 200:
    print(req.text)
access_token = json.loads(req.text)['access_token']
content = {
    'format': 'json',
    'session': access_token,
    'agent_id': 172361337,
    'method': 'dingtalk.corp.message.corpconversation.asyncsend',
    'timestamp': '2018-05-04 20:19:00',
    'msgtype': 'TEXT',
    'msgcontent': """{"content": "我是消息"}""",
    'to_all_user': 'false',
    'v': 2.0,
    'userid_list': 'manager9106'
}
content = urllib.urlencode(content)
req = requests.post(url="https://eco.taobao.com/router/rest", data=content, headers={'content-type': 'application/x-www-form-urlencoded'})
if req.status_code == 200:
    info = req.text
    print(info)


