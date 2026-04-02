#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# no copyright, this was optimized by AI

'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
'''

from collections import OrderedDict


class LRUCache:
    """LRU via OrderedDict: order is oldest → newest; move_to_end marks recent; popitem(False) evicts LRU."""

    def __init__(self, capacity: int) -> None:
        self._cap = capacity
        self._data: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self._data:
            return -1
        self._data.move_to_end(key)
        return self._data[key]

    def put(self, key: int, value: int) -> None:
        if key in self._data:
            self._data[key] = value
            self._data.move_to_end(key)
            return
        if len(self._data) >= self._cap:
            self._data.popitem(last=False)
        self._data[key] = value


if __name__ == '__main__':
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)  # evicts key 2
    assert c.get(2) == -1
    c.put(4, 4)  # evicts key 1
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4