"""
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
"""

from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


def generate_trees(n: int) -> list[TreeNode | None]:
    """All BST shapes on labels 1..n (empty list if n == 0)."""
    if n == 0:
        return []

    def trees(lo: int, hi: int) -> list[TreeNode | None]:
        if lo > hi:
            return [None]
        out: list[TreeNode] = []
        for root_val in range(lo, hi + 1):
            for left in trees(lo, root_val - 1):
                for right in trees(root_val + 1, hi):
                    out.append(TreeNode(root_val, left, right))
        return out

    return trees(1, n)


if __name__ == '__main__':
    assert len(generate_trees(3)) == 5
    assert len(generate_trees(1)) == 1