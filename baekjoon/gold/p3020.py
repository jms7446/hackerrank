import sys


def solve(N, H, xs):
    obs = [0] * H
    for b in xs[::2]:
        obs[b] -= 1
    for t in xs[1::2]:
        obs[H - t] += 1

    bump = N // 2
    min_value = bump
    min_count = 0
    for h in range(H):
        bump += obs[h]
        if bump < min_value:
            min_value = bump
            min_count = 1
        elif bump == min_value:
            min_count += 1
    return min_value, min_count


def main():
    stdin = sys.stdin
    N, H = [int(x) for x in stdin.readline().split()]
    xs = [int(stdin.readline()) for _ in range(N)]
    print(*solve(N, H, xs))


if __name__ == "__main__":
    main()

from util import *


def test_main():
    in_str = """
14 5
1
3
4
2
2
4
3
4
3
3
3
2
3
3
    """.strip()
    out_str = """
7 2
    """.strip()
    assert evaluate_via_io(main, in_str) == out_str


def test_add():
    in_str = """
2 2
2
2
    """.strip()
    out_str = """
2 2
    """.strip()
    assert evaluate_via_io(main, in_str) == out_str


def test_add2():
    in_str = """
2 2
1
2
    """.strip()
    out_str = """
1 1
    """.strip()
    assert evaluate_via_io(main, in_str) == out_str
