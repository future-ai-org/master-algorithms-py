#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch
# author: bt3gl


def lowest_common_ancestor(root, p, q):

        node, result = root, root
        
        while node:
            
            result = node
            
            if node.val > p.val and node.val > q.val:
                node = node.left
                
            elif node.val < p.val and node.val < q.val:
                node = node.right
                
            else:
                break
        
        return result
