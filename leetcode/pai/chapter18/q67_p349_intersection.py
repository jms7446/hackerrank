from typing import List, Set, Dict
import pytest
# from ..data_structure import *


# 40ms, 14.1MB (95%, 12%)
class SolutionFirst:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(nums2))


Solution = SolutionFirst


@pytest.mark.parametrize(['in1', 'in2', 'out'], [
    ([1, 2, 2, 1], [2, 2], [2]),
    ([4, 9, 5], [9, 4, 9, 8, 4], [9, 4]),
])
def test1(in1, in2, out):
    assert Solution().intersection(in1, in2) == out
