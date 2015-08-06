#!/usr/bin/env python
# -*- coding: utf-8 -*-

i = 0 
j = 0

for i in xrange(4):
    for j in xrange(4-i-1):
        print ' ',
    for j in xrange(i*2+1):
        print '*',
    print 
