import sys
from collections import Counter


def solve(_, H, xs):

    bs = Counter(b - 1 for b in xs[::2])
    ts = Counter(H-t for t in xs[1::2])

    acc_bs = [0] * H
    acc_bs[H - 1] = bs[H - 1]
    for h in reversed(range(H - 1)):
        acc_bs[h] = bs[h] + acc_bs[h + 1]

    acc_ts = [0] * H
    acc_ts[0] = ts[0]
    for h in range(1, H):
        acc_ts[h] = ts[h] + acc_ts[h - 1]

    counts = [b + t for b, t in zip(acc_bs[:H], acc_ts[:H])]
    max_value = min(counts)
    max_count = counts.count(max_value)
    return max_value, max_count


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
