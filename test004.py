#! /usr/bin/env python
# -*- coding: utf-8 -*-
import itertools

i = 0
seq = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
for element in itertools.permutations(seq, len(seq)):
    # print(element)
    print("".join(element))
    i += 1
print(i)
