# 아기 상어 2
import sys
from itertools import product

DIRECTIONS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def bfs(starts, R, C):
    dists = [[-1] * C for _ in range(R)]
    stack = []
    for r, c in starts:
        stack.append((r, c))
        dists[r][c] = 0

    step = 0
    while stack:
        step += 1
        new_stack = []
        for r, c in stack:
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < R and 0 <= nc < C) or dists[nr][nc] != -1:
                    continue
                dists[nr][nc] = step
                new_stack.append((nr, nc))
        stack = new_stack
    return dists


def solve(R, C, grid):
    starts = [(r, c) for r, c in product(range(R), range(C)) if grid[r][c] == 1]
    dists = bfs(starts, R, C)
    return max(max(row) for row in dists)


def main():
    stdin = sys.stdin
    R, C = [int(x) for x in stdin.readline().split()]
    grid = [[int(x) for x in stdin.readline().split()] for _ in range(R)]
    print(solve(R, C, grid))


if __name__ == "__main__":
    main()


from util import *
import pytest
import random


def test_compare():
    def gen_prob():
        R, C = 4, 4
        grid = [[1 if random.random() < 0.2 else 0 for _ in range(C)] for _ in range(R)]
        return merge_to_lines([
            (R, C),
            merge_to_lines(grid),
        ])
    compare_func_results(mock_io(main), ext_binary_to_func('p17086'), generate_probs(gen_prob, count=100))


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
5 4
0 0 1 0
0 0 0 0
1 0 0 0
0 0 0 0
0 0 0 1
    '''.strip(),
     '''
2
     '''.strip()),
    ('''
7 4
0 0 0 1
0 1 0 0
0 0 0 0
0 0 0 1
0 0 0 0
0 1 0 0
0 0 0 1
    '''.strip(),
     '''
2
     '''.strip()),
    ('''
2 2
1 1
0 1
    '''.strip(),
     '''
1
     '''.strip()),
    ('''
4 4
0 0 0 0
1 0 0 0
0 0 0 0
0 0 1 0
    '''.strip(),
     '''
3
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
