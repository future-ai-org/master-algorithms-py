#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch

'''
Given an array nums of distinct integers, return all the possible permutations.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
 
Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

from collections import Counter


def permutations(nums) -> list:

    if len(nums) < 2:
        return [nums]

    result = []

    for i in range(len(nums)):

        pivot = [nums[i]]
        remaining = nums[:i] + nums[i+1:]
        for permutation in permutations(remaining):
            result.append(pivot + perm)
        
    return result


def is_permutation(l1, l2) -> bool:
    
    counter = Counter()
    for i in l1:
        counter[i] +=1
    for i in l2:
        counter[i] -= 1
    for v in counter.values():
        if v != 0:
            return False
    return True


if __name__ == '__main__':

    assert(permutations([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
    assert(permutations([0,1]) == [[0,1],[1,0]])
    assert(permutations([1]) == [[1]])
    