import sys
from functools import reduce, lru_cache
from operator import mul
from math import factorial


@lru_cache(10000)
def permutations_with_dup(counts):
    return factorial(sum(counts)) // reduce(mul, (factorial(i) for i in counts if i >= 2), 1)


def iter_valid_cases(N):
    for t2 in range(N // 2 + 1):
        for s2 in range((N - t2 * 2) // 2 + 1):
            s1 = N - 2 * (t2 + s2)
            yield t2, s2, s1


def encode_state(counts):
    return tuple(sorted([c for c in counts if c > 0], reverse=True))


def calc_symmetry_counts(state):
    odds_count = len([d for d in state if d % 2 == 1])
    if odds_count <= 1:
        state = tuple(x // 2 for x in state)
        return permutations_with_dup(state)
    return 0


# test_time1: 307.63µs
def solve(N):
    def calc_counts(state):
        if state == () or state == (1, ):
            return 1
        elif state in memory:
            return memory[state]

        all_counts = permutations_with_dup(state)
        symmetric_counts = calc_symmetry_counts(state)
        memory[state] = (all_counts + symmetric_counts) // 2
        return memory[state]

    memory = {}
    total_counts = 0
    for counts in iter_valid_cases(N):
        state = encode_state(counts)
        total_counts += calc_counts(state)
    return total_counts


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    print(solve(N))


if __name__ == "__main__":
    main()

from util import *
import pytest


@pytest.mark.parametrize(['n', 'e'], [
    (1, 1),
    (2, 3),
    (3, 3),
    (4, 8),
    (5, 12),
    (6, 27),
    (7, 45),
    (8, 96),
    (30, 357935787),
])
def test_main(n, e):
    assert evaluate_via_io(main, str(n)) == str(e)


def test_time1():
    timeit(solve, (30, ), num_iter=10000, time_limit=0.5)
