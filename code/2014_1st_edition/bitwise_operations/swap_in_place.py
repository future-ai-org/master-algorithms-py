#!/usr/bin/env python
# Copyright (c) Marina von Steinkirch

__author__ = "bt3"

'''
    swapping values in place without extra memory
'''


def swap_bit(a, b):
    '''
    >>> swap_bit(14, 73)
    (73, 14)
    '''
    a = a^b
    b = a^b
    a = a^b
    return a, b


if __name__ == '__main__':
    import doctest
    doctest.testmod()