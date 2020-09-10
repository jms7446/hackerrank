from typing import List, Set, Dict
import pytest


# 64ms, 13.7MB (79%, 95%)
class SolutionFirst:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort(reverse=True)

        def bfs(idx, left, acc):
            if idx >= len(candidates):
                return
            if left == 0:
                res.append(acc.copy())
                return

            num = candidates[idx]
            if num <= left:
                acc.append(num)
                bfs(idx, left - num, acc)
                acc.pop()
            bfs(idx + 1, left, acc)

        bfs(0, target, [])
        return res


class SolutionLeetCode:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        self.dfs(candidates, 0, target, [], 0)
        return self.res

    def dfs(self, candidates, curr, target, path, index):
        if curr == target:
            self.res.append(path[:])

        for j in range(index, len(candidates)):
            if candidates[j] + curr > target:
                break
            self.dfs(candidates, curr + candidates[j], target, path + [candidates[j]], j)


Solution = SolutionLeetCode


@pytest.mark.parametrize(['in_', 't', 'out'], [
    ([2,3,6,7], 7, [ [7], [2,2,3] ]),
    ([2, 3, 5], 8, [ [2,2,2,2], [2,3,3], [3,5] ]),
])
def test1(in_, t, out):
    assert sorted([sorted(x) for x in Solution().combinationSum(in_, t)]) == sorted([sorted(x) for x in out])
