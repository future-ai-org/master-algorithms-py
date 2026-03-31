#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch
# author: bt3gl


def permutations(string) -> list:

    if len(string) == 1:
        return [string]
    
    result = []
    for i, char in enumerate(string):
        for perm in permutation(string[:i] + string[i+1:]):
            result += [char + perm]
    
    return result
