# python向微信好友发消息
# pip install itchat
import itchat
# 调试发现，能弹出二维码，但扫完后提示一个新设备要登录，按钮灰色，显示倒计时，需5秒后才能按，此时已经超时，又弹出二维码，如此循环。Not a good bird。
itchat.auto_login()
# itchat.auto_login(hotReload=True)
# itchat.auto_login(enableCmdQR=2, hotReload=True)
# itchat.auto_login(hotReload=True, statusStorageDir='itchat.pkl')
# itchat.auto_login(hotReload=True, statusStorageDir='itchat.pkl', enableCmdQR=2)
#
# # 获取好友列表
# friends = itchat.get_friends(update=True)[0:]
# for i in friends:
#    print(i['NickName'])


# 发送消息
# itchat.send('Hello, WeChat Friend!', toUserName='filehelper')