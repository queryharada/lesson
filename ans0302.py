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


def intToHex(val):
    if val == 0:
        return '00'

    i = 0
    hexStr = ''
    digits = 0
    while val > 0:
        modV = val % 16
        hexStr += hexString[modV]
        val = int(val / 16)
    return hexStr[::-1]


numList = []
while len(numList) < 2:
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
minValue = -1
maxValue = 0
totValue = 0
for v in numList:
    if (minValue == -1) or (v < minValue):
        minValue = v
    if v > maxValue:
        maxValue = v
    totValue += v

print('min value :',intToHex(minValue))
print('max value :',intToHex(maxValue))
print('total value :',intToHex(totValue))

if __name__ == "__main__":
    pass
