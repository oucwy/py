# 能用，但不好用，发消息有错。
from wxauto import *
wx = WeChat()
# msgs = wx.get_msg()
# wx.Search(
#     '艾滨'
# )
# msgs = wx.GetLastMessage
# for msg in msgs:
# print(msgs)
msg = 'Hello, I am Yong Yong'
who = '文件传输助手'
wx.ChatWith(who)
wx.SendMsg(msg)