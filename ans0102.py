# -*- coding:utf-8 -*-
#
# 文字列のリバース
#
def stringRevers(stringBuff):
    stringRes = ""
    i = len(stringBuff)
    while i > 0:
        stringRes += stringBuff[i-1:i]
        i -= 1
    return stringRes


if __name__ == '__main__':
    stringBuff = ["afasga", \
                  "abcnhek", \
                  "ADHdh", \
                  "漢字コードを含む", \
                  "む漢字コードを含む",
                  ]
    print("### stringRevers")
    for s in stringBuff:
        print(s+"\t->"+stringRevers(s))

