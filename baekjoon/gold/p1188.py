import sys
from math import ceil


# 1.56ms
def solve_old(N, M):
    def f(n, m):
        if n == 0 or m <= 1:
            return 0

        if n >= m:
            return f(n % m, m)
        else:
            base_cuts = ceil(m / n) - 1
            return base_cuts * n + f(n, m % n)

    return f(N, M)


# 668.80µs
def solve_old2(sausages, people):
    cuts = 0
    while people > 1:
        sausages %= people
        if sausages == 0:
            return cuts
        cuts += (ceil(people / sausages) - 1) * sausages
        people %= sausages
    return cuts


# 599.23µs
def solve(sausages, people):
    cuts = 0
    while people > 1:
        sausages %= people
        if sausages == 0:
            return cuts
        q, r = divmod(people, sausages)
        if r == 0:
            cuts += (q - 1) * sausages
        else:
            cuts += q * sausages
        people = r
    return cuts


def main():
    stdin = sys.stdin
    N, M = [int(x) for x in stdin.readline().split()]
    print(solve(N, M))


if __name__ == "__main__":
    main()


from util import *
import pytest


def test_time():
    import random
    random.seed(2)
    T = 1000
    args_list = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(T)]
    timeits(solve, args_list, num_iter=100)


@pytest.mark.parametrize(('N', 'M', 'expected'), [
    (2, 6, 4),
    (3, 4, 3),
    (1, 1, 0),
    (2, 2, 0),
    (3, 5, 4),
    (7, 3, 2),
    (3, 7, 6),
])
def test_main(N, M, expected):
    assert solve(N, M) == expected
