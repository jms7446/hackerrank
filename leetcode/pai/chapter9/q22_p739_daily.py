from typing import List, Set, Dict

from util import *


# 544ms, 20.3MB (47%, 5%)
class SolutionNaive:
    """O(nlogn) because of sorting"""
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = []
        stack = []
        for i, t in enumerate(T):
            while stack and stack[-1][1] < t:
                pi, pt = stack.pop()
                res.append((pi, i - pi))
            stack.append((i, t))
        for i, _ in stack:
            res.append((i, 0))
        return [d for _, d in sorted(res)]


# 500 ms, 17.7 MB(66 %, 24 %)
class SolutionBetter:
    """O(n) make result list in advance, no sorting"""
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and stack[-1][1] < t:
                pi, pt = stack.pop()
                res[pi] = i - pi
            stack.append((i, t))
        return res


# 480ms, 17.4MB (88%, 55%)
class SolutionRefer:
    """O(n), push index only to the stack, t can be identified in T"""
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                pi = stack.pop()
                res[pi] = i - pi
            stack.append(i)
        return res


Solution = SolutionRefer


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ([30], [0]),
])
def test1(in_, out):
    assert Solution().dailyTemperatures(in_) == out
