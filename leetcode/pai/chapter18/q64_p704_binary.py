from typing import List, Set, Dict
import pytest
from bisect import bisect_left
# from ..data_structure import *


# 244ms, 15.1MB (98%, 37%)
class SolutionFirst:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return -1


class SolutionSecond:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


class SolutionThird:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect_left(nums, target)
        return idx if idx < len(nums) and nums[idx] == target else -1


Solution = SolutionThird


@pytest.mark.parametrize(['in_', 'k', 'out'], [
    ([-1,0,3,5,9,12], 9, 4),
    ([-1,0,3,5,9,12], 2, -1),
    ([-1,0,3,5,9,12], 13, -1),
])
def test1(in_, out, k):
    assert Solution().search(in_, k) == out
