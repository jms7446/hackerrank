# https://leetcode.com/problems/product-of-array-except-self

from typing import List, Set, Dict
from operator import mul
from functools import reduce


class SolutionFirst:
    """
    124ms, 20.5MB (81.8%, 67.2%)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        acc = 1
        for i in range(1, len(nums)):
            acc *= nums[i - 1]
            result[i] = acc
        acc = 1
        for i in reversed(range(len(nums) - 1)):
            acc *= nums[i + 1]
            result[i] *= acc
        return result


class SolutionReference:
    """
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out


# Solution = SolutionFirst
Solution = SolutionReference


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    ([1,2,3,4], [24,12,8,6]),
])
def test1(in_, out):
    assert sorted(Solution().productExceptSelf(in_)) == sorted(out)
