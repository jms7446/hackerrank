from typing import List, Set, Dict
import pytest
from collections import Counter


# 100ms, 18.1MB (95%, 95%)
class SolutionFirst:
    """
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x for x, _ in Counter(nums).most_common(k)]


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'k', 'out'], [
    ([1,1,1,2,2,3], 2, [1, 2]),
    ([1], 1, [1]),
])
def test1(in_, k, out):
    assert Solution().topKFrequent(in_, k) == out
