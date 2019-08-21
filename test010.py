# -*- coding:utf-8 -*-

def rj(num, digit):
    numStr = str(num)
    padingDigit = digit - len(numStr)
    return ' ' * padingDigit + numStr


for i in range(1, 10):
    line = ''
    for j in range(1, 10):
        # line += str(i*j).rjust(4)
        line += rj(i * j, 4)
    print(line)
