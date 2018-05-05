# -*- coding: utf-8 -*-
import requests
import json
from secret_info import CORPSECRET

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


def get_access_token():
    # post请求 表单格式数据
    corpid = 'dingcd586d15e8bfef5d35c2f4657eb6378f'
    # 填写企业号密码
    corpsecret = CORPSECRET
    req = requests.get("https://oapi.dingtalk.com/gettoken?corpid=%s&corpsecret=%s" % (corpid, corpsecret))
    if req.status_code == 200:
        print(req.text)
    access_token = json.loads(req.text)['access_token']
    return access_token


def upload_pic(image_file):
    url = "https://oapi.dingtalk.com/media/upload?access_token=%s&type=file" % get_access_token()
    multiple_files = [('media', (image_file.split('/')[-1], open(image_file, 'rb'), 'image'))]
    r = requests.post(url, files=multiple_files)
    media_id = r.json()['media_id']
    return media_id


if __name__ == '__main__':
    dd_robot_url = 'https://oapi.dingtalk.com/robot/send?access_token=33e573e59594249cdbbdf854a3e2d6326e155e3df811c2fc5191cd8041ba337e'
    text = u'![](%s)' % upload_pic('123.png')
    send_msg(title=u'消息来了', t=text, url=dd_robot_url, mobiles=['15150375379'])
