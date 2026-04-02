#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# no copyright, this was optimized by AI


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right
            else:
                return

    def contains(self, value):
        current = self.root
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False


if __name__ == "__main__":
    bst = BST()
    assert bst.contains(10) is False

    bst.insert(10)
    assert bst.contains(10) is True
    assert bst.contains(5) is False

    bst.insert(5)
    bst.insert(15)
    bst.insert(12)
    assert bst.contains(5) is True
    assert bst.contains(15) is True
    assert bst.contains(12) is True
    assert bst.contains(99) is False
