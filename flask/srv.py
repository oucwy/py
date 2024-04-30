#
# flask服务器，接收url请求后，查询mongodb中news表，返回新闻列表
# 本文件上传到服务器位置：markwy.com上，/home/yong/flask/news_flask_markwy.py
# auth: markwy
# date: 2024.4.30
# 需要在markwy.com上安装flask和pymongo
# 以后台服务运行
# 客户端请求格式：http://markwy.com:5000/getnews
#
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
# 连接mongodb数据库，在markwy.com上，实际使用时，需要修改用户名和密码
client = MongoClient(
    "mongodb://markwy:Free_7890@markwy.com:27017"
)

# set database name:　myblog
db = client['myBlog']

# set collection name: newsCollection
collection = db['newsCollection']

# 收到/getnews后，返回新闻列表
@app.route('/getnews', methods=['GET'])
def get_news():
    news = collection.find()
    news_list = []
    for n in news:
        n['_id'] = str(n['_id'])
        news_list.append(n)
    return jsonify(news_list)

# 收到/about后，返回一个说明
@app.route('/about', methods=['GET'])
def about():
    return jsonify({'message': 'markwy.com新闻服务。使用Python实现Flask服务器，连接MongoDB数据库。by markwy，2024.4.30'})

# 收到根路径请求，返回一个说明
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'markwy.com数据服务已运行。/getnews获取新闻列表，/about获取说明。'})

# 其他请求，返回404
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message': '404 not found'}), 404

if __name__ == '__main__':
    # 在5000端口监听所有ip地址的请求
    app.run(host='0.0.0.0', port=5000)

