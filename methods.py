from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
	return '''
	<form action="login" method="POST">
		<input type='text' name='in'>
		<input type="submit" value="POST">
	</form>
	<br><br><br>
	<form action="login" method="GET">
		<input type='text' name='in'>
		<input type="submit" value="GET">
	</form>
	'''

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return "1"
	else:
		return '0 {}'.format(request.form['in'])
app.run()