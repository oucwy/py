
# Path: client.py
# 写一个客户端，请求服务器，获取新闻列表

import requests

url = 'http://127.0.0.1:5000/news'
res = requests.get(url)
print(res.json())

# Path: news.json
# 写一个json文件，存储新闻数据
[
    {
        "title": "新闻标题1",
        "content": "新闻内容1"
    },
    {
        "title": "新闻标题2",
        "content": "新闻内容2"
    }
]

# Path: insert.py
# 写一个脚本，读取news.json文件，插入mongodb数据库
from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client['news']
collection = db['news']

with open('news.json', 'r') as f:
    news = json.load(f)
    collection.insert_many(news)

# Path: query.py
# 写一个脚本，查询mongodb数据库中的新闻
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['news']
collection = db['news']

news = collection.find()
for n in news:
    print(n)

# Path: requirements.txt
# 写一个requirements.txt文件，列出所有依赖的包
flask
pymongo
requests

# Path: Dockerfile
# 写一个Dockerfile文件，构建docker镜像
FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "srv.py"]

