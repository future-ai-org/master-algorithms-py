#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# no copyright, this was optimized by AI

"""
Sorted array, in-place: keep at most two copies of each value.
Return k = length of the valid prefix; O(1) extra space.
"""


def remove_duplicates(nums: list[int]) -> int:
    if len(nums) <= 2:
        return len(nums)
    # write is where the next kept element goes; first two are always kept
    write = 2
    for read in range(2, len(nums)):
        # Third (or more) copy of same value equals nums[write-2]
        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1
    return write


if __name__ == '__main__':
    def check(nums: list[int], expected_prefix: list[int]) -> None:
        k = remove_duplicates(nums)
        assert k == len(expected_prefix)
        assert nums[:k] == expected_prefix

    check([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3])
    check([0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3])
    check([1], [1])
    check([1, 1], [1, 1])
