#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Marina von Steinkirch


def get_string_comp(s) -> str:

    count, last, aux = 1, '', []

    for i, c in enumerate(s):
        if last == c:
            count += 1

        else:
            if i != 0:
                aux.append(str(count))
            aux.append(c)
            count = 1
            last = c

    aux.append(str(count))
    return ''.join(aux)


if __name__ == '__main__':

    s = 'aabcccccaaaa'
    assert(get_string_comp(s) == 'a2b1c5a4')
