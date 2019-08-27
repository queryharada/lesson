# -*- coding: utf-8 -*-
import codecs
import unicodedata

filePathA = "C:/Users/harada/001/A.TXT"
filePathB = "C:/Users/harada/001/B.TXT"
filePathC = "C:/Users/harada/001/C.TXT"


#
# 漢字が含まれる場合の桁数(表示)取得
# ただし、表示フォントは等倍指定でないとカラムがズレる。
#
def columLen(lineStr):
    columLenRes = 0
    for c in lineStr:
        # 2桁文字(漢字)?
        if unicodedata.east_asian_width(c) in 'FWA':
            columLenRes = columLenRes + 2
        else:
            columLenRes = columLenRes + 1
    return columLenRes


# 初期化
lineReadA = ' '
lineReadB = ' '
lineWrite = ''
maxColun = 80
rowNum = 1

# ファイルストリーム取得
with codecs.open(filePathA, 'r', 'utf-8') as fsA, \
        codecs.open(filePathB, 'r', 'utf-8') as fsB, \
        codecs.open(filePathC, 'w', 'utf-8') as fsC:
    # ファイル名出力
    lineWrite = str(0).zfill(3) + ':' + filePathA.ljust(maxColun) + '|' + filePathB
    fsC.write(lineWrite + '\n')
    print(lineWrite)

    # 罫線出力
    lineWrite = str(0).zfill(3) + ':' + ('-' * maxColun) + '|' + ('-' * maxColun)
    fsC.write(lineWrite + '\n')
    print(lineWrite)

    # ファイルA、ファイルBをすべてリードするまで
    while lineReadA or lineReadB:
        # ファイルAを1行リード
        lineReadA = fsA.readline()
        if lineReadA == "":
            # データがない
            lineWriteB = ' ' * maxColun
        else:
            # スペース調整
            lineWriteA = lineReadA.replace('\n','') + (' ' * (maxColun - columLen(lineReadA.replace('\n',''))))

        # ファイルBを1行リード
        lineReadB = fsB.readline()
        if lineReadB == "":
            # データがない
            lineWriteB = ' ' * maxColun
        else:
            # スペース調整
            lineWriteB = lineReadB.replace('\n','') + (' ' * (maxColun - columLen(lineReadB.replace('\n',''))))

        # 行番号 + ':' + ファイルAの行 + ':' + ファイルBの行 を連結、出力
        lineWrite = str(rowNum).zfill(3) + ':' + lineWriteA + '|' + lineWriteB
        fsC.write(lineWrite + '\n')
        print(lineWrite)
        # 行番号 + 1
        rowNum = rowNum + 1