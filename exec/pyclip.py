import pyperclip
 
# 复制文本到剪贴板
pyperclip.copy('这是要复制的文本')
 
# 粘贴剪贴板的内容
paste_content = pyperclip.paste()
print(paste_content)
 
# 如果需要复制一个列表，可以先转换为字符串
pyperclip.copy('\n'.join(['列表项1', '列表项2', '列表项3'])) 
 
# 粘贴时，需要手动分割字符串
list_from_clipboard = pyperclip.paste().split('\n')
print(list_from_clipboard)