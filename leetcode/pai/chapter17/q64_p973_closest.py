from typing import List, Set, Dict
import pytest
# from ..data_structure import *


# 668ms, 19.1MB (94%, 87%)
class SolutionFirst:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:K]


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'k', 'out'], [
    ([[1,3],[-2,2]], 1, [[-2,2]]),
    ([[3,3],[5,-1],[-2,4]], 2, [[3,3],[-2,4]]),
])
def test1(in_, k, out):
    assert Solution().kClosest(in_, k) == out
