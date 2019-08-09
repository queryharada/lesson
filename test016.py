from flask import Flask, request
import sqlite3
from contextlib import closing

#
# Flask
#
app = Flask(__name__)

#
# sqlite実行SQL文
#
dbname = 'company.db'
dropTable = 'drop table company'
createTable = '''create table company (
                    companyId  char(8) primary key,
                    companyName varchar(128),
                    telephoneNumber varchar(12),
                    address varchar(256),
                    discription text
                )'''
insertTable = 'insert into company (companyId, companyName, telephoneNumber, address, discription) values (?,?,?,?,?)'
insertData = [
    ('12345678', 'ABC', '0354762911', '住所', '説明'),
    ('00000001', 'ABC1', '0422111163', '住所１', '説明１'),
    ('00000002', 'ABC2', '08012345678', '住所２', '説明２'),
    ('00000003', 'ABC3', '035476291', '住所３', '説明３'),
    ('00000004', 'ABC4', '035476291', '住所４', '説明４'),
    ('00000005', 'ABC5', '035476291', '住所５', '説明５')
]
selectTable = 'select * from company'

selectMaxcompanyId = 'select max(companyId) from company'
editTable = 'UPDATE company SET companyName=?, telephoneNumber=?, address=?, discription=? WHERE companyId=?'
delTable = 'DELETE from company WHERE companyId=?'

#
# HTML <form>......</form>
#
formStat = '''<form method="post" action="/router">
           '''
formEnd = ''' <p>＜処理＞</p>
                 <p>
                    <input type="radio" name="procSelect" value="select">選択
                    <input type="radio" name="procSelect" value="insert">新規
                    <input type="radio" name="procSelect" value="update">更新
                    <input type="radio" name="procSelect" value="delete">削除
                  </p>
                <p><input type="submit" value="送信"></p>
              </form>
          '''

#
# HTML <table>......</table>
#
tableTh = '''  <p>＜会社一覧＞</p>
               <table border="1" width="900" cellspacing="0" cellpadding="5" bordercolor="#333333">
                  <tr>
                    <th bgcolor="#a9a9a9" width="10"><font color="#FFFFFF"></font></th>
                    <th bgcolor="#a9a9a9" width="150"><font color="#FFFFFF">会社ID</font></th>
                    <th bgcolor="#a9a9a9" width="150"><font color="#FFFFFF">会社名</font></th>
                    <th bgcolor="#a9a9a9" width="200"><font color="#FFFFFF">電話番号</font></th>
                    <th bgcolor="#a9a9a9" width="200"><font color="#FFFFFF">住所</font></th>
                    <th bgcolor="#a9a9a9" width="200"><font color="#FFFFFF">説明</font></th>
                  </tr>
          '''
tableTd = '''     <tr>
                    <td bgcolor="{5}" align="center" width="10"><input type="radio" name="companyId" value="{0}"></td>
                    <td bgcolor="{5}" valign="top" width="150">{0}</td>
                    <td bgcolor="{5}" valign="top" width="200">{1}</td>
                    <td bgcolor="{5}" valign="top" width="200">{2}</td>
                    <td bgcolor="{5}" valign="top" width="200">{3}</td>
                    <td bgcolor="{5}" valign="top" width="200">{4}</td>
                  </tr>
          '''
tableTc = '''   </table>
          '''

#
# HTML <input>......</input>
#      <textarea>...</textarea>
#
inputTextarea = '''  <p>＜会社更新＞</p>
                     <p>会社ID:{0}</p>
                     <p>会社名:<input type="text" name="companyName" size="40" value="{1}"></p>
                     <p>電話番号:<input type="text" name="telephoneNumber" size="40" value="{2}"></p>
                     <p>住所:<textarea name="address" rows="2" cols="60" >{3}</textarea></p>
                     <p>説明:<textarea name="discription" rows="5" cols="60">{4}</textarea></p>
                '''


#
# DB初期化
#
def initdb():
    with closing(sqlite3.connect(dbname)) as conn:
        # カーソル取得
        cur = conn.cursor()
        # executeメソッドでSQL文を実行する
        cur.execute(dropTable)
        cur.execute(createTable)
        # executemanyメソッドを実行する
        cur.executemany(insertTable, insertData)
        # コミット
        conn.commit()


#
# DBからデータを取得
#
def selectData():
    rowData = list()
    with closing(sqlite3.connect(dbname)) as conn:
        # カーソル取得
        cur = conn.cursor()
        # executeメソッドでSQL文を実行する
        for row in cur.execute(selectTable):
            # データを追加
            rowData.append(row)
    return rowData


#
# DBへデータを追加 insertData名はNG
#
def addData(requestForm):
    maxcompanyId = ''
    rowData = list()
    with closing(sqlite3.connect(dbname)) as conn:
        # カーソル取得
        cur = conn.cursor()
        for maxcompanyId in cur.execute(selectMaxcompanyId):
            pass
        i = str(int(maxcompanyId[0]) + 1).zfill(8)
        row = (i, requestForm['companyName'], requestForm['telephoneNumber'], requestForm['address'],
               requestForm['discription'])
        cur.execute(insertTable, row)
        conn.commit()
    return i


#
# DBのデータを更新
#
def updateData(requestForm):
    with closing(sqlite3.connect(dbname)) as conn:
        # カーソル取得
        cur = conn.cursor()
        row = (
            requestForm['companyName'], requestForm['telephoneNumber'], requestForm['address'],
            requestForm['discription'],
            requestForm['companyId'])
        cur.execute(editTable, row)
        conn.commit()
    return requestForm['companyId']


#
# DBからデータを削除
#
def deleteData(companyId):
    with closing(sqlite3.connect(dbname)) as conn:
        # カーソル取得
        cur = conn.cursor()
        row = (companyId)
        cur.execute(delTable, row)
        # cur.execute("delete from company WHERE companyId='?'",companyId)
        conn.commit()


#
# テーブルタグ編集
#
def makeHtml(companyId):
    # DBからデータを取得
    rowList = selectData()
    htmlBuff = formStat + tableTh
    htmlBuff2 = inputTextarea.format('', '', '', '', '')
    for row in rowList:
        if companyId == row[0]:
            htmlBuff = htmlBuff + tableTd.format(row[0], row[1], row[2], row[3], row[4], '#ffc0cb')
            htmlBuff2 = inputTextarea.format(row[0], row[1], row[2], row[3], row[4])
        else:
            htmlBuff = htmlBuff + tableTd.format(row[0], row[1], row[2], row[3], row[4], '#F2F2F2')
    htmlBuff = htmlBuff + tableTc + htmlBuff2 + formEnd
    return htmlBuff


@app.route('/')
def index():
    return makeHtml('')


@app.route('/router', methods=['POST'])
def router():
    if request.form['procSelect'] == 'select':
        return makeHtml(request.form['companyId'])
    if request.form['procSelect'] == 'insert':
        companyId = addData(request.form)
        return makeHtml(companyId)
    if request.form['procSelect'] == 'update':
        updateData(request.form)
        return makeHtml(request.form['companyId'])
    if request.form['procSelect'] == 'delete':
        deleteData(request.form['companyId'])
        return makeHtml('')


if __name__ == '__main__':
    initdb()
    app.debug = True
    app.run(host='127.0.0.1', port=8080)
