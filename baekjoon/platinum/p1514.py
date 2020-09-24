# 자물쇠

import sys

sys.setrecursionlimit(1000000)
INF = float('inf')


def solve(N, start, target):
    def find(pos, x, y, z, d):
        if pos == N:
            return 0
        if dp[pos][x][y][z][d] != INF:
            return dp[pos][x][y][z][d]

        if x == target[pos]:
            dp[pos][x][y][z][d] = min(find(pos + 1, y, z, start[pos + 3], 0), find(pos + 1, y, z, start[pos + 3], 1))
        else:
            nums = (1, 2, 3) if d == 1 else (7, 8, 9)
            for num in nums:
                dp[pos][x][y][z][d] = min(dp[pos][x][y][z][d], 1 + find(pos, (x + num) % L, y, z, d))
                dp[pos][x][y][z][d] = min(dp[pos][x][y][z][d], 1 + find(pos, (x + num) % L, (y + num) % L, z, d))
                dp[pos][x][y][z][d] = min(dp[pos][x][y][z][d], 1 + find(pos, (x + num) % L, (y + num) % L, (z + num) % L, d))
        return dp[pos][x][y][z][d]

    L = 10
    dp = [[[[[INF] * 2 for _ in range(L)] for _ in range(L)] for _ in range(L)] for _ in range(N)]
    start += "000"
    start = [int(c) for c in start]
    target = [int(c) for c in target]
    return min(find(0, start[0], start[1], start[2], 0), find(0, start[0], start[1], start[2], 1))


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    start = stdin.readline().strip()
    target = stdin.readline().strip()
    print(solve(N, start, target))


if __name__ == "__main__":
    main()

from util import *
import pytest
import random


def test_compare():
    def gen_prob():
        N = 3
        start = ''.join(str(random.randint(0, 9)) for _ in range(N))
        target = ''.join(str(random.randint(0, 9)) for _ in range(N))
        return merge_to_lines([N, start, target])
    compare_func_results(mock_io(main), ext_binary_to_func('p1514'), generate_probs(gen_prob, count=100))


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
3
555
464
    '''.strip(),
     '''
2
     '''.strip()),
    ('''
4
1234
3456
    '''.strip(),
     '''
2
     '''.strip()),
    ('''
1
1
7
    '''.strip(),
     '''
2
     '''.strip()),
    ('''
3
146
085
    '''.strip(),
     '''
3
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
