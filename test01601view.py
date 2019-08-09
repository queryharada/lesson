# -*- coding:utf-8 -*-

#
# HTML <form>......</form>
#
formStat = '''<div style="margin : 20px">
                <form method="post" action="/router">
           '''
formEnd = '''       <p>＜処理＞</p>
                        <p>
                            <input type="radio" name="procSelect" value="select">選択
                            <input type="radio" name="procSelect" value="insert">新規
                            <input type="radio" name="procSelect" value="update">更新
                            <input type="radio" name="procSelect" value="delete">削除
                        </p>
                    <p>{0}</P>
                    <p><input type="submit" value="送信"></p>
                </form>
              </div>
          '''

#
# HTML <table>......</table>
#
tableTh = '''       <p>＜会社一覧＞</p>
                    <table border="0" width="900" cellspacing="0" cellpadding="5" bordercolor="#ffffff">
                          <tr>
                            <th bgcolor="#ffffff" align="center" width="10"><font color="#000000"></font></th>
                            <th bgcolor="#ffffff" align="left" width="150"><font color="#000000">会社ID</font></th>
                            <th bgcolor="#ffffff" align="left" width="150"><font color="#000000">会社名</font></th>
                            <th bgcolor="#ffffff" align="left" width="200"><font color="#000000">電話番号</font></th>
                            <th bgcolor="#ffffff" align="left" width="200"><font color="#000000">住所</font></th>
                            <th bgcolor="#ffffff" align="left" width="200"><font color="#000000">説明</font></th>
                          </tr>
          '''
tableTd = '''             <tr>
                            <td bgcolor="{5}" align="center" width="10"><input type="radio" name="companyId" value="{0}" {6}></td>
                            <td bgcolor="{5}" valign="top" width="150">{0}</td>
                            <td bgcolor="{5}" valign="top" width="200">{1}</td>
                            <td bgcolor="{5}" valign="top" width="200">{2}</td>
                            <td bgcolor="{5}" valign="top" width="200">{3}</td>
                            <td bgcolor="{5}" valign="top" width="200">{4}</td>
                          </tr>
          '''
tableTc = '''       </table>
          '''

#
# HTML <input>......</input>
#      <textarea>...</textarea>
#
inputTextarea = ''' <p>＜会社更新＞</p>
                    <p>会社ID　:{0}</p>
                    <p>会社名　:<input type="text" name="companyName" size="40" value="{1}"></p>
                    <p>電話番号:<input type="text" name="telephoneNumber" size="40" value="{2}"></p>
                    <p>住所　　:<textarea name="address" rows="2" cols="60" >{3}</textarea></p>
                    <p>説明　　:<textarea name="discription" rows="5" cols="60">{4}</textarea></p>
                '''

#
# メッセージ
#
footerMessage = dict()
footerMessage['000'] = '<br>'
footerMessage['001'] = '処理が選択されていません'
footerMessage['002'] = '会社Idは99999999を超えて採番できません'
footerMessage['003'] = '会社一覧が選択されていません'


#
# HTML作成
#
def makeHtml(rowList, companyId='', messageId='000'):
    htmlBuff = formStat + tableTh
    htmlBuff2 = inputTextarea.format('', '', '', '', '')

    for row in rowList:
        address = row[3]
        if len(address) > 30:
            address = address[:30]

        description = row[4]
        if len(description) > 30:
            description = description[:30]

        if companyId == row[0]:
            htmlBuff = htmlBuff + \
                       tableTd.format(row[0], row[1], row[2], address, description, '#c0c0c0', 'checked="checked"')
            htmlBuff2 = inputTextarea.format(row[0], row[1], row[2], row[3], row[4])
        else:
            htmlBuff = htmlBuff + \
                       tableTd.format(row[0], row[1], row[2], address, description, '#ffffff', '')

    htmlBuff = htmlBuff + \
               tableTc + \
               htmlBuff2 + \
               formEnd.format(footerMessage[messageId])

    return htmlBuff