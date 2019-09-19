# -*- coding:utf-8 -*-
from flask import Flask, jsonify, abort, make_response, render_template, request
from flask_cors import CORS

from datetime import datetime

api = Flask(__name__)
CORS(api)  # CORS有効化


@api.route('/del', methods=['GET'])
def delFirstLine():
    with open("./javascriptTest", mode='r') as f:
        lines = f.readlines()

    with open("./javascriptTest", mode='w') as f:
        lines = f.writelines([item for item in lines[1:]])

    return get()


@api.route('/get', methods=['GET'])
def get():
    result = ''
    with open("./javascriptTest", mode='r') as f:
        result += f.read()
    return result


@api.route('/post', methods=['POST'])
def post():
    result = request.form['param']
    with open("./javascriptTest", mode='a') as f:
        f.write(datetime.now().strftime("%Y/%m/%d %H:%M:%S") + ' : ' + result + "\n")
    return make_response(result)


@api.route('/')
def index():
    with open("./templates/index.html", mode='r', encoding='utf-8') as f:
        linesIndex = f.readlines()

    linesScript = ''
    with open("./templates/javascriptTest.js", mode='r', encoding='utf-8') as f:
        linesScript += f.read()

    lines = ''
    for line in linesIndex:
        if 'javascriptTest.js' in line:
            lines += '<script>' + linesScript + '</script>'
        else:
            lines += line

    return lines


# 4000番ポートでWebサーバを起動する
if __name__ == '__main__':
    api.run(host='127.0.0.1', port=4000, debug=True)