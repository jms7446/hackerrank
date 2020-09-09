from typing import List


class SolutionFirst:
    """
    220ms, 18.4 (50%, 50%)
    """
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-1-i] = s[-1-i], s[i]


class SolutionRefer:
    """I think that this way is abusing with python
    196ms, 18.1MB (99.1%, 92%)
    """
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


Solution = SolutionFirst


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    (["h","e","l","l","o"], ["o","l","l","e","h"]),
    (["H","a","n","n","a","h"], ["h","a","n","n","a","H"]),
])
def test1(in_, out):
    Solution().reverseString(in_)
    assert in_ == out
