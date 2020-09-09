from typing import List


class SolutionFirst:
    """
    288ms, 16.1MB (75.8%, 91.8%)
    """
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


Solution = SolutionFirst


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    ([1,4,3,2], 4),
])
def test1(in_, out):
    assert Solution().arrayPairSum(in_) == out
