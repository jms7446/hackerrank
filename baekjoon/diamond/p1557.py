import sys
import math
from itertools import takewhile
from functools import reduce
from operator import mul


def combination_prod_bound(xs, upper_bound):
    def search(idx, acc, q):
        if acc <= upper_bound:
            res.append(q)
        if acc > upper_bound or idx >= len(xs):
            return
        for i in range(idx, len(xs)):
            search(i + 1, acc * xs[i], q + [xs[i]])

    res = []
    for i in range(len(xs)):
        search(i + 1, xs[i], [xs[i]])
    return res


def test_cb():
    expected = sorted([[2, ], [3, ], [5, ], [7, ], [2, 3], [2, 5], [2, 7], [3, 5]])
    assert sorted(combination_prod_bound([2, 3, 5, 7], 16)) == expected


def iter_primes(max_value, begin=None):
    is_primes = [True] * (max_value + 1)
    is_primes[0] = is_primes[1] = False
    for i in range(2, (max_value + 1) // 2):
        if is_primes[i]:
            j = 2 * i
            while j <= max_value:
                is_primes[j] = False
                j += i
    if begin is None:
        return (i for i, is_prime in enumerate(is_primes) if is_prime)
    else:
        return (i for i, is_prime in enumerate(is_primes) if is_prime and i >= begin)


max_prime = 100
primes = list(iter_primes(max_prime))


def compare_to_solution(n, k):
    global max_prime, primes
    if n > max_prime ** 2:
        eprint('>>>>>>>>> re prime')
        max_prime = int(math.sqrt(n))
        primes = list(iter_primes(max_prime))

    prime_squares = list(takewhile(lambda x: x <= n, (i ** 2 for i in primes)))
    sq_count = 0
    for nums in combination_prod_bound(prime_squares, n):
        sign = (-1) ** (len(nums) + 1)
        sq_count += n // reduce(mul, nums) * sign
    nn_count = n - sq_count
    if nn_count > k:
        return 1
    elif nn_count < k:
        return -1
    elif any(n % pp == 0 for pp in prime_squares):  # n이 sq_num이면 찾는 수는 더 작다.
        return 1
    else:
        return 0


def solve(k):
    global max_prime, primes
    max_prime = int(math.sqrt(2 * k))
    primes = list(iter_primes(max_prime))

    left = k
    right = 2 * k
    # while compare_to_solution(right, k) < 0:
    #     left = right
    #     right *= 2
    while left <= right:
        mid = (left + right) // 2
        cmp = compare_to_solution(mid, k)
        if cmp > 0:
            right = mid - 1
        elif cmp < 0:
            left = mid + 1
        else:
            return mid
    return -1


def main():
    stdin = sys.stdin
    k = int(stdin.readline())
    print(solve(k))


if __name__ == "__main__":
    main()

from util import *
import pytest


def test_time():
    timeit_lp(solve, (100000, ), funcs=[compare_to_solution, iter_primes, combination_prod_bound])


# 1, 2, 3, 5, 6, 7, 10, 11, 13, 14
# 15, 17, 19, 21
@pytest.mark.parametrize(('in_str', 'out_str'), [
    # ('13', '19'),
    # ('14', '21'),
    # ('16', '23'),
    # ('1000000', '-1'),
    ('1000000000', '-1'),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str


