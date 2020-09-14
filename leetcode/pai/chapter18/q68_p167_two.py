from typing import List, Set, Dict
import pytest
from bisect import bisect_left


class SolutionFirst:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            remain = target - n
            idx = bisect_left(numbers, remain, lo=i+1)
            if idx < len(numbers) and numbers[idx] == remain:
                return [i + 1, idx + 1]


# 72ms, 14.4MB (44%, 37%)
class SolutionSecond:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum > target:
                right -= 1
            elif cur_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]


Solution = SolutionSecond


@pytest.mark.parametrize(['in_', 'target', 'out'], [
    ([2,7,11,15], 9, [1,2]),
    ([2,3,4], 6, [1,3]),
    ([-1,0], -1, [1,2]),
])
def test1(in_, target, out):
    assert Solution().twoSum(in_, target) == out
