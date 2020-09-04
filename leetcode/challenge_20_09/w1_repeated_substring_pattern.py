from typing import List, Set, Dict

# Solution1: naive way
# Solution: reference other codes, it's cool.


class Solution1:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)
        for ptn_len in range(1, N // 2 + 1):
            if N % ptn_len != 0:
                continue
            ptn = s[:ptn_len]
            for l in range(ptn_len, N, ptn_len):
                if s[l:l+ptn_len] != ptn:
                    break
            else:
                return True
        return False


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s)[1:-1].find(s) >= 0

from util import *
import pytest


@pytest.mark.parametrize(['input_', 'output'], [
    ('abab', True),
    ('aba',False),
    ('abcabcabcabc',True),
])
def test_solution(input_, output):
    assert Solution().repeatedSubstringPattern(input_) == output
