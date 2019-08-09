# -*- coding:utf-8 -*-

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
# HTML作成
#
def makeHtml(rowList, companyId=''):
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


if __name__ == "__main__"
    pass
