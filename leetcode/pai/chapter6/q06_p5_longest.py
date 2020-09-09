from typing import List, Set, Dict


class SolutionFirst:
    """
    260ms, 13.8MB (94%, 68%)
    """
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]

        if len(s) <= 1 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        return result


Solution = SolutionFirst


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    ("babad", "bab"),
    ("cbbd", "bb"),
])
def test1(in_, out):
    assert Solution().longestPalindrome(in_) == out
