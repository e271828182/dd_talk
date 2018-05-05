# -*- coding: utf-8 -*-
import requests
import json
from secret_info import CORPSECRET
from secret_info import CORPID


def get_access_token():
    # post请求 表单格式数据
    corpid = CORPID
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


# 创建微应用
def create_app(app_icon, app_name, app_esc, homepage_url, pc_homepage_url=''):
    content = {
        "appIcon": app_icon,
        "appName": app_name,
        "appDesc": app_esc,
        "homepageUrl": homepage_url,
        "pcHomepageUrl": pc_homepage_url
    }
    url = "https://oapi.dingtalk.com/microapp/create?access_token=%s" % get_access_token()
    req = requests.post(url=url, data=json.dumps(content), headers={'content-type': 'application/json'})
    print(req.text)
    # 坑，注意这里是小写
    return json.loads(req.text)['agentid']


# 更新微应用
def update_app(agent_id, app_icon, app_name, app_esc, homepage_url, pc_homepage_url=''):
    content = {
        "agentId": agent_id,
        "appIcon": app_icon,
        "appName": app_name,
        "appDesc": app_esc,
        "homepageUrl": homepage_url,
        "pcHomepageUrl": pc_homepage_url
    }
    url = "https://oapi.dingtalk.com/microapp/update?access_token=%s" % get_access_token()
    resp = requests.post(url, data=json.dumps(content), headers={'content-type': 'application/json'})
    print(resp.text)
    return json.loads(resp.text)['agentId']


# 删除微应用
def delete_app(agent_id):
    content = {
        "agentId": agent_id
    }
    url = "https://oapi.dingtalk.com/microapp/delete?access_token=%s" % get_access_token()
    resp = requests.post(url, data=json.dumps(content), headers={'content-type': 'application/json'})
    print(resp.text)


# 微应用列表
def list_app():
    url = "https://oapi.dingtalk.com/microapp/list?access_token=%s" % get_access_token()
    resp = requests.post(url, headers={'content-type': 'application/json'})
    print(resp.text)
    result = json.loads(resp.text)
    print([r for r in result['appList'] if r['isSelf'] is True])
    return [r['agentId'] for r in result['appList'] if r['isSelf'] is True]


if __name__ == '__main__':
    m_id = upload_pic('../group_chat_robot/img_msg/123.png')
    print(m_id)
    a_id = create_app(m_id, u'微应用测试', u"试试", 'http://www.baidu.com')
    print(a_id)
    print(list_app())
