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
def insertData(requestForm):
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

if __name__ == "__main__"
    pass
