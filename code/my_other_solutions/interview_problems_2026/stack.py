#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch


class Stack():

    def __init__(self):
        self.elements = []

    def push(self, num) -> bool:
        try:
            self.elements.append(num)

            return True
        except Exception as e:
            print(f'Error pushing {num}: {e}')

    def pop(self) -> int:
        try:
            return self.elements.pop()
        except Exception as e:
            print(f'Error popping: {e}')
            return 'Stack is empty'
    
    def size(self) -> int:
        return len(self.elements)

    def is_empty(self) -> bool:
        return len(self.elements) == 0

    def peek(self) -> int:
        return self.elements[-1]



if __name__ == '__main__':

    s = Stack()
    print(s.push(1))
    print(s.push(4))
    print(s.push(6))
    print(s.elements)
    
    assert(s.size() == 3)
    assert(s.peek() == 6)

    while s.elements:
        print(s.pop())

    print(s.pop())
    print(s.is_empty())


