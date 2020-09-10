from typing import List, Set, Dict
import pytest
from collections import defaultdict


# 496ms, 14MB (16%, 34%)
class SolutionFirst:
    """
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        last = {}
        i = 0
        length = 0
        N = len(s)
        while i < N:
            c = s[i]
            if c in last:
                longest = max(longest, length)
                i = last[c] + 1
                last = {}
                length = 0
            else:
                length += 1
                last[c] = i
                i += 1
        longest = max(longest, length)
        return longest


# 44ms, 14MB (99%, 32%)
class SolutionRefer:
    """
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = defaultdict(lambda: -1)
        max_length = length = 0
        start = 0
        for index, char in enumerate(s):
            if start <= used[char]:
                max_length = max(max_length, length)
                length -= used[char] + 1 - start
                start = used[char] + 1
            length += 1
            used[char] = index
        max_length = max(max_length, length)
        return max_length


Solution = SolutionRefer


@pytest.mark.parametrize(['in_', 'out'], [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    (" ", 1),
    ("dvdf", 3)
])
def test1(in_, out):
    assert Solution().lengthOfLongestSubstring(in_) == out
