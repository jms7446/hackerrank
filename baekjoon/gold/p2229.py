import sys


def solve(N, xs):
    # hack, dp[N] will be used for indexing dp[-1] (must be remained 0)
    dp = [0] * (N + 1)

    for i in range(1, N):
        high = low = xs[i]
        dp[i] = dp[i - 1]
        for j in reversed(range(i)):
            high = max(high, xs[j])
            low = min(low, xs[j])
            dp[i] = max(dp[i], high - low + dp[j - 1])
    return dp[N - 1]


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    xs = [int(x) for x in stdin.readline().split()]
    print(solve(N, xs))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
10
2 5 7 1 3 4 8 6 9 3
    """.strip()
    out_str = """
20
    """.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_all_in_one():
    in_str = """
4
1 2 3 4
    """.strip()
    out_str = """
3
    """.strip()
    assert get_output_with_stdin(main, in_str) == out_str
