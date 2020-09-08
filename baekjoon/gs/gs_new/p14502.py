import sys
from itertools import permutations

from .graph_search import *

ROOM, WALL, VIRUS = 0, 1, 2


def solve(N, M, X):
    map = TileMap(X, invalid_tiles=[1])
    viruses = list(map.find_all(VIRUS))
    rooms = list(map.find_all(ROOM))
    max_count = 0
    for rooms3 in permutations(rooms, 3):
        bfs = BFS(map, block_points=set(rooms3))
        bfs.search(viruses)
        cnt = bfs.checker.count_value_with_map(checker_value=False, map_value=0)
        max_count = max(max_count, cnt)

    return max_count


def main():
    stdin = sys.stdin
    N, M = [int(x) for x in stdin.readline().split()]
    X = [[int(x) for x in stdin.readline().split()] for _ in range(N)]
    print(solve(N, M, X))


if __name__ == "__main__":
    main()

from util import *
import pytest


def test_main():
    in_str = """
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
    """.strip()
    out_str = """
27
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_main2():
    in_str = """
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
    """.strip()
    out_str = """
9
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_main3():
    in_str = """
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
    """.strip()
    out_str = """
3
    """.strip()
    assert mock_io(main)(in_str) == out_str
