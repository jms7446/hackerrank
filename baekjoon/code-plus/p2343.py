import sys
import math
from itertools import accumulate
from operator import add
from bisect import bisect


def check_capacity(capacity, N, M, acc_xs):
    split_idx = 0
    x_base = 0
    for i in range(M):
        split_idx = bisect(acc_xs, x_base + capacity, lo=split_idx)
        x_base = acc_xs[split_idx - 1]
    if split_idx >= N:
        return True
    return False


def solve(N, M, xs):
    acc_xs = list(accumulate(xs, add))
    left = max(math.ceil(acc_xs[-1] / M), max(xs))
    right = acc_xs[-1]
    capacity = -1
    while left <= right:
        mid = (left + right) // 2
        if check_capacity(mid, N, M, acc_xs):
            capacity = mid
            right = mid - 1
        else:
            left = mid + 1
    return capacity


def main():
    stdin = sys.stdin
    N, M = [int(x) for x in stdin.readline().split()]
    xs = [int(x) for x in stdin.readline().split()]
    print(solve(N, M, xs))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = '''
9 3
1 2 3 4 5 6 7 8 9
    '''.strip()

    out_str = '''
17
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main2():
    in_str = '''
9 1
1 2 3 4 5 6 7 8 9
    '''.strip()

    out_str = '''
45
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str
