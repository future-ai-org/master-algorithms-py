#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch

import math


def is_prime(num) -> bool:

    for i in range(2, int(math.sqrt(n))):
        if num % i == 0:
            return False
    return True


def get_divisors(num) -> list:
    return [d for d in range(2, num//2 + 1) if num % d == 0] + [1, num]


def get_next_prime(num) -> int:

    while 1:
        num += 1
        if is_prime(num):
            return num
        

if __name__ == "__main__":
    
    for n in range(1, 20):
        print(f'is {n} prime? {is_prime(n)}')

    num = 14
    print(get_divisors(num))
    print(get_next_prime(num))
