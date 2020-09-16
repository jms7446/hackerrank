import sys


def solve(n, pairs):
    dp = [0] * (n + 50)     # t <= 50 (for skip check condition)
    for i in reversed(range(n)):
        t, p = pairs[i]
        income = dp[i + 1]
        complete_day = i + t - 1
        if complete_day < n:
            income = max(income, p + dp[complete_day + 1])
        dp[i] = income
    return dp[0]


def main():
    stdin = sys.stdin
    n = int(stdin.readline())
    pairs = [[int(x) for x in stdin.readline().split()] for _ in range(n)]
    print(solve(n, pairs))


if __name__ == "__main__":
    main()

from util import *
import pytest


def test_main():
    in_str = """

    """.strip()
    out_str = """

    """.strip()
    assert mock_io(main)(in_str) == out_str


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
    '''.strip(), '45'.strip()),
    ('''
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
    '''.strip(), '55'.strip()),
    ('''
10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6
    '''.strip(), '20'.strip()),
    ('''
10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
    '''.strip(), '90'.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
