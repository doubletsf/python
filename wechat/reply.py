import itchat
import time
from itchat.content import *

@itchat.msg_register(INCOME_MSG)
def text_reply(msg):
    # 打印获取到的信息
    # print(msg)
    itchat.send("您发送了：\'%s\'\n微信目前处于python托管，你的消息我会转发到手机，谢谢" %
                (msg['Text']), toUserName=msg['FromUserName'])


itchat.auto_login( hotReload=True)
itchat.run()