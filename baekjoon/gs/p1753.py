import sys
from collections import defaultdict
from heapq import heappush, heappop

INF = float('inf')


def solve(V, E, es, start):
    es = [(fr - 1, to - 1, d) for fr, to, d in es]
    start -= 1

    edges = [defaultdict(lambda: INF) for _ in range(V)]
    for fr, to, d in es:
        edges[fr][to] = min(edges[fr][to], d)
    dists = [INF] * V
    visited = [False] * V

    dists[start] = 0
    heap = [(0, start)]
    while heap:
        _, cur_node = heappop(heap)
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        for neighbor, dist in edges[cur_node].items():
            if visited[neighbor]:
                continue
            new_dist = dists[cur_node] + dist
            if new_dist < dists[neighbor]:
                dists[neighbor] = new_dist
                heappush(heap, (new_dist, neighbor))

    return dists


def main():
    stdin = sys.stdin
    V, E = [int(x) for x in stdin.readline().split()]
    s = int(stdin.readline())
    es = [[int(x) for x in stdin.readline().split()] for _ in range(E)]
    dists = solve(V, E, es, s)
    for dist in dists:
        print(dist if dist != INF else 'INF')


if __name__ == "__main__":
    main()

from util import *


def test_main():
    in_str = """
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
    """.strip()
    out_str = """
0
2
3
7
INF
    """.strip()
    timeit(mock_io(main), in_str)
    assert mock_io(main)(in_str) == out_str
