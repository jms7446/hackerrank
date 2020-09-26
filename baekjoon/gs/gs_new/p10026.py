# 적록색약

import sys
from itertools import product


class Direction:
    def __init__(self, dir_type, R, C):
        if dir_type == 4:
            self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        elif dir_type == 8:
            self.directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        else:
            raise Exception(f'Unknown dir_type: {dir_type}')
        self.R = R
        self.C = C

    def iter_next(self, point):
        pr, pc = point
        for dr, dc in self.directions:
            r, c = pr + dr, pc + dc
            if 0 <= r < self.R and 0 <= c < self.C:
                yield r, c


def grid_to_map(grid):
    return {(r, c): mark for r, row in enumerate(grid) for c, mark in enumerate(row)}


def solve(R, grid):
    def roar(start, colors, visited):
        stack = [start]
        while stack:
            pre_pos = stack.pop()
            for pos in direction.iter_next(pre_pos):
                if pos in visited or grid[pos] not in colors:
                    continue
                visited.add(pos)
                stack.append(pos)

    grid = grid_to_map(grid)
    direction = Direction(4, R, R)

    visited = set()
    region_count = 0
    for pos in product(range(R), range(R)):
        if pos not in visited:
            colors = (grid[pos], )
            roar(pos, colors, visited)
            region_count += 1

    visited = set()
    region_count2 = 0
    for pos in product(range(R), range(R)):
        if pos not in visited:
            if grid[pos] == 'B':
                colors = ('B', )
            else:
                colors = ('R', 'G')
            roar(pos, colors, visited)
            region_count2 += 1

    return region_count, region_count2


def main():
    stdin = sys.stdin
    R = int(stdin.readline())
    grid = [stdin.readline().strip() for _ in range(R)]
    print(*solve(R, grid))


if __name__ == "__main__":
    main()

from util import *
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
    '''.strip(),
     '''
4 3
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
