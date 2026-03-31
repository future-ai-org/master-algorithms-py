#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch


def reverse_string_inplace(s):
    if s:
        s = s[-1] + reverse_string_inplace(s[:-1])
    return s


def reverse_string_inplace2(s):
    return s[::-1]


if __name__ == '__main__':  
    s = 'hello'
    assert(reverse_string_inplace(s) == 'olleh')
    assert(reverse_string_inplace2(s) == 'olleh')
    s = ''
    assert(reverse_string_inplace(s) == '')
    assert(reverse_string_inplace2(s) == '')