# 아기 상어 2
import sys
from itertools import product


################################################################################
# From util
################################################################################

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

################################################################################


def bfs(starts, R, C):
    direction = Direction(8, R, C)
    visited = set(starts)
    stack = BFSStack(starts)
    for _, it in stack.next_step_iter():
        for cur_point in it:
            for next_point in direction.iter_next(cur_point):
                if next_point not in visited:
                    visited.add(next_point)
                    stack.append(next_point)
    return stack.step - 1


def solve(R, C, grid):
    starts = [(r, c) for r, c in product(range(R), range(C)) if grid[r][c] == 1]
    return bfs(starts, R, C)


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
