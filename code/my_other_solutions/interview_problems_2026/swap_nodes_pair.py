#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# no copyright, this was optimized by AI

'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''

from __future__ import annotations

from linked_list import Node


def swap_pairs(head: Node | None) -> Node | None:
    """Swap every two adjacent nodes by rewiring pointers — O(n) time, O(1) extra space."""
    dummy = Node(0, head)
    prev = dummy
    while prev.next is not None and prev.next.next is not None:
        first = prev.next
        second = first.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return dummy.next


def _values(head: Node | None) -> list[int]:
    out: list[int] = []
    while head is not None:
        out.append(head.value)
        head = head.next
    return out


def _from_values(values: list[int]) -> Node | None:
    if not values:
        return None
    head = Node(values[0])
    cur = head
    for v in values[1:]:
        cur.next = Node(v)
        cur = cur.next
    return head


if __name__ == '__main__':
    assert _values(swap_pairs(_from_values([1, 2, 3, 4]))) == [2, 1, 4, 3]
    assert _values(swap_pairs(_from_values([]))) == []
    assert _values(swap_pairs(_from_values([1]))) == [1]
    assert _values(swap_pairs(_from_values([1, 2, 3]))) == [2, 1, 3]

