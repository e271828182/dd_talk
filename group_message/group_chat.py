# -*- coding: utf-8 -*-
import requests
import json
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

# 创建群聊
def create_group_chat(group_name, owner, useridlist):
    url = 'https://oapi.dingtalk.com/chat/create?access_token=%s' % get_access_token()
    content = {
        "name": group_name,
        "owner": owner,
        "useridlist": useridlist
    }
    resp = requests.post(url, data=json.dumps(content), headers={'content-type': 'application/json'})
    print(resp.text)
    chatid = json.loads(resp.text).get('chatid')
    return chatid


# 发送消息
def send_msg(t, chatid):
    url = 'https://oapi.dingtalk.com/chat/send?access_token=%s' % get_access_token()
    content = {
        'chatid': chatid,
        "msgtype": "text",
        "text": {
            "content": t
        }
    }
    resp = requests.post(url, data=json.dumps(content), headers={'content-type': 'application/json'})
    print(resp.text)
    message_id = json.loads(resp.text).get('messageId')
    return message_id


# 获取群信息
def get_group_info(chatid):
    url = 'https://oapi.dingtalk.com/chat/get?access_token=%s&chatid=%s' % (get_access_token(), chatid)
    resp = requests.get(url)
    print(resp.text)

# 修改群信息
def update_group_info(chatid, group_name, owner, add_useridlist=[], del_useridlist=[]):
    url = 'https://oapi.dingtalk.com/chat/update?access_token=%s'% get_access_token()
    content = {
        "chatid": chatid,
        "name": group_name,
        "owner": owner,
        "add_useridlist": add_useridlist,
        "del_useridlist": del_useridlist
    }
    resp = requests.post(url, data=json.dumps(content), headers={'content-type': 'application/json'})
    print(resp.text)


# 查看已读人员列表
def get_read_list(message_id):
    base_url = 'https://oapi.dingtalk.com/chat/getReadList?access_token=%(access_token)s&messageId=%(message_id)s&cursor=%(cursor)d&size=%(size)d'
    url = base_url % {
        'access_token': get_access_token(),
        'message_id': message_id,
        'cursor': 0,
        'size': 100
    }
    resp = requests.get(url)
    print(resp.text)
    next_cursor = json.loads(resp.text).get('next_cursor')
    while(True):
        if not next_cursor:
            break
        url = base_url % {
            'access_token': get_access_token(),
            'message_id': message_id,
            'cursor': next_cursor,
            'size': 100
        }
        resp = requests.get(url)
        print(resp.text)

if __name__ == '__main__':
    # c_id = create_group_chat('456','manager9106',['manager9106'])
    c_id = 'chat1dcd24886b5ba3cfcf89159e364e09d8'
    m_id = send_msg(u'你好', c_id)
    get_read_list(m_id)