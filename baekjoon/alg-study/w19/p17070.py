import sys

# Horizontal, Vertical, Diagonal
H, V, D = range(3)


def solve(n, grid):
    grid.append([1] * n)        # hack, padding for grid[-1][c] = 1

    pre = [[0, 0, 0] for _ in range(n)]
    cur = [[0, 0, 0] for _ in range(n)]
    cur[1][H] = 1
    for r in range(n):
        for c in range(2, n):
            if grid[r][c] != 1:
                cur[c][H] = cur[c-1][H] + cur[c-1][D]
                cur[c][V] = pre[c][V] + pre[c][D]
                if grid[r-1][c] != 1 and grid[r][c-1] != 1:
                    cur[c][D] = sum(pre[c-1])
        pre = cur
        cur = [[0, 0, 0] for _ in range(n)]
    return sum(pre[n-1])


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    G = [[int(x) for x in stdin.readline().split()] for _ in range(N)]
    print(solve(N, G))


if __name__ == "__main__":
    main()


from util import *


def test_main():
    in_str = """
3
0 0 0
0 0 0
0 0 0
    """.strip()
    out_str = """
1
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_main2():
    in_str = """
4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
    """.strip()
    out_str = """
3
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_main3():
    in_str = """
5
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
    """.strip()
    out_str = """
0
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_main4():
    in_str = """
6
0 0 0 0 0 0
0 1 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
    """.strip()
    out_str = """
13
    """.strip()
    assert mock_io(main)(in_str) == out_str
