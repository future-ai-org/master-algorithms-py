#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch


from collections import Counter


def is_anagram(s1, s2):

    counter = Counter()

    for c in s1:
        counter[c] += 1

    for c in s2:
        counter[c] -= 1

    for v in counter.values():
        if v != 0:
            return False
    return True


def get_unicode_sum(word):
    s = 0
    for p in word:
        s += ord(p)
    return s


def is_anagram2(w1, w2):
    return get_unicode_sum(w1) == get_unicode_sum(w2)


if __name__ == '__main__':
    
    assert(is_anagram('cat', 'tac') == True)
    assert(is_anagram('cat', 'hat') == False)

    assert(is_anagram2('cat', 'tac') == True)
    assert(is_anagram2('cat', 'hat') == False)

