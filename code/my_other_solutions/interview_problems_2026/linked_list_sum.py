#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch


''''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''


class ListNode:
     def __init__(self, value=0, next=None):
         self.value = value
         self.next = next


def create_list(l):
    head = ListNode(l[0])
    tail = head # do not forget you want to return the tail
    for item in l[1:]:
        tail.next = ListNode(item)
        tail = tail.next
    return head


def addTwoNumbers(l1, l2):
    n1 = create_list(l1)
    n2 = create_list(l2)
    result = []
    carry = 0
    while n1 or n2 or carry:
        v1 = n1.value if n1 else 0
        v2 = n2.value if n2 else 0
        total = v1 + v2 + carry
        carry = total // 10
        result.append(total % 10)
        if n1:
            n1 = n1.next
        if n2:
            n2 = n2.next
    return result


if __name__ == '__main__':
    assert addTwoNumbers([2, 4, 3], [5, 6, 4]) == [7, 0, 8]
    assert addTwoNumbers([0], [0]) == [0]
    assert addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]) == [8, 9, 9, 9, 0, 0, 0, 1]
    assert addTwoNumbers([9], [9]) == [8, 1]
    assert addTwoNumbers([5], [5]) == [0, 1]
