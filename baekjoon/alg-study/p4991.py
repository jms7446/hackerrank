import sys
from itertools import count


def search_position(lines, target):
    for r, line in enumerate(lines):
        c = line.find(target)
        if c >= 0:
            return r, c


def init_visited(R, C):
    return [[False] * C for _ in range(R)]


def get_next_positions(pos):
    r, c = pos
    return [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]


def solve(R, C, X):
    dirty_count = sum(x.count('*') for x in X)
    if dirty_count == 0:
        return 0
    start_position = search_position(X, 'o')

    stack = [(start_position, init_visited(R, C), set())]
    for step in count(1):
        if not stack:
            return -1
        new_stack = []
        for pos, visited, found in stack:
            for r, c in get_next_positions(pos):
                if not (0 <= r < R and 0 <= c < C) or visited[r][c] or X[r][c] == 'x':
                    continue
                if X[r][c] == '*' and (r, c) not in found:
                    new_found = found.union({(r, c)})
                    if len(new_found) == dirty_count:
                        return step
                    new_visited = init_visited(R, C)
                    new_visited[r][c] = True
                    new_stack.append(((r, c), new_visited, new_found))
                else:
                    visited[r][c] = True
                    new_stack.append(((r, c), visited, found))
        stack = new_stack


def main():
    stdin = sys.stdin
    while True:
        C, R = [int(x) for x in stdin.readline().split()]
        if R == 0:
            break
        X = [stdin.readline().strip() for _ in range(R)]
        print(solve(R, C, X))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
2 2
o*
**
7 5
.......
.o...*.
.......
.*...*.
.......
15 13
.......x.......
...o...x....*..
.......x.......
.......x.......
.......x.......
...............
xxxxx.....xxxxx
...............
.......x.......
.......x.......
.......x.......
..*....x....*..
.......x.......
10 10
..........
..o.......
..........
..........
..........
.....xxxxx
.....x....
.....x.*..
.....x....
.....x....
0 0
    '''.strip(),
     '''
3
8
49
-1
     '''.strip()),
])
def test_main(in_str, out_str):
    assert get_output_with_stdin(main, in_str) == out_str
