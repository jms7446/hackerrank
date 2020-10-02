from typing import List


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def func(idx, t, acc):
            nonlocal res
            if t == 0:
                res.append(acc)
                return
            if idx == len(candidates):
                return

            added = []
            while t >= 0:
                func(idx + 1, t, acc + added)
                added.append(candidates[idx])
                t -= candidates[idx]

        func(0, target, [])
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        acc = []

        def func(idx, t):
            nonlocal res
            if t == 0:
                res.append(acc[:])
                return
            if idx == len(candidates):
                return

            org_size = len(acc)
            while t >= 0:
                func(idx + 1, t)
                acc.append(candidates[idx])
                t -= candidates[idx]
            del acc[org_size:]

        func(0, target)
        return res


import pytest


@pytest.mark.parametrize(['candidates', 'target', 'expected'], [
    ([2,3,6,7], 7, [[2,2,3],[7]]),
    ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
    ([2], 1, []),
    ([1], 1, [[1]]),
    ([1], 2, [[1, 1]]),
])
def test(candidates, target, expected):
    assert sorted(Solution().combinationSum(candidates, target)) == sorted(expected)
