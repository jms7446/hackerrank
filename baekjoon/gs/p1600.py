import sys
from itertools import count

BASE_MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]
HORSE_MOVES = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]


def padding2(G, W, H, c):
    v_pad = [c * (W + 4)] * 2
    G = [c * 2 + line + c * 2 for line in G]
    G = v_pad + G + v_pad
    return G, W + 4, H + 4


def solve(K, W, H, G):
    def take_moves(moves, cost):
        """side-effect(modify): found_end, visited, new_stack"""
        nonlocal found_end, visited, new_stack

        if cost < 0:
            return

        for dx, dy in moves:
            x, y = px + dx, py + dy
            if visited[cost][y][x] or G[y][x] == '1':
                continue
            if (x, y) == end:
                found_end = True
                return
            visited[cost][y][x] = True
            new_stack.append((x, y, cost))

    G, W, H = padding2(G, W, H, '1')
    start, end = (2, 2), (W - 1 - 2, H - 1 - 2)
    if start == end:
        return 0
    visited = [[[False] * W for _ in range(H)] for _ in range(K + 1)]

    sx, sy = start
    stack = [(sx, sy, K)]
    visited[K][sy][sx] = True
    found_end = False
    for step in count(1):
        if not stack:
            break
        new_stack = []
        for px, py, k in stack:
            take_moves(BASE_MOVES, k)
            if found_end:
                return step
            take_moves(HORSE_MOVES, k - 1)
            if found_end:
                return step
        stack = new_stack
    return -1


def main():
    stdin = sys.stdin
    K = int(stdin.readline())
    W, H = [int(x) for x in stdin.readline().split()]
    G = [''.join(stdin.readline().split()) for _ in range(H)]
    print(solve(K, W, H, G))


if __name__ == "__main__":
    main()


from util import *


def test_main():
    in_str = """
1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0
    """.strip()
    out_str = """
4
    """.strip()
    assert evaluate_via_io(main, in_str) == out_str


def test_main_impossible():
    in_str = """
4
4 4
0 0 0 0
0 0 1 0
0 1 1 1
0 0 1 0
    """.strip()
    out_str = """
-1
    """.strip()
    assert evaluate_via_io(main, in_str) == out_str


def test_main_possible():
    in_str = """
1
4 4
0 0 0 0
0 0 1 1
0 0 1 1
0 1 1 0
    """.strip()
    out_str = """
4
    """.strip()
    assert evaluate_via_io(main, in_str) == out_str


def test_main_trivial():
    in_str = """
0
1 1
0
    """.strip()
    out_str = """
0
    """.strip()
    assert evaluate_via_io(main, in_str) == out_str
