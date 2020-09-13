from typing import List, Set, Dict
import pytest
# from ..data_structure import *


# 32ms, 13.8MB (78%, 71%)
class SolutionFirst:
    def sortColors(self, nums: List[int]) -> None:
        left = mid = 0
        right = len(nums)
        mid_val = 1
        while mid < right:
            num = nums[mid]
            if num < mid_val:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif num > mid_val:
                right -= 1
                nums[mid], nums[right] = nums[right], nums[mid]
            else:
                mid += 1


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    ([2,0,2,1,1,0], [0,0,1,1,2,2]),
    ([2,0,1], [0,1,2]),
    ([0], [0]),
    ([1], [1]),
])
def test1(in_, out):

    Solution().sortColors(in_)
    assert in_ == out
