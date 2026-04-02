#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# no copyright, this was optimized by AI


'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321
Example 2:
Input: x = -123
Output: -321
Example 3:
Input: x = 120
Output: 21
'''


INT_MAX = 2**31 - 1


def reverse_int(x: int) -> int:
    """Reverse decimal digits; return 0 if result is outside signed 32-bit range."""
    negative = x < 0
    x = abs(x)
    rev = 0
    while x:
        d = x % 10
        x //= 10
        if negative:
            # Result will be -rev; must stay >= INT_MIN (-2147483648)
            if rev > 214748364 or (rev == 214748364 and d > 8):
                return 0
        else:
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and d > INT_MAX % 10):
                return 0
        rev = rev * 10 + d
    return -rev if negative else rev


if __name__ == '__main__':
    assert reverse_int(123) == 321
    assert reverse_int(-123) == -321
    assert reverse_int(120) == 21
    assert reverse_int(1534236469) == 0
    assert reverse_int(-2147483648) == 0  # reversed magnitude overflows positive bound
