# -*- coding:utf-8 -*-
import sqlite3
from contextlib import closing

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
initData = [
    ('99999998', 'ABC', '0354762911', '住所', '説明'),
    ('00000001', 'ABC1', '0422111163', '住所１', '説明１'),
    ('00000002', 'ABC2', '08012345678', '住所２', '説明２'),
    ('00000003', 'ABC3', '035476291', '住所３', '説明３'),
    ('00000004', 'ABC4', '035476291', '住所４', '説明４'),
    ('00000005', 'ABC5', '035476291', '住所５', '説明５')
]
selectTable = 'select * from company'

selectMaxcompanyId = 'select max(companyId) from company'
updateTable = 'UPDATE company SET companyName=?, telephoneNumber=?, address=?, discription=? WHERE companyId=?'
#  うまく展開しないため、formatで対応した
# delTable = 'DELETE from company WHERE companyId=? '
delTable = 'DELETE from company WHERE companyId="{0}" '


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
        cur.executemany(insertTable, initData)
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
def insertData(requestForm):
    maxcompanyId = ''
    with closing(sqlite3.connect(dbname)) as conn:
        # カーソル取得
        cur = conn.cursor()
        #  最大会社ID取得
        for v in cur.execute(selectMaxcompanyId):
            pass
        if v is not None:
            num = 0
        else:
            num = int(v[0]) + 1

        # チェック　companyId　
        if num > 99999999:
            return None
        # チェック　companyName 型、桁数
        if requestForm['companyName']:
            pass
        # チェック　telephoneNumber　型、桁数、数字、ハイフン
        if requestForm['telephoneNumber']:
            pass
            # チェック　address　型、桁数
        if requestForm['address']:
            pass

        maxcompanyId = str(num).zfill(8)
        row = (maxcompanyId, requestForm['companyName'], requestForm['telephoneNumber'], requestForm['address'],
               requestForm['discription'])
        cur.execute(insertTable, row)
        conn.commit()
    return maxcompanyId


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
        cur.execute(updateTable, row)
        conn.commit()
    return requestForm['companyId']


#
# DBからデータを削除
#
def deleteData(companyId):
    with closing(sqlite3.connect(dbname)) as conn:
        # カーソル取得
        cur = conn.cursor()
        cur.execute(delTable.format(companyId))
        conn.commit()
