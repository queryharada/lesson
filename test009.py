# -*- coding: utf-8 -*-
import codecs

filePathA = "C:/Users/harada/001/test009.TXT"


#
# 英数字以外をスペースに置き換える
#
def spaceCovert(line):
    lineSp = ""
    for oneChar in line:
        if oneChar.isalnum():
            lineSp += oneChar
        else:
            lineSp += ' '
    return lineSp


with codecs.open(filePathA, 'r', 'utf-8') as fs:
    lineRead = ' '
    wordDict = dict()
    maxWordLen = 0

    while lineRead:
        # 1行リード
        lineRead = fs.readline()
        # 小文字に変換
        lineBuff = lineRead.lower()
        # 英数字以外をスペースに置き換える
        lineBuff = spaceCovert(lineBuff)
        # スペースを区切り記号として単語の抽出
        lineBuff = lineBuff.split(' ')
        # 単語ごとに処理
        for word in lineBuff:
            # 文字がある？
            if not (word == ""):
                if word in wordDict:
                    # 辞書に単語がすで登録
                    wordDict[word] += 1
                else:
                    # 辞書に単語がないので初期化
                    wordDict[word] = 1
                    if len(word) > maxWordLen:
                        maxWordLen = len(word)

    #
    # 結果表示
    #
    totalWordNum1 = 0
    totalWordNum2 = 0
    line = ""
    for key, value in sorted(wordDict.items(), key=lambda x: -x[1]):
        # for key, value in sorted(wordDict.items()):
        # print(str(key) + ": " + str(value))
        line = line + str(key).rjust(maxWordLen) + ": " + repr(value).rjust(3) + "  "
        if len(line) > 60:
            print(line)
            line = ""
        totalWordNum1 += value
        totalWordNum2 += 1

    print("TOTAL: " + str(totalWordNum2) + " / " + str(totalWordNum1))
