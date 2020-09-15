from typing import List, Set, Dict
import pytest
# from ..data_structure import *


# 64ms, 15MB (68%, 83%)
class SolutionFirst:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(n - p for p, n in zip(prices, prices[1:]) if p < n)


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    ([7,1,5,3,6,4], 7),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0),
])
def test1(in_, out):
    assert Solution().maxProfit(in_) == out
