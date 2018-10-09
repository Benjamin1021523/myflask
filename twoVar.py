from flask import Flask
app = Flask(__name__)

a = '''<br>
use /&lt;name&gt; to print your name<br>
use /&lt;name&gt;/&lt;id&gt; to print your name and id<br>
'''

@app.route("/")
def index():
    return "Index page" + a
@app.route("/<name>")
def helloXXX(name):
    return "Hello {}!".format(name)
@app.route("/<name>/<id>")
def name_id(name, id):
    return "name: {}, id: {}".format(name, id)

if __name__ == "__main__":
    app.run()