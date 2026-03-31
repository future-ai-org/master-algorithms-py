#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch


def is_palindrome_iter(s) -> bool:

    if len(s) < 2:
        return True

    i = 0

    while i < len(s)//2 + 1:

        if s[i] != s[-i-1]:
            return False
        
        i += 1

    return True


def is_palindrome_rec(s) -> bool:

    if len(s) < 2:
        return True

    if s[0] == s[-1]:
        return is_palindrome_rec(s[1:-1])
    else:
        return False


if __name__ == "__main__":

    assert(is_palindrome_iter('subinoonibus') == True)
    assert(is_palindrome_iter('hello') == False)
    assert(is_palindrome_iter('m') == True)
    assert(is_palindrome_iter('') == True)

    assert(is_palindrome_rec('subinoonibus') == True)
    assert(is_palindrome_rec('hello') == False)
    assert(is_palindrome_rec('m') == True)
    assert(is_palindrome_rec('') == True)
