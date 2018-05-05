# -*- coding: utf-8 -*-
import requests
import json
import datetime
from secret_info import CORPSECRET


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


# 发送企业通知
def send_msg(t, agent_id):
    content = {
        'format': 'json',
        'session': get_access_token(),
        'agent_id': agent_id,
        'method': 'dingtalk.corp.message.corpconversation.asyncsend',
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'msgtype': 'TEXT',
        'msgcontent': """{"content": "%s"}""" % t,
        'to_all_user': 'false',
        'v': 2.0,
        'userid_list': 'manager9106'
    }
    url = "https://eco.taobao.com/router/rest"
    req = requests.post(url=url, data=content, headers={'content-type': 'application/x-www-form-urlencoded'})
    print(req.text)
    return json.loads(req.text)['dingtalk_corp_message_corpconversation_asyncsend_response']['result']['task_id']


# 检查通知发送进度
def check_progress(task_id, agent_id):
    content_progress = {
        'format': 'json',
        'method': 'dingtalk.corp.message.corpconversation.getsendprogress',
        'v': 2.0,
        'session': get_access_token(),
        'agent_id': agent_id,
        'task_id': task_id
    }
    url = "https://eco.taobao.com/router/rest"
    resp = requests.post(url, data=content_progress,
                         headers={'content-type': 'application/x-www-form-urlencoded;charset=utf-8'})
    print(resp.text)


# 检查发送结果
def check_result(task_id, agent_id):
    content_result = {
        'format': 'json',
        'method': 'dingtalk.corp.message.corpconversation.getsendresult',
        'v': 2.0,
        'session': get_access_token(),
        'agent_id': agent_id,
        'task_id': task_id
    }
    url = "https://eco.taobao.com/router/rest"
    resp = requests.post(url, data=content_result,
                         headers={'content-type': 'application/x-www-form-urlencoded;charset=utf-8'})
    print(resp.text)


if __name__ == '__main__':
    # 微应用agent_id = 172361337，同一个人相同的消息一定时间内只能发一次（一定时间小于等于1天）
    t_id = send_msg(u'消息消息', 172361337)
    check_progress(t_id, 172361337)
    check_result(t_id, 172361337)
