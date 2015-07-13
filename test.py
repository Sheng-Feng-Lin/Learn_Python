#!/usr/bin/env python
# -*- coding: utf-8 -*-
def hello(name = None):
    if name:
        return 'Hello world %s !' % name
    else:
        return 'Hello world'

if __name__=='__main__':
    import sys

    print sys.argv

    if len(sys.argv) >= 2 :
        print hello(sys.argv[1])
    else:
	print hello()

