from typing import List, Set, Dict
import pytest
from itertools import combinations


# 80ms, 15MB (97%, 93%)
class SolutionFirst:
    """
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(xs) for xs in combinations(range(1, n + 1), k)]


# 88ms, 15.2MB (93%, 65%)
class SolutionSecond:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = list(range(1, n + 1))

        def dfs(idx, acc):
            if len(acc) == k:
                res.append(acc.copy())
            else:
                # len(acc) + 1 + (n - end) > k
                # so end < len(acc) + (n - k) + 1
                for j in range(idx, len(acc) + (n - k) + 1):
                    acc.append(nums[j])
                    dfs(j + 1, acc)
                    acc.pop()
        dfs(0, [])
        return res


Solution = SolutionSecond


@pytest.mark.parametrize(['n', 'k', 'out'], [
    (4, 2, [[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]]),
    (1, 1, [[1]])
])
def test1(n, k, out):
    assert sorted(Solution().combine(n, k)) == sorted(out)
