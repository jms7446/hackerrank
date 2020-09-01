import sys

MOD = 1000000007


# 3.44s
# 2.95
def solve3(N, L, R):
    if L > R:
        L, R = R, L
    dp = [[[-1] * (R + 1) for _ in range(L + 1)] for _ in range(N + 1)]
    dp[1][1][1] = 1

    def loop(n, l, r):
        if l <= 0 or r <= 0 or n <= 0:
            return 0
        if dp[n][l][r] >= 0:
            return dp[n][l][r]

        if l == r:
            res = loop(n - 1, l, r) * (n - 2) + loop(n - 1, l - 1, r) * 2
        else:
            res = loop(n - 1, l, r) * (n - 2) + loop(n - 1, l - 1, r) + loop(n - 1, l, r - 1)
        res %= MOD
        dp[n][l][r] = res
        return res
    return loop(N, L, R)


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


# 5.53s
def solve1(N, L, R):
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
        res = solve1(N - 1, L, R) * (N - 2) + solve1(N - 1, L - 1, R) + solve1(N - 1, L, R - 1)
    cache[cache_key] = res
    return res % MOD


# 4.17s
def solve2(N, L, R):
    dp = [[[0] * (R + 1) for _ in range(L + 1)] for _ in range(N + 1)]
    dp[1][1][1] = 1
    for n in range(2, N + 1):
        for l in range(1, L + 1):
            for r in range(1, R + 1):
                dp[n][l][r] = ((n - 2) * dp[n-1][l][r] + dp[n-1][l-1][r] + dp[n-1][l][r-1]) % MOD
    return dp[N][L][R]


# 1.8s
def solve(N, L, R):
    # by symetry, only consider the cases r >= l
    if L > R:
        L, R = R, L
    # trivial case
    if N == R:
        return int(L == 1)

    # we need dp array for n and (n-1), use two array with swapping.
    dpc = [[0] * (R + 1) for _ in range(L + 1)]
    dpn = [[0] * (R + 1) for _ in range(L + 1)]
    dpc[1][1] = dpn[1][1] = 1
    for n in range(2, N + 1):
        dpc, dpn = dpn, dpc
        for l in range(1, L + 1):
            dpc[l][l] = ((n - 2) * dpn[l][l] + 2 * dpn[l - 1][l]) % MOD
            for r in range(l + 1, R + 1):
                dpc[l][r] = ((n - 2) * dpn[l][r] + dpn[l - 1][r] + dpn[l][r - 1]) % MOD
    return dpc[L][R]


def main():
    stdin = sys.stdin
    N, L, R = [int(x) for x in stdin.readline().split()]
    print(solve(N, L, R))


if __name__ == "__main__":
    main()


from util import *
import pytest

import random
import time


def test_profile():
    global cache
    T = 100
    random.seed(3)
    st = time.time()
    for _ in range(T):
        N = random.randint(1, 100)
        L = random.randint(1, N)
        R = random.randint(1, N)
        solve(N, L, R)
        cache = {}
    print('elapse time : ', time.time() - st, file=sys.stderr)


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
12 5 4
    '''.strip(),
     '5522055'),
    ('''
6 3 3
    '''.strip(),
     '60'),
])
def test_main(in_str, out_str):
    assert evaluate_via_io(main, in_str) == out_str


