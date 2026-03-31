#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch
# author: bt3gl

def reverse_bits(n: int) -> int:
        
        result, base = 0, 31
        
        while n:
            result += (n & 1) << base
            n >>= 1
            base -= 1
        
        return result
