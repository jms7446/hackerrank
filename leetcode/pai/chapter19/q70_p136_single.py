from typing import List, Set, Dict
import pytest
# from ..data_structure import *
from functools import reduce


# 92ms, 16.4MB (61%, 29%)
class SolutionFirst:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
])
def test1(in_, out):
    assert Solution().singleNumber(in_) == out
