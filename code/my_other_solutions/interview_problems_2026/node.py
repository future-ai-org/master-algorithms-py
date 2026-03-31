#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch


class Node:

   def __init__(self, value):
       self.value = value
       self.next = None
       self.prev = None


if __name__ == "__main__":

    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
    n2.prev = n1

    assert(n1.value == 1)
    assert(n2.value == 2)
    assert(n1.next.value == n2.value)
    assert(n2.prev.value == n1.value)
