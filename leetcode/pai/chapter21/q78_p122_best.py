from typing import List, Set, Dict
import pytest
from itertools import tee


def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


# 52ms, 14.9MB (99%, 85%)
class SolutionSecond:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(n - p for p, n in pairwise(prices) if p < n)


# 64ms, 15MB (68%, 83%)
class SolutionFirst:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(n - p for p, n in zip(prices, prices[1:]) if p < n)


Solution = SolutionSecond


@pytest.mark.parametrize(['in_', 'out'], [
    ([7,1,5,3,6,4], 7),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0),
])
def test1(in_, out):
    assert Solution().maxProfit(in_) == out
