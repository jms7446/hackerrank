import sys


def make_sums(chapters):
    sums = [0] * (len(chapters) + 1)
    sums[0] = 0
    for i in range(len(chapters)):
        sums[i + 1] = sums[i] + chapters[i]
    return sums


# K = 100: 31.09ms
def solve(K, chapters):
    """ bottom-dp dp

    meanings
        sums[5] == sum(chapters[:5])
            so we can calculate `sum(chapters[a:b])` by `sums(b) - sums(a)`
            this drops time complexity.
        dp[1][4] == (cost of merging from chapters[1] to chapters[3])
    """
    sums = make_sums(chapters)
    dp = [[0] * (K + 1) for _ in range(K)]

    for merge_size in range(2, K + 1):
        for begin in range(K - merge_size + 1):
            end = begin + merge_size
            cost = min(dp[begin][m] + dp[m][end] for m in range(begin + 1, end))
            dp[begin][end] = sums[end] - sums[begin] + cost
    return dp[0][K]


def main():
    stdin = sys.stdin
    T = int(stdin.readline())
    for _ in range(T):
        K = int(stdin.readline())
        xs = [int(x) for x in stdin.readline().split()]
        print(solve(K, xs))


if __name__ == "__main__":
    main()

from util import *


def test_make_sums():
    xs = [1, 2, 3]
    sums = make_sums(xs)
    assert sums == [0, 1, 3, 6]
    assert sums[3] - sums[0] == 6


def test_main():
    in_str = """
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
    """.strip()
    out_str = """
300
864
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_main1():
    in_str = """
1
4
40 30 30 50
    """.strip()
    out_str = """
300
    """.strip()
    assert mock_io(main)(in_str) == out_str


# sys.setrecursionlimit(1000000)
# K == 10: 119.44ms
def solve_recursion_version(K, chapters):
    """recursion version"""
    def f(s, e):
        if s == e - 1:
            return 0
        if memory[s][e] is not None:
            return memory[s][e]
        memory[s][e] = sums[e] - sums[s] + min(f(s, m) + f(m, e) for m in range(s + 1, e))
        return memory[s][e]

    sums = make_sums(chapters)
    memory = [[None] * (K + 1) for _ in range(K)]
    res = f(0, K)
    return res


def test_time():
    import random
    random.seed(2)
    K = 100
    args_iter = ((K, [random.randint(1, 10000) for _ in range(K)]) for _ in range(5))
    timeits(solve, args_iter, num_iter=10, time_limit_per_args=0.1)
