from typing import List, Set, Dict
import pytest
# from ..data_structure import *


class SolutionFirst:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return -1


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    ([1,2,3,4,5], [3,4,5,1,2], 3),
    ([2,3,4], [3,4,3], -1),
])
def test1(in_, out):
    assert Solution().canCompleteCircuit(in_) == out
