import sys
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


def main():
    stdin = sys.stdin
    PN = int(stdin.readline())
    for _ in range(PN):
        N, M = [int(x) for x in stdin.readline().split()]
        print(ncr(M, N))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
3
2 2
1 5
13 29
""".strip()
    out_str = """
1
5
67863915
""".strip()
    assert get_output_with_stdin(main, in_str) == out_str
