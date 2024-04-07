# Description: This is a simple program to generate new year greeting message for a list of people.
# Author: Wang Yong (markwy@126.com)
# Date: 2024-2-8

import pandas as pd
# read name list from a excel file
def read_name_list():
    # import pandas as pd
    name_list = pd.read_excel('name_list1.xlsx')
    return name_list

# read greeting message from a excel file
def read_greeting_message():
    # import pandas as pd
    greeting_message = pd.read_excel('greeting_message.xlsx')
    return greeting_message

# generate greeting message
def generate_greeting_message(name_list, greeting_message):
    import random
    greeting_list = []
    for i in range(len(name_list)):
        greeting_list.append('祝'+name_list['call_name'][i] + greeting_message['message'][random.randint(0, len(greeting_message)-1)])
    return greeting_list
        
# main function
if __name__ == '__main__':
    # import uiautomation as uia
    from wxauto import *
    import pyperclip
    import pyautogui as pag
    wx = WeChat()
    name_list = read_name_list()
    greeting_message = read_greeting_message()
    greeting_list = generate_greeting_message(name_list, greeting_message)
    print('准备自动发送微信祝福信息......')
    for i in range(len(greeting_list)):
        wx.Search(
            name_list['real_name'][i]
        )
        pyperclip.copy(greeting_list[i])
        pag.hotkey('ctrl', 'v')
        pag.press('enter')
        print('发送完成：'+greeting_list[i]) 
        print()
    print('发送结束。')
