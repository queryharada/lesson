# -*- coding:utf-8 -*-

BASESTRING = '0123456789ABCDEF'
ENTERCOUNT = 4


# HEX文字列を数値へ変換
def hexToInt(hexStr):
    i = len(hexStr)
    value = 0
    digits = 0
    while i > 0:
        value += BASESTRING.find(hexStr[i - 1]) * (len(BASESTRING) ** digits)
        i -= 1
        digits += 1
    return value


# 数値をHEX文字列へ変換
def intToHex(intVal):
    if intVal == 0:
        return '00'
    i = 0
    hexStr = ''
    while intVal > 0:
        modV = intVal % len(BASESTRING)
        hexStr += BASESTRING[modV]
        intVal = int(intVal / len(BASESTRING))
    # 文字列をリバース
    return hexStr[::-1]

# HEX文字列入力
numList = []
while len(numList) < ENTERCOUNT:
    inputStr = input("Please Enter Number(HEX): ")
    inputStr = inputStr.upper()

    # HEX文字列チェック
    isNumChk = True
    for oneChar in inputStr:
        if not oneChar in BASESTRING:
            isNumChk = False

    if isNumChk:
        inputVal = hexToInt(inputStr)
        numList.append(inputVal)
    else:
        print('Enter Number is not HEX format')

# 最小最大を求める
minValue = -1
maxValue = 0
totValue = 0
for v in numList:
    if (minValue == -1) or (v < minValue):
        minValue = v
    if v > maxValue:
        maxValue = v
    totValue += v

# 最小最大平均を出力
print(numList)
print('min value     :', intToHex(minValue))
print('max value     :', intToHex(maxValue))
print('total value   :', intToHex(totValue))
print('average value :', intToHex(int(totValue / ENTERCOUNT)))

if __name__ == "__main__":
    pass
