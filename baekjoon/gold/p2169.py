import sys

NINF = -1000000


def solve(X, N, M):
    # hack, to avoid special case; i == 0, i >= M
    top = [0] * (M + 1)
    left = [0] * (M + 1)
    right = [0] * (M + 1)
    left[M] = right[M] = NINF

    # for first line, now allowed left direction.
    for i in range(M):
        top[i] = top[i-1] + X[0][i]

    for n in range(1, N):
        for i in range(M):
            right[i] = max(right[i-1], top[i]) + X[n][i]
        for i in reversed(range(M)):
            left[i] = max(left[i+1], top[i]) + X[n][i]
        for i in range(M):
            top[i] = max(left[i], right[i], top[i] + X[n][i])
    return top[M-1]


def main():
    stdin = sys.stdin
    N, M = [int(x) for x in stdin.readline().split()]
    X = [[int(x) for x in stdin.readline().split()] for _ in range(N)]
    print(solve(X, N, M))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
5 5
10 25 7 8 13
68 24 -78 63 32
12 -69 100 -29 -25
-16 -22 -57 -33 99
7 -76 -11 77 15
""".strip()
    assert get_output_with_stdin(main, in_str) == "319"


def test_main2():
    in_str = """
1 1
3
""".strip()
    assert get_output_with_stdin(main, in_str) == "3"


def test_main3():
    in_str = """
1 3
3 1 0
""".strip()
    assert get_output_with_stdin(main, in_str) == "4"


def test_main4():
    in_str = """
3 1
1
-1
-5
""".strip()
    assert get_output_with_stdin(main, in_str) == "-5"


def test_main5():
    in_str = """
2 3
-1 -2 -3
-10 -10 0 
""".strip()
    assert get_output_with_stdin(main, in_str) == "-6"
