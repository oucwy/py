# weixin operation


import win32api, win32gui, win32con
import win32clipboard as clipboard
import time
# import requests
from apscheduler.schedulers.blocking import BlockingScheduler

# 按下ctrl+v并回车
def paste_and_enter(win):
    # 以下为“CTRL+V”组合键,回车发送，（方法一）
    win32api.keybd_event(17, 0, 0, 0)  # 有效，按下CTRL
    time.sleep(1)  # 需要延时
    win32gui.SendMessage(win, win32con.WM_KEYDOWN, 86, 0)  # V
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开CTRL
    time.sleep(1)  # 缓冲时间
    win32gui.SendMessage(win, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)  # 回车发送
    return

# 将文本信息缓存入剪贴板
def copy_to_clipboard(str):
    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardData(win32con.CF_UNICODETEXT, str)
    clipboard.CloseClipboard()
    return

# def day_english():
#     # 获取金山词霸每日一句
#     url = 'http://open.iciba.com/dsapi'
#     r = requests.get(url)
#     content = r.json()['content']
#     note = r.json()['note']
#     print(content + note)
#     return content + note

def get_window(className, titleName):
    # title_name = className  # 单独打开，好友名称
    # win = win32gui.FindWindow(className, titleName)
    # 窗体前端显示
    # win32gui.SetForegroundWindow(win)
    # 使窗体最大化
    # win32gui.ShowWindow(win, win32con.SW_MAXIMIZE)
    win = win32gui.FindWindow(className, titleName)
    print("找到句柄：%x" % win)
    if win != 0:
        # left, top, right, bottom = win32gui.GetWindowRect(win)
        # print(left, top, right, bottom)  # 最小化为负数
        win32gui.SetForegroundWindow(win)  # 置于最前
        time.sleep(0.5)
    else:
        print('找不到- %s -这个人（或群）！' % className)
    return win
#######################发送过程=================
def sendMsg():
    # 查找微信小窗口
    # win = get_window('ChatWnd', '文件传输助手')
    win = get_window('WeChatMainWndForPC', '')
    # 读取文本
    
    str = '早上好，新的一天开始了，加油！'
    print(str)
    copy_to_clipboard(str)
    paste_and_enter(win)


# scheduler = BlockingScheduler()
# # scheduler.add_job(sendTaskLog, 'interval', seconds=3)
# # scheduler.add_job(sendTaskLog, 'cron',day_of_week='mon-fri', hour=7,minute=31,second='10',misfire_grace_time=30)
# scheduler.add_job(sendTaskLog, 'cron', day_of_week='mon-fri', hour=6, minute=55, second='10', misfire_grace_time=30)
# try:
#     scheduler.start()
# except (KeyboardInterrupt, SystemExit):
#     pass

sendMsg()