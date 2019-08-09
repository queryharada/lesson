# -*- coding:utf-8 -*-
#
# 文字列に同じ文字が含まれるかチェックする。
# チェックバッファ使用。
#
def duplicateCharCheck1(stringBuff):
    oneCharDict = dict()
    for oneChar in stringBuff:
        if oneChar in oneCharDict:
            return True
        else:
            oneCharDict[oneChar] = True
    return False


#
# 文字列に同じ文字が含まれるかチェックする。
# チェックバッファは使用しない。
#   考え方::チェックする文字を除いた文字列を作成し、その中に存在すれば重複と判断する。
#
def duplicateCharCheck2(stringBuff):
    stringLen = len(stringBuff)
    for i in range(stringLen):
        if stringBuff[i:i + 1] in stringBuff[0:i] + stringBuff[i + 1:stringLen]:
            return True
    return False


if __name__ == '__main__':
    stringBuff = ["afasga",
                  "abcnhek",
                  "ADHdh",
                  "漢字コードを含む",
                  "む漢字コードを含む",
                  ]
    print("### duplicateCharCheck1")
    for s in stringBuff:
        if duplicateCharCheck1(s):
            print(s + "\t:" + "重複文字あり")
        else:
            print(s + "\t:" + "重複文字なし")
    print("")

    print("### duplicateCharCheck2")
    for s in stringBuff:
        if duplicateCharCheck2(s):
            print(s + "\t:" + "重複文字あり")
        else:
            print(s + "\t:" + "重複文字なし")
