import sys

# Horizontal, Vertical, Diagonal
H, V, D = range(3)


def solve_refer(n, house):
    pipe = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
    pipe[0][1][0] = 1
    for i, x in enumerate(pipe[0][2:]):
        if house[0][i + 2]:
            break
        pipe[0][i + 2][0] = pipe[0][i + 1][0]
    for i in range(1, n):
        for j in range(1, n):
            if house[i][j]:
                continue
            pipe[i][j][0] = pipe[i][j - 1][0] + pipe[i][j - 1][1]
            pipe[i][j][2] = pipe[i - 1][j][1] + pipe[i - 1][j][2]
            if house[i - 1][j] or house[i][j - 1]:
                continue
            pipe[i][j][1] = sum(pipe[i - 1][j - 1])
    return sum(pipe[n - 1][n - 1])


# 288
def solve2(n, grid):
    grid.append(['1'] * n)        # hack, padding for grid[-1][c] = 1

    costs = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
    costs[0][1][H] = 1
    for r in range(n):
        for c in range(2, n):
            if grid[r][c] != '1':
                costs[r][c][H] = costs[r][c-1][H] + costs[r][c-1][D]
                costs[r][c][V] = costs[r-1][c][V] + costs[r-1][c][D]
                if grid[r-1][c] != '1' and grid[r][c-1] != '1':
                    costs[r][c][D] = sum(costs[r-1][c-1])
    return sum(costs[n-1][n-1])


# 225.91µs
def solve(n, grid):
    grid.append(['1'] * n)        # hack, padding for grid[-1][c] = 1

    pre = [[0, 0, 0] for _ in range(n)]
    cur = [[0, 0, 0] for _ in range(n)]
    cur[1][H] = 1
    for r in range(n):
        for c in range(2, n):
            if grid[r][c] != '1':
                cur[c][H] = cur[c-1][H] + cur[c-1][D]
                cur[c][V] = pre[c][V] + pre[c][D]
                if grid[r-1][c] != '1' and grid[r][c-1] != '1':
                    cur[c][D] = sum(pre[c-1])
        pre = cur
        cur = [[0, 0, 0] for _ in range(n)]
    return sum(pre[n-1])


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    G = [[x for x in stdin.readline().split()] for _ in range(N)]
    print(solve(N, G))


if __name__ == "__main__":
    main()


from util import *


def test_time():
    N = 16
    grid = [[0] * N for _ in range(N)]
    timeit_lp(solve, (N, grid), num_iter=1000, time_limit=1)



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
