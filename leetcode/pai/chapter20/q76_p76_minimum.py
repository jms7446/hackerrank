from typing import List, Set, Dict
import pytest
from collections import Counter


# 132ms, 14.5MB (58%, 54%)
class SolutionFirst:
    def minWindow(self, s: str, t: str) -> str:
        tc = Counter(t)
        left = 0
        cnt = 0
        min_span_size = float('inf')
        min_span = ""
        counter = Counter()
        for idx, c in enumerate(s):
            if c in t:
                if counter[c] < tc[c]:
                    cnt += 1
                counter[c] += 1

            if cnt == len(t):
                while cnt == len(t):
                    left_c = s[left]
                    if left_c in tc:
                        counter[left_c] -= 1
                        if counter[left_c] < tc[left_c]:
                            cnt -= 1
                            span_size = idx - left + 1
                            if span_size < min_span_size:
                                min_span = s[left:idx+1]
                                min_span_size = span_size
                    left += 1
        return min_span


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'k', 'out'], [
    ("ADOBECODEBANC","ABC", "BANC"),
    ("a", "aa", ""),
])
def test1(in_, k, out):
    assert Solution().minWindow(in_, k) == out
