#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch
# author: bt3gl

def remove_elements(head, val):
        
  sentinel = Node(0)
  sentinel.next = head
  prev, current = sentinel, head

  while current:
    if current.val == val:
      prev.next = current.next
    else:
      prev = current
    current = current.next
                
  return sentinel.next
  
