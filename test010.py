# -*- coding:utf-8 -*-

for i in range(1,10):
    line = ''
    for j in range(1,10):
        line += str(i*j).rjust(4)
    print(line)