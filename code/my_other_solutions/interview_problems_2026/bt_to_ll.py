#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# no copyright, this was optimized by AI


'''
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
'''

from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root: TreeNode | None) -> None:
    """Pre-order flatten in place: follow right pointers; left is always None.

    At each node with a left child, the rightmost node of that left subtree is
    the last vertex visited before the original right subtree in preorder, so
    we hang the old right subtree off it, then promote the left subtree to the right.
    """
    cur = root
    while cur:
        if cur.left:
            pre = cur.left
            while pre.right:
                pre = pre.right
            pre.right = cur.right
            cur.right = cur.left
            cur.left = None
        cur = cur.right
