import sys
from itertools import count
from heapq import heappush, heappop
from copy import copy


def search_positions(lines, target):
    return [(r, c) for r, line in enumerate(lines) for c, cell in enumerate(line) if cell == target]


def get_next_positions(pos):
    r, c = pos
    return [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]


def measure_distance_to_dusts(src_dust, X, R, C):
    dust_distances = []
    visited = [[False] * C for _ in range(R)]
    visited[src_dust[0]][src_dust[1]] = True
    stack = [src_dust]
    for step in count(1):
        if not stack:
            break
        new_stack = []
        for pos in stack:
            for r, c in get_next_positions(pos):
                if not (0 <= r < R and 0 <= c < C) or visited[r][c] or X[r][c] == 'x':
                    continue
                if X[r][c] == '*':
                    dust_distances.append(((r, c), step))
                visited[r][c] = True
                new_stack.append((r, c))
        stack = new_stack
    return dust_distances


def traverse(graph, start):
    queue = [(0, start, set())]
    while queue:
        acc_dist, node, visited = heappop(queue)
        visited.add(node)
        if len(visited) == len(graph):
            return acc_dist
        for next_node, dist in graph[node]:
            if next_node not in visited:
                item = (acc_dist + dist, next_node, copy(visited))
                heappush(queue, item)
    return -1


def solve(R, C, X):
    dusts = search_positions(X, '*')
    start = search_positions(X, 'o')[0]
    graph = {src_pos: measure_distance_to_dusts(src_pos, X, R, C) for src_pos in dusts + [start]}
    return traverse(graph, start)


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
    import time
    st = time.time()
    for i in range(1000):
        get_output_with_stdin(main, in_str)
    print(f'elapse time : {time.time() - st}', file=sys.stderr)
    assert False
    assert get_output_with_stdin(main, in_str) == out_str
