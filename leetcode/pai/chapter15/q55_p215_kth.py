from typing import List, Set, Dict
import pytest


# 60ms, 14.7MB (95%, 28%)
class SolutionFirst:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'k', 'out'], [
    ([3,2,1,5,6,4], 2, 5),
])
def test1(in_, k, out):
    assert Solution().findKthLargest(in_, k) == out
