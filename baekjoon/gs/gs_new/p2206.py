# 벽 부수고 이동하기
import sys


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


def solve(R, C, grid):
    def get_mark(pos):
        return grid[pos[0]][pos[1]]

    start, end = (0, 0), (R - 1, C - 1)
    if start == end:
        return 1

    direction = Direction(4, R, C)

    stack = BFSStack([(start, 0)], step=1)
    visited = [{start}, set()]
    for step, it in stack.next_step_iter():
        for pre_pos, break_count in it:
            for pos in direction.iter_next(pre_pos):
                if pos in visited[break_count]:
                    continue
                if pos == end:
                    return step
                if get_mark(pos) == '0':
                    visited[break_count].add(pos)
                    stack.append((pos, break_count))
                elif break_count == 0:
                    visited[break_count + 1].add(pos)
                    stack.append((pos, break_count + 1))
    return -1


# 206.16µs
def solve3(R, C, grid):
    start, end = (0, 0), (R - 1, C - 1)
    if start == end:
        return 1

    direction = Direction(4, R, C)

    stack = BFSStack([(start, 0)], step=1)
    visited = [[[False] * C for _ in range(R)] for _ in range(2)]
    for step, it in stack.next_step_iter():
        for pre_pos, break_count in it:
            for r, c in direction.iter_next(pre_pos):
                if visited[break_count][r][c]:
                    continue
                if (r, c) == end:
                    return step
                if grid[r][c] == '0':
                    visited[break_count][r][c] = True
                    stack.append(((r, c), break_count))
                elif break_count == 0:
                    visited[break_count][r][c] = True
                    stack.append(((r, c), break_count + 1))
    return -1


def main():
    stdin = sys.stdin
    R, C = [int(x) for x in stdin.readline().split()]
    grid = [stdin.readline().strip() for _ in range(R)]
    print(solve(R, C, grid))


if __name__ == "__main__":
    main()

from util import *
import pytest
import random


def test_time():
    def gen_prob():
        R, C = 1000, 1000
        grid = [[1 if random.random() < 0.5 else 0 for _ in range(C)] for _ in range(R)]
        return R, C, grid
    timeit_lp(solve, gen_prob())


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
6 4
0100
1110
1000
0000
0111
0000
    '''.strip(),
     '''
15
     '''.strip()),
    ('''
4 4
0111
1111
1111
1110
    '''.strip(),
     '''
-1
     '''.strip()),
    ('''
1 1
0
    '''.strip(),
     '''
1
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
