import sys

SCALE = 1000000007

cache = {}


def combination(n, r):
    if (n - r) < r:
        r = n - r
    numer = 1
    denom = 1
    for k in range(r):
        numer *= (n - k)
        denom *= (r - k)
    return numer // denom


def solve(N, L, R):
    L, R = max(L, R), min(L, R)
    M = L + R - 1
    if (N, L, R) == (1, 1, 1):
        return 1
    elif R < 1 or N < 1:
        return 0

    cache_key = (N, L, R)
    if cache_key in cache:
        return cache[cache_key]

    if M == N:
        res = combination(L + R - 2, L - 1)
    else:
        res = solve(N - 1, L, R) * (N - 2) + solve(N - 1, L - 1, R) + solve(N - 1, L, R - 1)
    cache[cache_key] = res
    return res % SCALE


def main():
    stdin = sys.stdin
    N, L, R = [int(x) for x in stdin.readline().split()]
    print(solve(N, L, R))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
3 2 2
        '''.strip(),
     '2'),
    ('''
4 2 2 
    '''.strip(),
     '6'),
    ('''
5 12 4
    '''.strip(),
     '0'),
    ('''
12 5 4
    '''.strip(),
     '5522055'),
    ('''
6 3 3
    '''.strip(),
     '60'),
])
def test_main(in_str, out_str):
    assert get_output_with_stdin(main, in_str) == out_str
