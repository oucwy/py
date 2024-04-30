
# 
# 客户端测试，请求获取新闻列表
# author: markwy
# date: 2024.4.30
#
import requests
import json

url = 'http://markwy.com:5000/getnews'

res = requests.get(url)
# print(res.json())
# json结果放入一个列表中
news_list = res.json()
# 打印新闻列表
for news in news_list:
    print(news['date'])
    print(news['content'])
    print('---')

# 保存到json文件
with open('c:/dev/py/flask/news.json', 'w') as f:
    json.dump(news_list, f)