import sys

# I use the the fact that palindrome number bigger than 1000000 is 1003001.
MAX_NUM = 1005000


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


def is_palindrome(d):
    s = str(d)
    half = len(s) // 2
    return s[:half] == s[-1:-half-1:-1]


def solve(N):
    primes = iter_primes(MAX_NUM, begin=N)
    for p in primes:
        if is_palindrome(p):
            return p
    return -1


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    print(solve(N))


if __name__ == "__main__":
    main()

from util import *
import pytest


def test_main():
    in_str = """
31
    """.strip()
    out_str = """
101
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_add():
    assert mock_io(main)('124125') == '1003001'


@pytest.mark.skip
def test_time():
    timeit_lp(solve, 31, funcs=[])
