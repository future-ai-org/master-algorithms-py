#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch


def combinations(array) -> set(): 

    if len(array) < 2:
        return set(array)

    result = set()
    for i, item in enumerate(array):
        new_array = array[:i] + array[i+1:]
        result.add(item)

        for combination in combinations(new_array):
            new_item = ''.join(sorted(item + combination))
            result.add(new_item)
    
    return result


if __name__ == '__main__':

    nums = ['a', 'b', 'c']
    result = set(['a', 'ac', 'ab', 'abc', 'bc', 'c', 'b']) 
    
    assert(combinations(nums) == result)
    
    nums = ['']
    result = set([''])
    
    assert(combinations(nums) == result)
    
    nums = ['a']
    result = set(['a'])
    
    assert(combinations(nums) == result)