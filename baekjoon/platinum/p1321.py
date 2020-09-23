# 군인

import sys


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


def solve(xs, cs):
    xs = xs[:]
    tree = FenwickTree(xs)
    res = []
    for command in cs:
        if command[0] == 1:
            _, idx, diff = command
            tree.update(idx - 1, diff)
            xs[idx - 1] += diff
        else:
            _, nth = command
            left, right = 0, len(xs) - 1
            while left <= right:
                mid = (left + right) // 2
                upper = tree.get_range_value(0, mid)
                lower = upper - xs[mid]
                if nth > upper:
                    left = mid + 1
                elif nth <= lower:
                    right = mid - 1
                else:
                    res.append(mid + 1)
                    break
    return res


def main():
    stdin = sys.stdin
    _ = int(stdin.readline())
    xs = [int(x) for x in stdin.readline().split()]
    M = int(stdin.readline())
    cs = [[int(x) for x in stdin.readline().split()] for _ in range(M)]
    for r in solve(xs, cs):
        print(r)


if __name__ == "__main__":
    main()


from util import *
import pytest
import random


def solve_naive(xs, cs):
    res = []
    for command in cs:
        if command[0] == 1:
            _, idx, diff = command
            xs[idx-1] += diff
        else:
            _, nth = command
            acc = 0
            for idx, size in enumerate(xs):
                acc += size
                if nth <= acc:
                    res.append(idx + 1)
                    break
    return res


def test_compare():
    def gen_prob():
        N = 4
        xs = [random.randint(1, 5) for _ in range(N)]
        M = 2
        cs = []
        for _ in range(M):
            if random.random() < 0.5:
                idx = random.randint(1, N)
                diff = random.randint(-2, 2)
                cs.append((1, idx, diff))
                xs[idx-1] += diff
            else:
                ts = sum(xs)
                cs.append((2, random.randint(1, ts)))
        return xs, cs

    compare_func_results(solve, solve_naive, generate_probs(gen_prob, count=100))


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
5
1 4 3 5 2
5
1 2 -3
1 4 2
2 5
1 2 4
2 5
    '''.strip(),
     '''
3
2
     '''.strip()),
    ('''
4
2 2 5 6
2
1 4 2
2 10
    '''.strip(),
     '''
4
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
