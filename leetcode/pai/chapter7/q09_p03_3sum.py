from typing import List
from itertools import combinations
from collections import Counter


class SolutionNaive:
    """
    1956ms, 18.9MB (14%, 5%)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        counter = Counter(nums)
        for a, b in combinations(nums, 2):
            complement = -(a + b)
            if complement <= 0:
                continue
            count = counter[complement]
            if count == 0:
                continue
            if b == complement:
                if count >= 2:
                    result.add((a, b, complement))
            elif count >= 1:
                if b < complement:
                    result.add((a, b, complement))
                else:
                    result.add((a, complement, b))
        if counter[0] >= 3:
            result.add((0, 0, 0))
        return [list(triple) for triple in result]


class SolutionSubTwoSum:
    """
    624ms, 18.8MB (98%, 5%)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        pre_n1 = None
        for i, n1 in enumerate(nums[:-2]):
            if n1 == pre_n1:
                continue
            pre_n1 = n1
            if n1 > 0:
                break

            # from now, we will solve two sum problem of which sum is target
            target = -n1
            n2s = {nums[i + 1]}
            for n3 in nums[i+2:]:
                n2_guess = target - n3
                if n2_guess in n2s:
                    result.add((n1, n2_guess, n3))
                n2s.add(n3)     # pre n3 is candidate of n2
        return [list(x) for x in result]


class SolutionTwoPointer:
    """
    784ms, 17.1MB (87%, 75%)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        pre_num = None
        for idx, n1 in enumerate(nums):
            if n1 == pre_num:
                continue
            pre_num = n1
            if n1 > 0:
                break
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum + n1 == 0:
                    result.append([n1, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                elif two_sum + n1 > 0:
                    right -= 1
                else:
                    left += 1
        return result


Solution = SolutionSubTwoSum


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([], []),
    ([0], []),
    ([0, 0, 0], [[0, 0, 0]]),
    ([-1,0,1,2,-1,-4,-2,-3,3,0,4],[[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]),
    ([-2,0,0,2,2], [[-2,0,2]]),
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([-2,0,1,1,2], [[-2,0,2],[-2,1,1]]),
    ([0,0,0,0], [[0,0,0]]),
])
def test1(in_, out):
    assert sorted([list(xs) for xs in Solution().threeSum(in_)]) == sorted(out)
