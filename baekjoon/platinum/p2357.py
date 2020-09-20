import sys


################################################################################
# from util.data_structure
################################################################################

from operator import add


class SegmentTree:
    def __init__(self, xs, acc_func=add, init=0):
        def build(v, il, ir):
            if il == ir:
                self.tree[v] = xs[il]
            else:
                im = (il + ir) // 2
                self.tree[v] = self.acc_func(build(v * 2 + 1, il, im), build(v * 2 + 2, im + 1, ir))
            return self.tree[v]

        self.acc_func = acc_func
        self.init = init
        self.n = len(xs)
        self.tree = [0] * (self.n * 4)   # rough max
        build(0, 0, self.n - 1)

    def get_range_value(self, left, right):
        def get_value(v, il, ir):
            if il >= left and ir <= right:
                return self.tree[v]
            elif il > right or ir < left:
                return self.init
            else:
                im = (il + ir) // 2
                return self.acc_func(get_value(v * 2 + 1, il, im), get_value(v * 2 + 2, im + 1, ir))
        return get_value(0, 0, self.n - 1)

    def update(self, idx, val):
        def _update(v, il, ir):
            if il == idx and ir == idx:
                self.tree[v] = val
            elif il <= idx <= ir:
                im = (il + ir) // 2
                self.tree[v] = self.acc_func(_update(v * 2 + 1, il, im), _update(v * 2 + 2, im + 1, ir))
            return self.tree[v]
        _update(0, 0, self.n - 1)

################################################################################


def solve(N, M, xs, rs):
    min_tree = SegmentTree(xs, acc_func=min, init=float('inf'))
    max_tree = SegmentTree(xs, acc_func=max, init=-float('inf'))
    return [(min_tree.get_range_value(left, right), max_tree.get_range_value(left, right)) for left, right in rs]


def main():
    stdin = sys.stdin
    N, M = [int(x) for x in stdin.readline().split()]
    xs = [int(stdin.readline()) for _ in range(N)]
    rs = [[int(x) - 1 for x in stdin.readline().split()] for _ in range(M)]
    for a, b in solve(N, M, xs, rs):
        print(a, b)


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


def test_MaxSegmentTree():
    from itertools import combinations

    xs = [2, 3, 7, 4, 5, 9, 6, 1]
    tree = MaxSegmentTree(xs)
    for i, j in combinations(range(len(xs)), 2):
        assert (tree.max(i, j-1), (i, j)) == (max(xs[i:j]), (i, j))

    xs[3] = 10
    tree.update(3, 10)
    for i, j in combinations(range(len(xs)), 2):
        assert (tree.max(i, j-1), (i, j)) == (max(xs[i:j]), (i, j))


