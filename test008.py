# -*- coding: utf-8 -*-
import codecs


filePathA = "C:/Users/harada/Desktop/A.TXT"
filePathB = "C:/Users/harada/Desktop/B.TXT"

f = codecs.open(filePathA, 'r', 'utf-8')
line = f.readline()
while line:
    line = f.readline()
    print(line)

f.close()
