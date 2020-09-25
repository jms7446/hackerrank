# 괄호
import sys

M = 10**9 + 7


def solve(xs):
    max_n = max(xs) // 2
    dp = [0] * (max_n + 2)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, max_n + 1):
        count = 0
        for j in range(i):
            count += dp[j] * dp[i - j - 1]
        dp[i] = count % M

    return [dp[x // 2] if x % 2 == 0 else 0 for x in xs]


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    xs = [int(stdin.readline()) for _ in range(N)]
    for r in solve(xs):
        print(r)


if __name__ == "__main__":
    main()

from util import *
import pytest


def test_compare():
    compare_func_result(mock_io(main), ext_binary_to_func('p10422'), ('1\n5000\n', ))


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
4
1
2
4
6
    '''.strip(),
     '''
0
1
2
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
