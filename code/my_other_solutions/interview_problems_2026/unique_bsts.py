#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# no copyright

from __future__ import annotations

"""
Given n, return every structurally distinct BST that stores 1..n exactly once.
"""


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def _trees_between(lo: int, hi: int) -> list[TreeNode | None]:
    """All BSTs using values lo..hi inclusive."""
    if lo > hi:
        return [None]
    out: list[TreeNode] = []
    for root_val in range(lo, hi + 1):
        for left in _trees_between(lo, root_val - 1):
            for right in _trees_between(root_val + 1, hi):
                out.append(TreeNode(root_val, left, right))
    return out


def generate_unique_bsts(n: int) -> list[TreeNode | None]:
    if n == 0:
        return []
    return _trees_between(1, n)


def _is_bst(node: TreeNode | None, low: float, high: float) -> bool:
    if node is None:
        return True
    if not (low < node.value < high):
        return False
    return _is_bst(node.left, low, node.value) and _is_bst(node.right, node.value, high)


def _node_count(node: TreeNode | None) -> int:
    if node is None:
        return 0
    return 1 + _node_count(node.left) + _node_count(node.right)


def _catalan(k: int) -> int:
    if k <= 1:
        return 1
    return sum(_catalan(i) * _catalan(k - 1 - i) for i in range(k))


if __name__ == '__main__':
    for n in range(1, 5):
        trees = generate_unique_bsts(n)
        assert len(trees) == _catalan(n)
        for t in trees:
            assert _node_count(t) == n
            assert _is_bst(t, float('-inf'), float('inf'))

    assert len(generate_unique_bsts(3)) == 5
    assert len(generate_unique_bsts(1)) == 1
