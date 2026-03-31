#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch
# author: bt3gl


class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def add(self, value):
        new_node = Node(value)
        if not self.left:
            self.left = new_node
        elif not self.right:
            self.right = new_node
        else:
            self.left = self.left.add(value)

    def search(self, item):
        return self.value == item or \
            (self.left and self.left.search(item)) or \
            (self.right and self.right.search(item))

    def preorder(self):
        yield self.value
        if self.left:
            for node in self.left.preorder():
                yield node
        if self.right:
            for node in self.right.preorder():
                yield node

    def postorder(self):
        yield self.value
        if self.left:
            for node in self.left.postorder():
                yield node
        if self.right:
            for node in self.right.postorder():
                yield node

    def inorder(self):
        yield self.value
        if self.left:
            for node in self.left.inorder():
                yield node
        if self.right:
            for node in self.right.inorder():
                yield node


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.root.add(value)

    def search(self, item):
        if self.root:
            return self.root.search(item)

    def preorder(self):
        if self.root:
            return list(self.root.preorder())

    def inorder(self):
        if self.root:
            return list(self.root.inorder())

    def postorder(self):
        if self.root:
            return list(self.root.postorder())


if __name__ == '__main__':


    print("\n\n🌳🌳🌳 Testing BinaryTree 🌳🌳🌳")
    bt = BinaryTree()
    array1 = [4, 1, 4, 6, 7, 9, 10, 5, 11, 5]
    print(f'\n🟡 Adding {array1} to the tree...')
    for i in array1:
        bt.add(i)
    print(f"🟢 Print the tree preorder: {bt.preorder()}")  
    print(f"🟢 Print the tree inorder: {bt.inorder()}")
    print(f"🟢 Print the tree postorder: {bt.postorder()}") 

    print(f'\n🟢 Search for node 5: {bt.search(5)}')
    print(f'❌ Search for node 15: {bt.search(15)}')
