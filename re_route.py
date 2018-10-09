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
def re_route(name, id):
    #可以在這裡判斷name的值，再次route?
    import re
    n = re.compile("^[A-Za-z_][A-Za-z0-9_-]*$")
    i = re.compile("^[0-9]+$")
    data1 = n.search(name)
    data2 = i.search(id)
    if data1 != None and data2 != None:
        return "name: {}, id: {}".format(data1[0], data2[0])
    else:
        return "form error"

if __name__ == "__main__":
    app.run()