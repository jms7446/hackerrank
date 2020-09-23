# 스위치

import sys


class SegmentTreeLazy:
    def __init__(self, xs):
        self.n = len(xs)
        self.tree = [0] * (self.n * 4)   # rough max
        self.lazy = [0] * (self.n * 4)   # rough max

    def get_range_value(self, left, right):
        def get_value(v, il, ir, lazy):
            self.lazy[v] = (lazy + self.lazy[v]) % 2
            if il >= left and ir <= right:
                if self.lazy[v]:
                    return (ir - il + 1) - self.tree[v]
                else:
                    return self.tree[v]
            elif il > right or ir < left:
                return 0
            else:
                im = (il + ir) // 2
                cur_lazy = self.lazy[v]
                if cur_lazy:
                    self.tree[v] = (ir - il + 1) - self.tree[v]
                self.lazy[v] = 0
                ll = get_value(v * 2 + 1, il, im, cur_lazy)
                rr = get_value(v * 2 + 2, im + 1, ir, cur_lazy)
                return ll + rr

        return get_value(0, 0, self.n - 1, 0)

    def range_update(self, left, right):
        def _update(v, il, ir):
            if il >= left and ir <= right:
                self.lazy[v] = 1 - self.lazy[v]
            elif il > right or ir < left:
                pass
            else:
                im = (il + ir) // 2
                self.tree[v] = _update(v * 2 + 1, il, im) + _update(v * 2 + 2, im + 1, ir)
            return self.tree[v] if self.lazy[v] == 0 else (ir - il + 1) - self.tree[v]

        return _update(0, 0, self.n - 1)


def solve(N, cs):
    res = []
    tree = SegmentTreeLazy([0] * N)
    for command, left, right in cs:
        left, right = left - 1, right - 1       # convert to 0-base index
        if command == 0:
            tree.range_update(left, right)
        else:
            res.append(tree.get_range_value(left, right))
    return res


def main():
    stdin = sys.stdin
    N, M = [int(x) for x in stdin.readline().split()]
    cs = [[int(x) for x in stdin.readline().split()] for _ in range(M)]
    for r in solve(N, cs):
        print(r)


if __name__ == "__main__":
    main()

from util import *
import pytest


def test_base1():
    n = 5
    cs = [(0, 1, 2), (1, 2, 3)]
    assert solve(n, cs) == [1]


def test_base2():
    n = 5
    cs = [(0, 1, 2), (0, 2, 4), (1, 2, 3)]
    assert solve(n, cs) == [1]


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
4 5
0 1 2
0 2 4
1 2 3
0 2 4
1 1 4
    '''.strip(),
     '''
1
2
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
