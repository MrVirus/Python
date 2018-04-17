# coding=utf8
import requests
import itchat

KEY = '6746cc93f7cd4b849ff0b339e141b51e'


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        print("收到消息:", msg)
        return r.get('text')
    except:
        return


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    reply = "[我是文诗妹的机器人]" + get_response(msg['Text'])
    print("回复消息:", reply)
    return reply


itchat.auto_login(hotReload=True)
itchat.run()
