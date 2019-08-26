# -*- coding:utf-8 -*-

hexString = '0123456789ABCDEF'


def hexToInt(hexStr):
    i = len(hexStr)
    value = 0
    digits = 0
    while i > 0:
        value += hexString.find(hexStr[i - 1]) * (16 ** digits)
        i -= 1
        digits += 1
    return value


numList = []
while len(numList) < 4:
    inputStr = input("Please Enter Number(HEX): ")
    inputStr = inputStr.upper()
    isNumChk = True
    for oneChar in inputStr:
        if not oneChar in hexString:
            isNumChk = False

    if isNumChk:
        inputVal = hexToInt(inputStr)
        numList.append(inputVal)
    else:
        print('Enter Number is not HEX format')

print(numList)
minValue = 0
maxValue = 0
totValue = 0
for v in numList:
    if v < minValue:
        minValue = v
    if v > maxValue:
        maxValue = v
    totValue += v

print('min value :')

if __name__ == "__main__":
    pass
