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
    footerMessage = ''

    if not 'procSelect' in request.form:
        rowList = selectData()
        footerMessage = '処理を選択されていません'
        companyId = ''
        return makeHtml(rowList, companyId, footerMessage)

    if request.form['procSelect'] == 'select':
        rowList = selectData()
        return makeHtml(rowList, request.form['companyId'])

    if request.form['procSelect'] == 'insert':
        companyId = insertData(request.form)

        if companyId == None:
            footerMessage = 'companyIdは99999999を超えて採番できません'
        rowList = selectData()
        return makeHtml(rowList, companyId, footerMessage)

    if request.form['procSelect'] == 'update':
        updateData(request.form)
        rowList = selectData()
        return makeHtml(rowList, request.form['companyId'])

    if request.form['procSelect'] == 'delete':
        deleteData(request.form['companyId'])
        rowList = selectData()
        return makeHtml(rowList)


if __name__ == '__main__':
    initdb()
    app.debug = True
    app.run(host='127.0.0.1', port=8080)
