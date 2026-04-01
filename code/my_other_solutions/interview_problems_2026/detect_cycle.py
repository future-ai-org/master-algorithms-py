#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch

from node import Node

def has_cycle(head) -> bool:

    if not head:
        return False

    p1 = head
    p2 = head.next

    while p1 != p2:
        
        if not p1 or not p2 or not p2.next:
            return False

        p1 = p1.next
        p2 = p2.next.next

    return True


def detect_cycle_2(head):

    seen = set()
    node = head

    while node is not None:

        if node in seen:
            return node

        else:
            seen.add(node)
            node = node.next

    return False
  