#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch


class Queue():

    def __init__(self):
        self.enqueue = []
        self.dequeue = []

    def en2de(self) -> None:
        if not self.dequeue:
            while len(self.enqueue) > 0:
                self.dequeue.append(self.enqueue.pop())

    def run_enq(self, item) -> None:
        self.enqueue.append(item)

    def run_deq(self) -> int:
        self.en2de()
        return self.dequeue.pop()

    def peak(self) -> int:
        self.en2de()
        if self.dequeue:
            return self.dequeue[-1]

    def size(self) -> int:
        return len(self.enqueue) + len(self.dequeue)

    def is_empty(self) -> bool:
        return not (self.enqueue + self.dequeue)


if __name__ == '__main__':

    q = Queue()
    for i in range(1,11):
        q.run_enq(i)
    
    print(f'Size: {q.size()}')
    print(f'Is empty? {q.is_empty()}')
    print(f'Peak: {q.peak()}')
    print('Dequeuing...')

    for i in range(10):
         q.run_deq()

    print(f'Size: {q.size()}')
    print(f'Is empty? {q.is_empty()}')
    print(f'Peak: {q.peak()}')
