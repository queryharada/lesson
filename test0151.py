from flask import Flask, request
import sqlite3
from contextlib import closing

#
# Flask
#
app = Flask(__name__)

htmlData = '''
        <form method="post" action="/select">
            <p>Value001:<input type="text" name="Value001" size="40" value="11111"></p>
            <p>Value002:<input type="text" name="Value002" size="40" value="22222"></p>
            <p><input type="submit" value="送信"></p>
        </form>
        '''


@app.route('/')
def index():
    return htmlData


@app.route('/select', methods=['POST'])
def select():
    responseStr = ''
    for elementKey in request.form:
        responseStr += elementKey + ':' + request.form[elementKey] + '<br>'
    return responseStr


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=8080)
