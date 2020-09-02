import sys
from itertools import count

DIGITS = '0123456789'


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
        return [i for i, is_prime in enumerate(is_primes) if is_prime and i >= begin]


def iter_near_numbers(prime):
    for c in DIGITS:
        yield c + prime[1:]
        yield prime[:-1] + c
        yield prime[:1] + c + prime[2:]
        yield prime[:2] + c + prime[3:]


def search(fr, to, primes):
    if fr == to:
        return 0

    visited = set()

    stack = [fr]
    visited.add(fr)
    for step in count(1):
        if not stack:
            return step
        new_stack = []
        for prime in stack:
            for next_prime in iter_near_numbers(prime):
                if next_prime in visited or next_prime not in primes:
                    continue
                if next_prime == to:
                    return step
                visited.add(next_prime)
                new_stack.append(next_prime)
        stack = new_stack


def solve(pairs):
    primes = {str(d) for d in iter_primes(9999, begin=1000)}
    return [search(fr, to, primes) for fr, to in pairs]


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    pairs = [[x for x in stdin.readline().split()] for _ in range(N)]
    for res in solve(pairs):
        print(res if res is not None else 'Impossible')


if __name__ == "__main__":
    main()

from util import *


def test_main():
    in_str = """
3
1033 8179
1373 8017
1033 1033
    """.strip()
    out_str = """
6
7
0
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_time():
    in_str = """
    3
    1033 8179
    1373 8017
    1033 1033
        """.strip()
    timeit_lp(mock_io(main), in_str, funcs=[solve, search, iter_near_numbers])
