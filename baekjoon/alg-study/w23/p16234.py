# 인구 이동
import sys
from itertools import product, count


class Direction:
    def __init__(self, dir_type, R, C):
        if dir_type == 4:
            self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
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


def movement_population(N, L, R, grid):
    def get_population(state):
        return grid[state[0]][state[1]]

    def set_population(state, p):
        grid[state[0]][state[1]] = p

    def union_with(start_state):
        stack = [start_state]
        visited.add(start_state)
        union = {start_state}
        union_population = get_population(start_state)
        while stack:
            cur_state = stack.pop()
            cur_population = get_population(cur_state)
            for neighbor_state in direction.iter_next(cur_state):
                neighbor_population = get_population(neighbor_state)
                if neighbor_state not in visited and L <= abs(neighbor_population - cur_population) <= R:
                    visited.add(neighbor_state)
                    union.add(neighbor_state)
                    union_population += neighbor_population
                    stack.append(neighbor_state)

        avg_population = union_population // len(union)
        for state in union:
            set_population(state, avg_population)
        return len(union) > 1

    population_moved = False
    direction = Direction(4, N, N)
    visited = set()
    for state in product(range(N), range(N)):
        if state not in visited:
            population_moved = union_with(state) or population_moved

    return population_moved


def solve(N, L, R, grid):
    for step in count(0):
        population_moved = movement_population(N, L, R, grid)
        if not population_moved:
            return step


def main():
    stdin = sys.stdin
    N, L, R = [int(x) for x in stdin.readline().split()]
    grid = [[int(x) for x in stdin.readline().split()] for _ in range(N)]
    print(solve(N, L, R, grid))


if __name__ == "__main__":
    main()

from util import *
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
2 20 50
50 30
20 40
    '''.strip(),
     '''
1
     '''.strip()),
    ('''
2 40 50
50 30
20 40
    '''.strip(),
     '''
0
     '''.strip()),
    ('''
2 20 50
50 30
30 40
    '''.strip(),
     '''
1
     '''.strip()),
    ('''
1 1 1
1
    '''.strip(),
     '''
0
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
