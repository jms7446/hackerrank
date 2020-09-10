import sys
from itertools import combinations
from operator import mul
from functools import reduce


# 574.15µs
def solve1(N, M, primes):
    count = 0
    for s in range(1, N + 1):
        sign = (-1) ** (s + 1)
        for nums in combinations(primes, s):
            num = reduce(mul, nums)
            count += M // num * sign
    return count


# 513.25µs
def solve(N, M, primes):
    count = 0
    for s in range(1, N + 1):
        sign = (-1) ** (s + 1)
        for nums in combinations(primes, s):
            m = M
            for num in nums:
                m //= num
            count += m * sign
    return count


# 537.89µs
def solve3(N, M, primes):
    count = 0
    for group_size in range(1, N + 1):
        sign = (-1) ** (group_size + 1)
        count += sign * sum(M // reduce(mul, nums) for nums in combinations(primes, group_size))
    return count


# 542.50µ
def solve2(N, M, primes):
    count = 0
    total_prod = reduce(mul, primes)
    for s in range(1, N + 1):
        sign = (-1) ** (s + 1)
        if s < N // 2:
            count += sign * sum(M // reduce(mul, nums) for nums in combinations(primes, s))
        else:
            count += sign * sum(M // (total_prod // reduce(mul, nums, 1)) for nums in combinations(primes, N - s))
    return count


def main():
    stdin = sys.stdin
    N, M = [int(x) for x in stdin.readline().split()]
    primes = [int(x) for x in stdin.readline().split()]
    print(solve(N, M, primes))


if __name__ == "__main__":
    main()

from util import *
import pytest


def test_time():
    N = 10
    M = 10 ** 12
    primes = [2, 3, 5, 7, 9, 11, 13, 17, 19, 23]
    timeit_lp(solve, (N, M, primes), num_iter=10000, time_limit=1)  #, log=True, changed='use sum')


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
1 100
3
    '''.strip(), '33'.strip()),
    ('''
2 100
2 3
    '''.strip(), '67'.strip()),
    ('''
3 100
2 3 5
    '''.strip(), '74'.strip()),
    ('''
4 100
2 3 5 7
    '''.strip(), '78'.strip()),
    ('''
5 100
11 13 17 19 23
    '''.strip(), '30'.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
