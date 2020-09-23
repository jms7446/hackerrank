# 나무 심기

import sys
from operator import itemgetter


class FenwickTree:
    def __init__(self, xs):
        self.tree = [0] * (len(xs) + 1)
        for i in range(1, len(xs) + 1):
            self._update(i, xs[i - 1])

    def get_range_value(self, left, right):
        return self._sum(right + 1) - self._sum(left)

    def update(self, idx, diff):
        self._update(idx + 1, diff)

    def _sum(self, idx):
        acc = 0
        while idx > 0:
            acc += self.tree[idx]
            idx &= idx - 1
        return acc

    def _update(self, idx, diff):
        tree_size = len(self.tree)
        while idx < tree_size:
            self.tree[idx] += diff
            idx += (idx & -idx)


def solve(N, xs):
    sorted_xs_with_index = sorted(enumerate(xs), key=itemgetter(1))
    idx_to_sorted_idx = {i: si for si, (i, _) in enumerate(sorted_xs_with_index)}
    tree = FenwickTree([0] * N)
    count_tree = FenwickTree([0] * N)

    tree.update(idx_to_sorted_idx[0], xs[0])
    count_tree.update(idx_to_sorted_idx[0], 1)
    acc = xs[0]
    res = 1
    for i in range(1, N):
        si = idx_to_sorted_idx[i]
        left_sum = tree.get_range_value(0, si - 1)
        left_count = count_tree.get_range_value(0, si - 1)
        right_sum = acc - left_sum
        cost = xs[i] * (2 * left_count - i) - left_sum + right_sum
        res = (res * cost) % 1000000007
        tree.update(idx_to_sorted_idx[i], xs[i])
        count_tree.update(idx_to_sorted_idx[i], 1)
        acc += xs[i]
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
