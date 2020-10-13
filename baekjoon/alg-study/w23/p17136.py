#색종이 붙이기
import sys

INF = float('inf')


def solve(grid, N, K, M):
    def dfs(r, c, count):
        nonlocal min_count
        if r == N:
            min_count = min(min_count, count)
        elif grid[r][c] == 0:
            next_r, next_c = get_next_pos(r, c)
            dfs(next_r, next_c, count)
        else:
            for size in range(1, K + 1):
                if not can_expand_size(r, c, size):
                    break
                if remains[size] == 0:
                    continue
                attach(r, c, size)
                remains[size] -= 1
                next_r, next_c = get_next_pos(r, c)
                dfs(next_r, next_c, count + 1)
                detach(r, c, size)
                remains[size] += 1

    def can_expand_size(r, c, size):
        if r + size > N or c + size > N:
            return False
        for s in range(size):
            if grid[r + size - 1][c + s] == 0:
                return False
            if grid[r + s][c + size - 1] == 0:
                return False
        return True

    def attach(r, c, size):
        for row in range(r, r + size):
            for col in range(c, c + size):
                grid[row][col] = 0

    def detach(r, c, size):
        for row in range(r, r + size):
            for col in range(c, c + size):
                grid[row][col] = 1

    def get_next_pos(r, c):
        if c == N - 1:
            return r + 1, 0
        else:
            return r, c + 1

    remains = [M] * (K + 1)
    min_count = INF
    dfs(0, 0, 0)
    return min_count if min_count != INF else -1


def main():
    stdin = sys.stdin
    grid = [[int(x) for x in stdin.readline().split()] for _ in range(10)]
    print(solve(grid, 10, 5, 5))


if __name__ == "__main__":
    main()

from util import *
import pytest


def test1():
    assert solve([[1, 1], [1, 1]], 2, 2, 2) == 1
    assert solve([[1, 1], [1, 0]], 2, 2, 2) == -1
    assert solve([[1, 1], [1, 0]], 2, 3, 3) == 3
    assert solve([[1, 1], [1, 0]], 2, 3, 3) == 3


def test2():
    in_str = '''
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
    '''.strip()
    assert mock_io(main)(in_str) == '0'


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
    '''.strip(),
     '''
0
     '''.strip()),
    ('''
0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
'''.strip(),
     '''
4
     '''.strip()),
    ('''
0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
'''.strip(),
     '''
5
     '''.strip()),
    ('''
0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
'''.strip(),
     '''
-1
     '''.strip()),
    ('''
0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 1 1 1 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0
0 0 0 1 1 1 1 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
'''.strip(),
     '''
7
     '''.strip()),
    ('''
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
'''.strip(),
     '''
4
     '''.strip()),
    ('''
0 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 0 0 0 0
0 1 1 1 1 1 0 0 0 0
0 0 1 1 1 1 0 0 0 0
0 0 1 1 1 1 0 0 0 0
0 1 1 1 1 1 1 1 1 1
0 1 1 1 0 1 1 1 1 1
0 1 1 1 0 1 1 1 1 1
0 0 0 0 0 1 1 1 1 1
0 0 0 0 0 1 1 1 1 1
'''.strip(),
     '''
6
     '''.strip()),
    ('''
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 0 1 1 1 1
0 0 0 0 0 0 0 0 0 0
0 1 1 1 0 1 1 0 0 0
0 1 1 1 0 1 1 0 0 0
0 1 1 1 0 0 0 0 0 1
'''.strip(),
     '''
5
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
