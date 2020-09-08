import sys

from .graph_search import *


def solve(N, r1, c1, r2, c2):
    start = Point(r1, c1)
    end = Point(r2, c2)
    moves = (Point(-2, -1), Point(-2, 1), Point(0, -2), Point(0, 2), Point(2, -1), Point(2, 1))
    map = Map(N, N, moves=moves)
    return BFS(map, target_condition=lambda p: p == end).search([start])


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    r1, c1, r2, c2 = [int(x) for x in stdin.readline().split()]
    print(solve(N, r1, c1, r2, c2))


if __name__ == "__main__":
    main()


from util import *
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
7
6 6 0 1
        '''.strip(), '4'),
    ('''
6
5 1 0 5
        '''.strip(), '-1'),
    ('''
7
0 3 4 3
    '''.strip(), '2'),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
