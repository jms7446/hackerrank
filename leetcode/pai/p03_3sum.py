from typing import List
from itertools import combinations
from collections import Counter


class Solution:
    """
    1956ms(14%), 18.9MB(5%)
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


def test1():
    assert Solution().threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]


def test2():
    assert Solution().threeSum([]) == []


def test3():
    assert Solution().threeSum([0]) == []


def test4():
    assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]


def test5():
    assert sorted(Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4])) == sorted([[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]])


def test6():
    assert sorted(Solution().threeSum([-2,0,0,2,2])) == [[-2,0,2]]
