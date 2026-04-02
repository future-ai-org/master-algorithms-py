#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# no copyright, this was optimized by AI


'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.
'''

from __future__ import annotations

from linked_list import Node


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


def sorted_list_to_bst(head: Node | None) -> TreeNode | None:
    """Build a height-balanced BST by simulating in-order traversal over the list.

    Count nodes once, then recurse on index ranges: left subtree consumes the first
    half of nodes, the root takes the next list node, then the right subtree. A
    moving reference walks the list exactly once — O(n) time, O(log n) recursion depth.
    """
    n = 0
    p = head
    while p is not None:
        n += 1
        p = p.next

    cur: list[Node | None] = [head]

    def build(lo: int, hi: int) -> TreeNode | None:
        if lo >= hi:
            return None
        mid = (lo + hi) // 2
        left = build(lo, mid)
        node = cur[0]
        assert node is not None
        root = TreeNode(node.value)
        cur[0] = node.next
        root.left = left
        root.right = build(mid + 1, hi)
        return root

    return build(0, n)


def _inorder(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    return _inorder(root.left) + [root.val] + _inorder(root.right)


def _balanced_height(root: TreeNode | None) -> int | None:
    if root is None:
        return 0
    lh = _balanced_height(root.left)
    rh = _balanced_height(root.right)
    if lh is None or rh is None or abs(lh - rh) > 1:
        return None
    return 1 + max(lh, rh)


def _from_values(values: list[int]) -> Node | None:
    if not values:
        return None
    h = Node(values[0])
    t = h
    for v in values[1:]:
        t.next = Node(v)
        t = t.next
    return h


if __name__ == '__main__':
    for vals in ([], [1], [1, 2], [1, 2, 3, 4, 5], [-3, 0, 5, 9]):
        root = sorted_list_to_bst(_from_values(vals))
        assert _inorder(root) == vals
        assert _balanced_height(root) is not None
