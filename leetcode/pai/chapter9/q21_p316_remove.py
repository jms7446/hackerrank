from typing import List, Set, Dict
from collections import Counter


class SolutionRefer:
    """
    """
    def removeDuplicateLetters(self, s: str) -> str:
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(s) == set(suffix):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''


class SolutionLeetCode:
    """
    28ms, 13.8MB (97%, 86%)
    """
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}
        for idx, char in enumerate(s):
            last[char] = idx
        stack = []
        for idx, char in enumerate(s):
            if char in stack:
                continue
            while stack and char < stack[-1] and last[stack[-1]] > idx:
                stack.pop()
            stack.append(char)
        return ''.join(stack)


Solution = SolutionLeetCode


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    ('bcabc', 'abc'),
    ('cbacdcbc', 'acdb'),
])
def test1(in_, out):
    assert Solution().removeDuplicateLetters(in_) == out
