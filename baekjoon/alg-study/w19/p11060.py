import sys
from itertools import count


# 16.15ms
def solve_org(N, xs):
    if N == 1:
        return 0

    visited = [False] * N
    stack = [0]
    visited[0] = True
    for step in count(1):
        if not stack:
            return -1
        new_stack = []
        for idx in stack:
            jump = xs[idx]
            for s in range(-jump, jump + 1):
                next_idx = idx + s
                if next_idx == N - 1:
                    return step
                if not (0 <= next_idx < N) or visited[next_idx]:
                    continue
                visited[next_idx] = True
                new_stack.append(next_idx)
        stack = new_stack


INF = float('inf')


# 2.13ms
def solve(N, xs):
    xs = list(reversed(xs))
    dp = [INF] * N
    dp[0] = 0
    for i in range(1, N):
        if xs[i] > 0:
            left = max(0, i - xs[i])
            dp[i] = min(dp[left:i]) + 1
    return dp[N-1] if dp[N-1] != INF else -1


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    G = [int(x) for x in stdin.readline().split()]
    print(solve(N, G))


if __name__ == "__main__":
    main()

from util import *
import pytest
import random


def test_time():
    random.seed(2)
    N = 1000
    xs = [random.randint(0, 100) for _ in range(N)]
    timeit_lp(solve, (N, xs), num_iter=1000, time_limit=1)  # , log=True, changed='base')


def test_compare():
    def gen_prob(N=1000):
        xs = [random.randint(0, 100) for _ in range(N)]
        return (N, xs)

    compare_func_results(solve, solve_org, generate_probs(gen_prob, (100, ), count=1000))




@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
10
1 2 0 1 3 2 1 5 4 2
        '''.strip(),
     '''
5
     '''.strip()),
    ('''
1
1
    '''.strip(),
     '''
0
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
