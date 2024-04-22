# 写一个flask服务器，接收url请求后，查询mongodb中存的新闻，返回新闻列表
from flask import Flask, request, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client['news']
collection = db['news']

@app.route('/get_news', methods=['GET'])
def get_news():
    news = collection.find()
    news_list = []
    for n in news:
        news_list.append(n)
    return jsonify(news_list)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

