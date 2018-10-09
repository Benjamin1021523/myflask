from flask import Flask
app = Flask(__name__)

a = '''<br>
use /&lt;name&gt; to print your name<br>
'''

@app.route("/")
def index():
    return "Index page" + a
@app.route("/<name>")
def helloXXX(name):
    return "Hello {}!".format(name)

if __name__ == "__main__":
    app.run()