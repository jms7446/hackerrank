# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List, Set, Dict


class SolutionFirst:
    """
    68ms, 15MB (62.4%, 91.9%)
    """
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0
        for p in prices:
            max_profit = max(max_profit, p - min_price)
            min_price = min(min_price, p)
        return max_profit


Solution = SolutionFirst


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0),
])
def test1(in_, out):
    assert Solution().maxProfit(in_) == out


