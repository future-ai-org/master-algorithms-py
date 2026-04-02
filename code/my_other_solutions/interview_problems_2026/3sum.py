#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# no copyright, this was optimized by AI

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
'''


def three_sum(nums: list[int]) -> list[list[int]]:
    """All unique triplets that sum to zero — O(n^2) time, O(1) extra space (excluding output)."""
    nums.sort()
    n = len(nums)
    out: list[list[int]] = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        left, right = i + 1, n - 1
        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                out.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return out


if __name__ == '__main__':
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]

