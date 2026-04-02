#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# no copyright, this was optimized by AI

'''
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''


def length_of_longest_substring(s: str) -> int:
    """Longest substring with all distinct characters — O(n) time, O(k) space (k = distinct chars in window)."""
    last_index: dict[str, int] = {}
    start = 0
    best = 0
    for i, c in enumerate(s):
        prev = last_index.get(c, -1)
        if prev >= start:
            start = prev + 1
        last_index[c] = i
        best = max(best, i - start + 1)
    return best


if __name__ == '__main__':
    assert length_of_longest_substring('abcabcbb') == 3
    assert length_of_longest_substring('bbbbb') == 1
    assert length_of_longest_substring('pwwkew') == 3
    assert length_of_longest_substring('') == 0

