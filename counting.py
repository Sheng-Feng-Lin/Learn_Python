#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = 'Please count the characters here'
d = {}

for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

print d 
