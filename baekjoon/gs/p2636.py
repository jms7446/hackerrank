import sys
from itertools import count

DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def solve(R, C, G):
    if R <= 2 or C <= 2:
        return 0, 0

    visited = [[False] * C for _ in range(R)]
    air_set = set()
    for r in range(R):
        visited[r][0] = True
        visited[r][C-1] = True
        air_set.add((r, 0))
        air_set.add((r, C-1))
    for c in range(C):
        visited[0][c] = True
        visited[R-1][c] = True
        air_set.add((0, c))
        air_set.add((R-1, c))

    remain_cheese_count = 0
    for step in count(0):
        cheese_set = set()
        while air_set:
            pr, pc = air_set.pop()
            for dr, dc in DIRECTIONS:
                r, c = pr + dr, pc + dc
                if not (0 <= r < R and 0 <= c < C) or visited[r][c]:
                    continue
                if G[r][c] == 0:
                    air_set.add((r, c))
                    visited[r][c] = True
                else:
                    cheese_set.add((r, c))

        if not cheese_set:
            return step, remain_cheese_count

        remain_cheese_count = len(cheese_set)
        for r, c in cheese_set:
            G[r][c] = 0
            visited[r][c] = True
            air_set.add((r, c))

    return -1


def main():
    stdin = sys.stdin
    R, C = [int(x) for x in stdin.readline().split()]
    G = [[int(x) for x in stdin.readline().split()] for _ in range(R)]
    res = solve(R, C, G)
    print(res[0])
    print(res[1])


if __name__ == "__main__":
    main()


from util import *


def test_main():
    in_str = """
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
    """.strip()
    out_str = """
3
5
    """.strip()
    assert evaluate_via_io(main, in_str) == out_str


def test_add1():
    in_str = """
4 4
0 0 0 0
0 0 1 0
0 1 1 0
0 0 0 0
    """.strip()
    out_str = """
1
3
    """.strip()
    assert evaluate_via_io(main, in_str) == out_str
