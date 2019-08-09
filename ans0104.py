# -*- coding:utf-8 -*-
#
# 文字列内のスペースを %20 に置換する。
#

def stringSort(stringBuff):
    stringListArray = list()
    for oneChar in stringBuff:
        stringListArray.append(oneChar)
    stringListArray.sort()
    stringRes = ""
    for oneChar in stringListArray:
        stringRes += oneChar
    return stringRes


def stringAnagramCheck(stringBuff1, stringBuff2):
    return stringSort(stringBuff1) == stringSort(stringBuff2)


if __name__ == '__main__':
    stringBuff = [("afasga", "faagsa"), \
                  ("abcnhek", "abanhek"), \
                  ("ADHdh", "ADHdh"), \
                  ("漢字コードを含む", "漢字コードを含む"), \
                  ("む漢字コードを含む", "む漢字コドを含む")
                  ]
    print("### stringAnagramCheck")
    for s in stringBuff:
        print(s[0] + "\t:" + s[1] + "\t:" + str(stringAnagramCheck(s[0], s[1])))
