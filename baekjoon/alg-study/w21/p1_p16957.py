# 체스판 위의 공
import sys
from itertools import product
from collections import defaultdict

DIRECTIONS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def count_balls(point, flow_from):
    count = 0
    stack = [point]
    while stack:
        fr = stack.pop()
        count += 1
        if fr in flow_from:
            for fr2 in flow_from[fr]:
                stack.append(fr2)
    return count


def solve(R, C, grid):
    if R == 1 and C == 1:
        return [[1]]

    local_minimums = set()
    flow_from = defaultdict(list)
    for r, c in product(range(R), range(C)):
        neighbors = ((r + dr, c + dc) for dr, dc in DIRECTIONS)
        neighbors = ((grid[nr][nc], (nr, nc)) for nr, nc in neighbors if (0 <= nr < R and 0 <= nc < C))
        min_height, flow_to = min(neighbors)
        if min_height < grid[r][c]:
            flow_from[flow_to].append((r, c))
        else:
            local_minimums.add((r, c))

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
