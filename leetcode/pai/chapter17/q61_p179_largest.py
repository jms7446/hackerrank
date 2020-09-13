from typing import List, Set, Dict
import pytest
from functools import cmp_to_key


# 36ms, 13.8MB (86%, 58%)
class SolutionFirst:
    def largestNumber(self, nums: List[int]) -> str:
        @cmp_to_key
        def compare(x, y):
            if x + y < y + x:
                return -1
            else:
                return 1

        nums = [str(num) for num in nums]
        nums.sort(key=compare, reverse=True)
        if nums[0] == '0':
            return '0'
        else:
            return ''.join(nums)


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    ([10, 2], '210'),
    ([3, 30, 34, 5, 9], '9534330'),
    ([0, 0], '0'),
])
def test1(in_, out):
    assert Solution().largestNumber(in_) == out
