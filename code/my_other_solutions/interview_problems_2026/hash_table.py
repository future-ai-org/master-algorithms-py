#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# no copyright, this was optimized by AI


class HashTable:
    def __init__(self, size=16):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _index(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        bucket = self.buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key, default=None):
        bucket = self.buckets[self._index(key)]
        for k, v in bucket:
            if k == key:
                return v    # return v or not, that'the question...
        return default

    def delete(self, key):
        bucket = self.buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False


if __name__ == "__main__":
    table = HashTable(size=4)

    table.set("a", 1)
    table.set("b", 2)
    table.set("a", 3)  # update existing key

    assert table.get("a") == 3
    assert table.get("b") == 2
    assert table.get("missing") is None
    assert table.get("missing", 0) == 0

    assert table.delete("b") is True
    assert table.get("b") is None
    assert table.delete("b") is False
