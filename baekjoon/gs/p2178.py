# 미로 탐색
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
    def get_mark(p):
        return grid[p[0]][p[1]]

    start, end = (0, 0), (R - 1, C - 1)
    stack = BFSStack([start])
    direction = Direction(4, R, C)
    visited = set()
    for step, it in stack.next_step_iter():
        for cur_pos in it:
            for next_pos in direction.iter_next(cur_pos):
                if next_pos in visited or get_mark(next_pos) == '0':
                    continue
                if next_pos == end:
                    return step + 1
                visited.add(next_pos)
                stack.append(next_pos)
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


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
4 6
101111
101010
101011
111011
    '''.strip(),
     '''
15
     '''.strip()),
    ('''
4 6
110110
110110
111111
111101
    '''.strip(),
     '''
9
     '''.strip()),
    ('''
2 25
1011101110111011101110111
1110111011101110111011101
    '''.strip(),
     '''
38
     '''.strip()),
    ('''
7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111
    '''.strip(),
     '''
13
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
