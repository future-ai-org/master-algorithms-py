#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch


def get_gcd(n1, n2) -> int:

    result = 0
    assert(n1 > n2)

    while (n2 != 0):
        result = n2
        n1, n2 = n2, n1 % n2


if __name__ == '__main__':
    
    n1, n2 = 21, 12
    get_gcd(n1, n2)