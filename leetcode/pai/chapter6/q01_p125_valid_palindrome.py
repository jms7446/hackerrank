# https://leetcode.com/problems/valid-palindrome/

from typing import List, Set, Dict
import re


class SolutionFirst:
    """
    """
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]


Solution = SolutionFirst


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
])
def test1(in_, out):
    assert Solution().isPalindrome(in_) == out


