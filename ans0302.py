# -*- coding:utf-8 -*-

BASESTRING = '0123456789ABCDEF'
ENTERCOUNT = 4


def hexToInt(hexStr):
    i = len(hexStr)
    value = 0
    digits = 0
    while i > 0:
        value += BASESTRING.find(hexStr[i - 1]) * (len(BASESTRING) ** digits)
        i -= 1
        digits += 1
    return value


def intToHex(val):
    if val == 0:
        return '00'
    i = 0
    hexStr = ''
    while val > 0:
        modV = val % len(BASESTRING)
        hexStr += BASESTRING[modV]
        val = int(val / len(BASESTRING))
    return hexStr[::-1]


numList = []
while len(numList) < ENTERCOUNT:
    inputStr = input("Please Enter Number(HEX): ")
    inputStr = inputStr.upper()
    isNumChk = True
    for oneChar in inputStr:
        if not oneChar in BASESTRING:
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

print('min value :', intToHex(minValue))
print('max value :', intToHex(maxValue))
print('total value :', intToHex(totValue))
print('average value :', intToHex(int(totValue / ENTERCOUNT)))

if __name__ == "__main__":
    pass
