#!/usr/bin/env python
# Copyright (c) Marina von Steinkirch

__author__ = "bt3"

filename = raw_input('Enter a file name: ')
try:
    f = open(filename, "r")
except:
    print 'There is no file named', filename

