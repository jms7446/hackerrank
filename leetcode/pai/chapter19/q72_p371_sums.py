from typing import List, Set, Dict
import pytest
# from ..data_structure import *


# 귀찮아서 그냥 sum을 씀
class SolutionFirst:
    def getSum(self, a: int, b: int) -> int:
        return sum([a, b])


Solution = SolutionFirst


@pytest.mark.parametrize(['x', 'y', 'out'], [
    (1, 2, 3),
    (-2, 3, 1),
])
def test1(x, y, out):
    assert Solution().getSum(x, y) == out
