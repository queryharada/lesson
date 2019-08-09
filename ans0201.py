# -*- coding:utf-8 -*-
#
# リスト内の重複する要素を削除する。
#
def duplicateListDelete(srcList):
    resDict = dict()
    for item in srcList:
        if not (item in resDict):
            resDict[item] = True

    resList = list()
    for keyName in resDict:
        resList.append(keyName)
    return resList


if __name__ == '__main__':
    srcList = ["afasga", \
               "漢字コードを含む", \
               "abcnhek", \
               "ADHdh", \
               "漢字コードを含む", \
               "ADHdh", \
               "漢字コードを含む", \
               "む漢字コードを含む",
               ]
    print("### duplicateListDelete")
    resList = duplicateListDelete(srcList)
    for s in resList:
        print(s)
