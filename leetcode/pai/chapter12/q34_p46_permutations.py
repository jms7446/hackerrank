from typing import List, Set, Dict
import pytest
from itertools import permutations

from util import *


# 36ms, 13.9MB (92%, 69%)
class SolutionFirst:
    """
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(x) for x in permutations(nums)]


# 44ms 14MB (57%, 37%)
class SolutionLeetCode:
    """interesting and neat implementation of permutation by recursion
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i):
            if i == len(nums):
                res.append(nums[:])

            for j in range(i, len(nums)):
                nums[j], nums[i] = nums[i], nums[j]
                backtrack(i + 1)
                nums[j], nums[i] = nums[i], nums[j]

        backtrack(0)
        return res


Solution = SolutionLeetCode


@pytest.mark.parametrize(['in_', 'out'], [
    ([1, 2, 3], [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]),
])
def test1(in_, out):
    assert sorted(Solution().permute(in_)) == sorted(out)
