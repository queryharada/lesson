# -*- coding:utf-8 -*-
#
# 文字列のアナグラムチェック
#

# 文字列ソートによる比較
def stringSort(stringBuff):
    stringListArray = list()
    for oneChar in stringBuff:
        stringListArray.append(oneChar)
    stringListArray.sort()
    stringRes = ""
    for oneChar in stringListArray:
        stringRes += oneChar
    return stringRes


def stringAnagramCheck1(stringBuff1, stringBuff2):
    return stringSort(stringBuff1) == stringSort(stringBuff2)


# 文字数による比較
def stringCharCount(stringBuff):
    oneCharDict = dict()
    for oneChar in stringBuff:
        if oneChar in oneCharDict:
            oneCharDict[oneChar] += 1
        else:
            oneCharDict[oneChar] = 1
    return oneCharDict


def stringAnagramCheck2(stringBuff1, stringBuff2):
    return stringCharCount(stringBuff1) == stringCharCount(stringBuff2)


if __name__ == '__main__':
    stringBuff = [("afasga", "faagsa"),
                  ("abcnhek", "abanhek"),
                  ("ADHdh", "ADHdh"),
                  ("漢字コードを含む", "漢字コードを含む"),
                  ("む漢字コードを含む", "む漢字コドを含む")
                  ]
    print("### stringAnagramCheck1")
    for s in stringBuff:
        print(s[0] + "\t:" + s[1] + "\t:" + str(stringAnagramCheck1(s[0], s[1])))
    print("")
    print("### stringAnagramCheck2")
    for s in stringBuff:
        print(s[0] + "\t:" + s[1] + "\t:" + str(stringAnagramCheck2(s[0], s[1])))
