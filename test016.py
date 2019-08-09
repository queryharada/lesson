# -*- coding:utf-8 -*-
from flask import Flask, request

from test01601view import *
from test01602model import *

#
# Flask
#
app = Flask(__name__)


@app.route('/')
def index():
    # DBからデータを取得
    rowList = selectData()
    return makeHtml(rowList)


@app.route('/router', methods=['POST'])
def router():
    if request.form['procSelect'] == 'select':
        rowList = selectData()
        return makeHtml(rowList, request.form['companyId'])

    if request.form['procSelect'] == 'insert':
        companyId = insertData(request.form)
        rowList = selectData()
        return makeHtml(rowList, companyId)

    if request.form['procSelect'] == 'update':
        updateData(request.form)
        rowList = selectData()
        return makeHtml(rowList, request.form['companyId'])

    if request.form['procSelect'] == 'delete':
        rowList = selectData()
        deleteData(rowList, request.form['companyId'])
        return makeHtml('')


if __name__ == '__main__':
    initdb()
    app.debug = True
    app.run(host='127.0.0.1', port=8080)
