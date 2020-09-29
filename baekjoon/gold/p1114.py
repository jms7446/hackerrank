import sys


def leftmost_size(max_size, cut, xs):
    end = xs[-1]
    for i in reversed(range(len(xs) - 1)):
        if end - xs[i] > max_size:
            cut -= 1
            end = xs[i + 1]
            if end - xs[i] > max_size:
                return end
            if cut == 0:
                break
    if cut > 0:
        end = xs[1]
    return end


def solve(L, K, C, xs):
    xs = [0] + sorted(xs) + [L]

    left = 1
    right = L - 1
    while left <= right:
        mid = (left + right) // 2
        if leftmost_size(mid, C, xs) <= mid:
            right = mid - 1
        else:
            left = mid + 1
    return left, leftmost_size(left, C, xs)


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
        K = random.randint(1, 100)
        C = random.randint(1, 100)
        L = random.randint(K + 1, 1000)
        xs = list(range(1, L))
        random.shuffle(xs)
        xs = sorted(xs[:K])
        return merge_to_lines([
            (L, K, C),
            xs,
        ])
    compare_func_results(mock_io(main), ext_binary_to_func('p1114'), generate_probs(gen_prob, count=10))


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
    ('''
2 3 2

    '''.strip(),
     '''
2 1
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
