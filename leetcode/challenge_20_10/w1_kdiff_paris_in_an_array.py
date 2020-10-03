from typing import List
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            return sum(c >= 2 for c in Counter(nums).values())
        num_set = set(nums)
        return sum(n + k in num_set for n in sorted(num_set))


import pytest


@pytest.mark.parametrize(['in_', 'k', 'out'], [
    ([3,1,4,1,5], 2, 2),
    ([1,2,3,4,5], 1, 4),
    ([1,3,1,5,4], 0, 1),
    ([1,2,4,4,3,3,0,9,2,3], 3, 2),
    ([-1,-2,-3], 1, 2),
])
def test1(in_, k, out):
    assert Solution().findPairs(in_, k) == out
