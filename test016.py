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
    messageId = '000'

    if not 'procSelect' in request.form:
        rowList = selectData()
        messageId = '001'  # '処理が選択されていません'
        companyId = ''
        return makeHtml(rowList, companyId, messageId)

    if request.form['procSelect'] == 'select':
        if not 'companyId' in request.form:
            messageId = '002'  # ''会社一覧が選択されていません'
            companyId = ''
        else:
            companyId = request.form['companyId']

        rowList = selectData()
        return makeHtml(rowList, companyId, messageId)

    if request.form['procSelect'] == 'insert':
        companyId, messageId = insertData(request.form)
        rowList = selectData()
        return makeHtml(rowList, companyId, messageId)

    if request.form['procSelect'] == 'update':
        companyId, messageId = updateData(request.form)
        rowList = selectData()
        return makeHtml(rowList, companyId, messageId)

    if request.form['procSelect'] == 'delete':
        if not 'companyId' in request.form:
            messageId = '002'  # ''会社一覧が選択されていません'
        else:
            deleteData(request.form['companyId'])
        companyId = ''
        rowList = selectData()
        return makeHtml(rowList, companyId, messageId)


if __name__ == '__main__':
    initdb()
    app.debug = True
    app.run(host='127.0.0.1', port=8080)
