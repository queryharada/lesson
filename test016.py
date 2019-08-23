# -*- coding:utf-8 -*-
from flask import Flask, request

from test01601view import *
from test01602model import *

#
# Flask
#
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    #
    # 初期(DBからデータを取得)
    #
    rowList = selectData()
    return makeHtml(rowList)


@app.route('/router', methods=['POST'])
def router():
    messageId = '000'

    #
    # 処理チェック
    #
    if not 'procSelect' in request.form:
        rowList = selectData()
        messageId = '001'
        companyId = ''
        return makeHtml(rowList, companyId, messageId)

    #
    # 選択
    #
    if request.form['procSelect'] == 'select':
        if not 'companyId' in request.form:
            messageId = '002'  # ''会社一覧が選択されていません'
            companyId = ''
        else:
            companyId = request.form['companyId']

        rowList = selectData()
        return makeHtml(rowList, companyId, messageId)

    #
    # 新規
    #
    if request.form['procSelect'] == 'insert':
        companyId, messageId = insertData(request.form)
        rowList = selectData()
        return makeHtml(rowList, companyId, messageId)

    #
    # 更新
    #
    if request.form['procSelect'] == 'update':
        if request.form['companyIdKey'] == '':
            messageId = '002'  # ''会社一覧が選択されていません'
            companyId = ''
        else:
            companyId, messageId = updateData(request.form)

        rowList = selectData()
        return makeHtml(rowList, companyId, messageId)

    #
    # 削除
    #
    if request.form['procSelect'] == 'delete':
        if not 'companyId' in request.form:
            messageId = '009'  # ''会社一覧が選択されていません'
        else:
            deleteData(request.form['companyId'])
        companyId = ''
        rowList = selectData()
        return makeHtml(rowList, companyId, messageId)


if __name__ == '__main__':
    #
    #  DB初期化
    #
    initdb()

    #
    #  FLASK起動
    #
    app.debug = True
    app.run(host='127.0.0.1', port=8080)
