# 등차수열

import sys
from collections import Counter
from bisect import bisect_left
from itertools import count


def find(i, j, nums, visited):
    d = nums[j] - nums[i]
    for cnt in count(2):
        visited[i][j] = True
        target = nums[j] + d
        k = bisect_left(nums, target, lo=j)
        if k < len(nums) and nums[k] == target:
            i, j = j, k
        else:
            return cnt


def solve(xs):
    counter = Counter(xs)
    max_found = counter.most_common(1)[0][1]

    nums = sorted(counter.keys())
    n = len(nums)
    visited = [[False] * n for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if not visited[i][j]:
                max_found = max(max_found, find(i, j, nums, visited))
    return max_found


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    xs = [int(stdin.readline()) for _ in range(N)]
    print(solve(xs))


if __name__ == "__main__":
    main()


from util import *
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
5
1
4
3
5
7
    '''.strip(),
     '''
4
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
