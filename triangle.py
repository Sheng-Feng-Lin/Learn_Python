#!/usr/bin/env python
# -*- coding: utf-8 -*-

for i in xrange(4, 0, -1): # for loop 4, 3, 2, 1.
    for j in xrange(4-i):
        print ' ',
    for j in xrange(i*2-1):
        print '*',
    print 
