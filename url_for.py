from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
	return 'index'
@app.route('/login')
def login():
	return 'login'
@app.route('/user/<username>')
def profile(username):
	return '{}\'s profile'.format(username)
	
with app.test_request_context():
	print(url_for('index'))
	print(url_for('login'))
	print(url_for('login', next='/'))
	print(url_for('profile', username='John Doe'))
#查看各函式用網址如何呼叫與傳值
#也可以拿來用在template網頁上目標網址