from typing import List, Set, Dict
import pytest
from collections import Counter


# 148ms, 14MB (53%, 17%)
class SolutionFirst:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        left = right = 0
        counter = Counter()
        most = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            most = max(most, counter[s[right]])
            if right - left + 1 > most + k:
                counter[s[left]] -= 1
                left += 1
        return right - left + 1


class SolutionSecond:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = most = 0
        freq = {} # frequency table
        for i in range(len(s)):
            freq[s[i]] = 1 + freq.get(s[i], 0)
            most = max(most, freq[s[i]])
            if ans < most + k: ans += 1
            else: freq[s[i - ans]] -= 1
        return ans


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'k', 'out'], [
    ("ABAB", 2, 4),
    ("AABABBA", 1, 4),
])
def test1(in_, k, out):
    assert Solution().characterReplacement(in_, k) == out
