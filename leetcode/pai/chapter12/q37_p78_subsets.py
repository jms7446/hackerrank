from typing import List, Set, Dict
import pytest


# 32ms, 14MB (86%, 69%)
class SolutionFirst:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bfs(idx, acc):
            if idx >= len(nums):
                res.append(acc.copy())
                return

            bfs(idx + 1, acc)

            acc.append(nums[idx])
            bfs(idx + 1, acc)
            acc.pop()

        bfs(0, [])
        return res


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    ([1,2,3], [ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], [] ]),
])
def test1(in_, out):
    assert sorted([sorted(x) for x in Solution().subsets(in_)]) == sorted([sorted(x) for x in out])
