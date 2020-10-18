from typing import List, Set, Dict
import pytest


class SolutionFirst:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return -1


Solution = SolutionFirst


@pytest.mark.parametrize(['k', 'prices', 'out'], [
    (2, [2,4,1], 2),
    (2, [3,2,6,5,0,3], 7),
])
def test1(k, prices, out):
    assert Solution().maxProfit(k, prices) == out
