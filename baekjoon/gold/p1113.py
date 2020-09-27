# 수영장 만들기
import sys

MAX_HEIGHT = 9


class BFSStack:
    def __init__(self, starts=None, step=0):
        if starts:
            self.stack = starts[:]
        else:
            self.stack = []
        self.step = step

    def next_step_iter(self):
        while self.stack:
            self.step += 1
            stack = self.stack
            self.stack = []
            yield self.step, stack

    def append(self, v):
        self.stack.append(v)

    def __repr__(self):
        return f'BFSStack({self.stack}, {self.step})'


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

    def iter_next_with_half_padding(self, point):
        pr, pc = point
        for dr, dc in self.directions:
            r, c = pr + dr, pc + dc
            if -1 <= r <= self.R and -1 <= c <= self.C:
                yield r, c


def padding(grid, C):
    for row in grid:
        row.append(0)
    grid.append([0] * (C + 1))


def solve(R, C, grid):
    padding(grid, C)
    direction = Direction(4, R, C)
    visited = [[False] * (C + 1) for _ in range(R + 1)]

    starts = []
    for c in range(-1, C + 1):
        starts.append((R, c))
        starts.append((-1, c))
    for r in range(R):
        starts.append((r, C))
        starts.append((r, -1))

    water_amount = 0
    for r, c in starts:
        visited[r][c] = True
    stack = BFSStack(starts)
    for _, it in stack.next_step_iter():
        for pre_pos in it:
            min_height = MAX_HEIGHT
            for r, c in direction.iter_next_with_half_padding(pre_pos):
                if visited[r][c]:
                    min_height = min(min_height, grid[r][c])
                else:
                    stack.append((r, c))
                    visited[r][c] = True
            water_amount += max(0, min_height - grid[pre_pos[0]][pre_pos[1]])
            # FIXME 실패!!! 물은 밖으로만 향하는 것이 아니라, 내부를 거쳐 반대편 밖으로도 나갈 수 있다.
    return water_amount


def main():
    stdin = sys.stdin
    R, C = [int(x) for x in stdin.readline().split()]
    grid = [[int(x) for x in stdin.readline().strip()] for _ in range(R)]
    print(solve(R, C, grid))


if __name__ == "__main__":
    main()

from util import *
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
3 5
16661
61116
16661
    '''.strip(),
     '''
15
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
