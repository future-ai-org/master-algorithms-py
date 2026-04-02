#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# no copyright, this was optimized by AI

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def to_list(self):
        return list(self)


if __name__ == "__main__":
    ll = LinkedList()
    assert ll.to_list() == []

    ll.append(10)
    assert ll.to_list() == [10]

    ll.append(20)
    ll.append(30)
    assert ll.to_list() == [10, 20, 30]

    assert list(ll) == [10, 20, 30]
