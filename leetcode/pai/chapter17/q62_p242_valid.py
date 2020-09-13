from typing import List, Set, Dict
import pytest
# from ..data_structure import *
from collections import Counter


# 52ms, 14.7MB (60%, 15%)
class SolutionFirst:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# 36ms, 14.1MB (95%, 74%)
class SolutionLeetCode:
    def isAnagram(self, s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)
        return not ((a - b) or (b - a))


Solution = SolutionLeetCode


@pytest.mark.parametrize(['in1', 'in2', 'out'], [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
])
def test1(in1, in2, out):
    assert Solution().isAnagram(in1, in2) == out
