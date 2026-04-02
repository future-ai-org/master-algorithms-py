#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# no copyright, this was optimized by AI

'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character
'''


def min_distance(word1: str, word2: str) -> int:
    """Levenshtein distance: dp[i][j] = edits to turn word1[:i] into word2[:j]. O(m*n) time and space."""
    m, n = len(word1), len(word2)
    # dp[i][j]: minimum operations for first i chars of word1 -> first j chars of word2
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # delete from word1
                    dp[i][j - 1],      # insert into word1
                    dp[i - 1][j - 1],  # replace
                )
    return dp[m][n]


if __name__ == '__main__':
    assert min_distance('horse', 'ros') == 3
    assert min_distance('intention', 'execution') == 5
    assert min_distance('', '') == 0
    assert min_distance('a', '') == 1
    assert min_distance('', 'a') == 1
    assert min_distance('abc', 'abc') == 0