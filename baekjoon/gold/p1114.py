import sys


def right_remain_size(max_size, cut, xs):
    if xs[0] > max_size:
        return xs[-1]

    # FIXME 로직이 지저분하고 틀리는 곳이 존재. 갈끔하게 정리해보자.
    start = 0
    for i in range(1, len(xs)):
        if xs[i] - start <= max_size:
            continue
        cut -= 1
        start = xs[i - 1]
        if cut == 0:
            break
        if xs[i] - start > max_size:
            return xs[-1] - start
    return xs[-1] - start


def solve(L, K, C, xs):
    rxs = [L - x for x in reversed(xs)]
    rxs.append(L)

    left = 1
    right = L
    while left <= right:
        mid = (left + right) // 2
        if right_remain_size(mid, C, rxs) <= mid:
            right = mid - 1
        else:
            left = mid + 1

    left_most = right_remain_size(left, C, rxs)
    return left, left_most if left_most > 0 else xs[0]


def main():
    stdin = sys.stdin
    L, K, C = [int(x) for x in stdin.readline().split()]
    xs = [int(x) for x in stdin.readline().split()]
    print(*solve(L, K, C, xs))


if __name__ == "__main__":
    main()

from util import *
import pytest
import random


def test_compare():
    def gen_prob():
        L, K, C = 9, 3, 2
        xs = list(range(1, L-1))
        random.shuffle(xs)
        xs = sorted(xs[:K])
        return merge_to_lines([
            (L, K, C),
            xs,
        ])
    compare_func_results(mock_io(main), ext_binary_to_func('p1114'), generate_probs(gen_prob, count=100))


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
9 2 1
4 5
    '''.strip(),
     '''
5 4
     '''.strip()),
    ('''
5 2 2
2 3
    '''.strip(),
     '''
2 2
     '''.strip()),
    ('''
9 3 2
1 6 7
    '''.strip(),
     '''
5 1
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
