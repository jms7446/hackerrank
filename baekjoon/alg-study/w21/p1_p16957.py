# 체스판 위의 공
import sys
from itertools import product
from collections import defaultdict


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


def count_balls(point, flow_from):
    count = 0
    stack = [point]
    while stack:
        fr = stack.pop()
        count += 1
        if fr not in flow_from:
            continue
        for fr2 in flow_from[fr]:
            stack.append(fr2)
    return count


def solve(R, C, grid):
    def get_height(point):
        return grid[point[0]][point[1]]

    if R == 1 and C == 1:
        return [[1]]

    local_minimums = set()
    flow_from = defaultdict(list)
    direction = Direction(8, R, C)
    for cur_point in product(range(R), range(C)):
        neighbor_heights = ((get_height(neighbor), neighbor) for neighbor in direction.iter_next(cur_point))
        min_height, flow_to = min(neighbor_heights)
        if min_height < get_height(cur_point):
            flow_from[flow_to].append(cur_point)
        else:
            local_minimums.add(cur_point)

    def count_balls_finally(point):
        if point in local_minimums:
            return count_balls(point, flow_from)
        else:
            return 0
    return [[count_balls_finally((r, c)) for c in range(C)] for r in range(R)]


def main():
    stdin = sys.stdin
    R, C = [int(x) for x in stdin.readline().split()]
    grid = [[int(x) for x in stdin.readline().split()] for _ in range(R)]
    for row in solve(R, C, grid):
        print(*row)


if __name__ == "__main__":
    main()

from util import *
import pytest
import random


def test_compare():
    def gen_prob():
        R, C = random.randint(1, 4), random.randint(1, 4)
        # R, C = 3, 1
        R, C = 500, 500
        nums = list(range(R * C))
        random.shuffle(nums)
        grid = [nums[r*C:(r+1)*C] for r in range(R)]
        return merge_to_lines([
            (R, C),
            merge_to_lines(grid),
        ])
        # return R, C, grid

    timeit(mock_io(main), gen_prob())


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
3 3
1 3 4
5 6 7
8 9 2
    '''.strip(),
     '''
6 0 0
0 0 0
0 0 3
     '''.strip()),
    ('''
1 6
10 20 3 4 5 6
'''.strip(),
     '''
1 0 5 0 0 0 
     '''.strip()),
    ('''
4 4
20 2 13 1
4 11 10 35
3 12 9 7
30 40 50 5
'''.strip(),
     '''
0 4 0 4
0 0 0 0
4 0 0 0
0 0 0 4
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
