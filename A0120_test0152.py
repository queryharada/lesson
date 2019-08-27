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

#
# HTML <table>......</table>
#
tableTh = '''<form method="post" action="/select">
                <table border="1" width="900" cellspacing="0" cellpadding="5" bordercolor="#333333">
                  <tr>
                    <th bgcolor="#a9a9a9" width="10"><font color="#FFFFFF">check</font></th>
                    <th bgcolor="#a9a9a9" width="100"><font color="#FFFFFF">seq no.</font></th>
                    <th bgcolor="#a9a9a9" width="150"><font color="#FFFFFF">companyId</font></th>
                    <th bgcolor="#a9a9a9" width="150"><font color="#FFFFFF">companyName</font></th>
                    <th bgcolor="#a9a9a9" width="200"><font color="#FFFFFF">telephoneNumber</font></th>
                    <th bgcolor="#a9a9a9" width="200"><font color="#FFFFFF">address</font></th>
                    <th bgcolor="#a9a9a9" width="200"><font color="#FFFFFF">discription</font></th>
                  </tr>
          '''
tableTd = '''     <tr>
                    <td bgcolor="{6}" align="center" width="10"><input type="radio" name="companyId" value="{1}"></td>
                    <td bgcolor="{6}" align="center" nowrap>{0}</td>
                    <td bgcolor="{6}" valign="top" width="150">{1}</td>
                    <td bgcolor="{6}" valign="top" width="200">{2}</td>
                    <td bgcolor="{6}" valign="top" width="200">{3}</td>
                    <td bgcolor="{6}" valign="top" width="200">{4}</td>
                    <td bgcolor="{6}" valign="top" width="200">{5}</td>
                  </tr>
          '''
tableTc = '''   </table>
                <p><input type="submit" value="送信"></p>
             </form>

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
# テーブルタグ編集
#
def makeTable(companyId):
    # DBからデータを取得
    rowList = selectData()
    # <table><th>タグ
    htmlBuff = tableTh
    seqNo = 1
    # <td>タグ
    for row in rowList:
        if companyId == row[0]:
            htmlBuff = htmlBuff + tableTd.format(seqNo, row[0], row[1], row[2], row[3], row[4], '#ffc0cb')
        else:
            htmlBuff = htmlBuff + tableTd.format(seqNo, row[0], row[1], row[2], row[3], row[4], '#F2F2F2')
        seqNo += 1
    # </table>タグ
    htmlBuff = htmlBuff + tableTc
    return htmlBuff


@app.route('/')
def index():
    return makeTable('')


@app.route('/select', methods=['POST'])
def select():
    return makeTable(request.form['companyId'])


if __name__ == '__main__':
    initdb()
    app.debug = True
    app.run(host='127.0.0.1', port=8080)
