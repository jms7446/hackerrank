import sys


def solve(N, xs):
    table = [set() for _ in range(N)]
    for idx, x in enumerate(xs):
        table[x].add(idx)
    stack = [idx for idx, s in enumerate(table) if not s]
    while stack:
        idx = stack.pop()
        nxt = xs[idx]
        table[nxt].remove(idx)
        if not table[nxt]:
            stack.append(nxt)
    return sorted(idx for idx, s in enumerate(table) if s)


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    X = [int(x) - 1 for x in stdin.readlines()]
    res = solve(N, X)
    print(len(res))
    print('\n'.join(str(x + 1) for x in res))


if __name__ == "__main__":
    main()

from util import *


def test_main():
    in_str = """
7
3
1
1
5
5
4
6
    """.strip()
    out_str = """
3
1
3
5
    """.strip()
    assert evaluate_via_io(main, in_str) == out_str


def test_add1():
    in_str = """
1
1
    """.strip()
    out_str = """
1
1
    """.strip()
    assert evaluate_via_io(main, in_str) == out_str


def test_add2():
    in_str = """
3
2
2
1
    """.strip()
    out_str = """
1
2
    """.strip()
    assert evaluate_via_io(main, in_str) == out_str
