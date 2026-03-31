#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch


def get_fib_element(n):

    if n < 3:
        return n
    return get_fib_element(n - 1) + get_fib_element(n - 2)


def get_fib_sequence(n):

    if n < 3:
        return 1

    a, b, i = 0, 1, 0
    seq = set()

    while i < n:
        seq.add(a)
        seq.add(b)
        a, b, i = b, a + b, i + 1

    return sorted(list(seq))


if __name__ == "__main__":
    print(get_fib_sequence(10))