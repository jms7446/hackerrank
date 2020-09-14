from typing import List, Set, Dict
import pytest
# from ..data_structure import *


# 32ms, 13.9MB (57%, 35%)
class SolutionFirst:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


Solution = SolutionFirst


@pytest.mark.parametrize(['x', 'y', 'out'], [
    (1, 4, 2),
])
def test1(x, y, out):
    assert Solution().hammingDistance(x, y) == out
