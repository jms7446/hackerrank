from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in num_map:
                return [num_map[complement], i]
            else:
                num_map[n] = i


import pytest


@pytest.mark.parametrize(('nums',  'target', 'expected'), [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
])
def test_solution(nums, target, expected):
    assert Solution().twoSum(nums, target) == expected
