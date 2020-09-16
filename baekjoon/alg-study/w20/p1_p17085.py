import sys


def solve(n, m, grid):
    return -1


def main():
    stdin = sys.stdin
    n, m = [int(x) for x in stdin.readline().split()]
    grid = [stdin.readline().strip() for _ in range(n)]
    print(solve(n, m, grid))


if __name__ == "__main__":
    main()

from util import *
import pytest


def test_main():
    in_str = """
5 6
######
#...#.
######
##..#.
######
    """.strip()
    out_str = '5'
    assert mock_io(main)(in_str) == out_str


def test_main2():
    in_str = """
6 6
.#..#.
######
.#..#.
######
.#..#.
.#..#.
    """.strip()
    out_str = '25'
    assert mock_io(main)(in_str) == out_str
