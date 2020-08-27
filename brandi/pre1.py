import sys
from math import ceil
from collections import Counter


def solve(N, K, xs):
    count = Counter(xs)
    _, c = count.most_common(1)[0]
    rest = N - c
    return ceil(rest / (K - 1))


def main():
    stdin = sys.stdin
    N, K = [int(x) for x in stdin.readline().split()]
    xs = [int(x) for x in stdin.readline().split()]
    print(solve(N, K, xs))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
4 3
2 3 1 4
    '''.strip(),
     '2'),
    ('''
8 3
7 3 1 8 4 6 2 5
    '''.strip(),
     '4'),
    ('''
37 4
31 36 20 30 1 9 6 13 3 29 11 25 7 8 2 24 34 18 26 15 23 28 37 19 21 4 32 14 16 10 12 27 22 35 5 17 33
    '''.strip(),
     '12'),
])
def test_main(in_str, out_str):
    assert get_output_with_stdin(main, in_str) == out_str
