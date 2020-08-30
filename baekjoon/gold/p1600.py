import sys
from itertools import count

BASE_MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]
HORSE_MOVES = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]


def solve(K, W, H, G):
    def take_moves(moves, cost):
        """side-effect(modify): found_end, visited, new_stack"""
        nonlocal found_end, visited, new_stack

        if cost < 0:
            return

        for dx, dy in moves:
            x, y = px + dx, py + dy
            if not (0 <= x < W and 0 <= y < H):
                continue
            if visited[cost][y][x] or G[y][x] == '1':
                continue
            if (x, y) == end:
                found_end = True
                return
            visited[cost][y][x] = True
            new_stack.append((x, y, cost))

    start, end = (0, 0), (W - 1, H - 1)
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


from util.result_check import get_output_with_stdin


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
    assert get_output_with_stdin(main, in_str) == out_str


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
    assert get_output_with_stdin(main, in_str) == out_str


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
    assert get_output_with_stdin(main, in_str) == out_str


def test_main_trivial():
    in_str = """
0
1 1
0
    """.strip()
    out_str = """
0
    """.strip()
    assert get_output_with_stdin(main, in_str) == out_str
