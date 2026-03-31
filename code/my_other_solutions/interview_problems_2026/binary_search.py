#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch


def bs_iter(nums, n) -> int:

    if len(nums) == 0:
        return False
    low, high = 0, len(nums)
    
    while low < high:
        i = (high + low) // 2
        if nums[i] == n:
            return i
        elif nums[i] > n:
            high = i - 1
        else:
            low = i + 1

    return False


def bs_matrix_iter(m, n):

    if not m:
        return None

    rows = len(m)
    cols = len(m[0])

    low, high = 0, rows * cols

    while low < high:

        i = (high + low) // 2
        row = i // rows
        col = i % rows
        item = m[row][col]

        if item == n:
            return [row, col]
        
        elif item > n:
            high = i - 1
        
        else:
            low = i + 1
        


def bs_rec(nums, n, high=None, low=0):

    high = high or len(nums)
    
    if high < low:
        return False

    i = (high + low) // 2

    if nums[i] == n:
        return i

    elif nums[i] > n:
        return bs_rec(nums, n, i - 1, low)
    
    else:
        return bs_rec(nums, n, high, i + 1)


if __name__ == '__main__':    

    nums = [2, 4, 6, 7, 8, 9, 13, 19, 20, 88]
    n = 14
    assert(bs_iter(nums, n) == False)  
    assert(bs_iter(nums, n) == False)  
    n = 13
    assert(bs_rec(nums, n) == 6)
    assert(bs_rec(nums, n) == 6)


    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n = 6
    assert(bs_matrix_iter(m, n) == [1, 2])
    n = 12
    assert(bs_matrix_iter(m, n) == None)
