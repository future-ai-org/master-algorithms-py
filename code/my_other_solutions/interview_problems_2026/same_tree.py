#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch

'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
 
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''

class TreeNode:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def isSameTree(p, q) -> bool:

    if p.value != q.value:
        return False

    if p.left is None and q.left is None: 
        return True
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right) 



if __name__ == "__main__":

    p = TreeNode(1, TreeNode(2), TreeNode(4))
    q = TreeNode(1, TreeNode(2), TreeNode(4))
    assert(isSameTree(p, q) == True)

    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(4))
    assert(isSameTree(p, q) == False)

    p = TreeNode(0, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert(isSameTree(p, q) == False)

    p = TreeNode(1, TreeNode(3))
    q = TreeNode(1, TreeNode(2))
    assert(isSameTree(p, q) == False)