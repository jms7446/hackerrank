from typing import List, Set, Dict
import pytest


# 28ms, 14MB (100%, 83%)
class SolutionFirst:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] <= nums[-1]:
            left = 0
            right = len(nums) - 1
        else:
            pivot = self.search_pivot(nums)
            if nums[0] <= target:
                left = 0
                right = pivot - 1
            else:
                left = pivot
                right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

    def search_pivot(self, nums: List[int]):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'target', 'out'], [
    ([4,5,6,7,0,1,2], 0, 4),
    ([4,5,6,7,0,1,2], 3, -1),
    ([1], 0, -1),
    ([1], 1, 0),
    ([1, 3], 3, 1),
])
def test1(in_, target, out):
    assert Solution().search(in_, target) == out
