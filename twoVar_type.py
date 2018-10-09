from flask import Flask
app = Flask(__name__)

a = '''<br>
use /&lt;name&gt; to print your name<br>
use /&lt;name&gt;/&lt;id&gt; or /&lt;id&gt;/&lt;name&gt; to print your name and id<br>
'''

@app.route("/")
def index():
    return "Index page" + a
@app.route("/<name>")
def helloXXX(name):
    return "Hello {}!".format(name)
@app.route("/<string:name>/<int:id>")
@app.route("/<int:id>/<string:name>")
def type_route(name, id):
    return "name: {}, id: {}".format(name, id)

if __name__ == "__main__":
    app.run()