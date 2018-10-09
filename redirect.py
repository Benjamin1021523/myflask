from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <form action="login" method="POST">
        <input type='text' name='in'>
        <input type="submit" value="POST">
    </form>
    '''
@app.route('/login', methods=['POST'])
def login():
    return redirect(url_for('result', name=request.form['in']))
@app.route('/result')
def result(name):
    return "your name is {}".format(name)
app.run()