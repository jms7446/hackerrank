# 나무 심기

import sys
from operator import itemgetter
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


def solve(N, xs):
    sorted_xs_with_index = sorted(enumerate(xs), key=itemgetter(1))
    idx_to_sorted_idx = {i: si for si, (i, _) in enumerate(sorted_xs_with_index)}
    tree = SegmentTree([0] * N)
    count_tree = SegmentTree([0] * N)

    tree.update(idx_to_sorted_idx[0], xs[0])
    count_tree.update(idx_to_sorted_idx[0], 1)
    res = 1
    for i in range(1, N):
        si = idx_to_sorted_idx[i]
        left_sum = tree.get_range_value(0, si - 1)
        left_count = count_tree.get_range_value(0, si - 1)
        right_sum = tree.get_range_value(si + 1, N - 1)
        cost = xs[i] * (2 * left_count - i) - left_sum + right_sum
        res = (res * cost) % 1000000007
        tree.update(idx_to_sorted_idx[i], xs[i])
        count_tree.update(idx_to_sorted_idx[i], 1)
    return res


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    xs = [int(stdin.readline()) for _ in range(N)]
    print(solve(N, xs))


if __name__ == "__main__":
    main()


from util import *
import pytest
import random


def test_time():
    def gen_prob():
        N = 20000
        xs = [random.randint(1, 200000) for _ in range(N)]
        return N, xs

    random.seed(2)
    timeit(solve, gen_prob())


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
5
3
4
5
6
7
    '''.strip(),
     '''
180
     '''.strip()),
    ('''
4
1
5
3
2
    '''.strip(),
     '''
80
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
