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


if __name__ == '__main__':    

    nums = [2, 4, 6, 7, 8, 9, 13, 19, 20, 88]

    n = 14
    assert(bs_iter(nums, n) == False)  
    
    n = 13
    assert(bs_iter(nums, n) == 6)  

