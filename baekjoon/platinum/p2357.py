import sys


class SegmentTree:
    def __init__(self, xs):
        self.xs = xs
        self.root = [0] * len(xs)

    def sum(self, start, end):
        pass


def test_SegmentTree():
    from itertools import combinations

    xs = [2, 3, 7, 4, 5, 9, 6, 1]
    tree = SegmentTree(xs)
    for i, j in combinations(xs, 2):
        assert tree.sum(i, j-1) == sum(xs[i:j])




def solve(N, M, xs, rs):
    return -1


def main():
    stdin = sys.stdin
    N, M = [int(x) for x in stdin.readline().split()]
    xs = [int(stdin.readline()) for _ in range(N)]
    rs = [[int(x) for x in stdin.readline().split()] for _ in range(N)]
    print(solve(N, M, xs, rs))


if __name__ == "__main__":
    main()

from util import *
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
10 4
75
30
100
38
50
51
52
20
81
5
1 10
3 5
6 9
8 10
    '''.strip(),
     '''
5 100
38 100
20 81
5 81
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
