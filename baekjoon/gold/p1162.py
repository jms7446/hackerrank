#도로포장

import sys
from heapq import heappop, heappush

INF = float('inf')


def solve(N, _, K, edges):
    graph = [[] for _ in range(N)]
    for fr, to, dist in edges:
        graph[fr - 1].append((to - 1, dist))
        graph[to - 1].append((fr - 1, dist))
    start, end = 0, N - 1

    dists = [[INF] * N for _ in range(K + 1)]

    heap = [(0, start, K)]
    dists[K][start] = True
    while heap:
        cost, city, remain = heappop(heap)
        if city == end:
            return cost
        if cost > dists[remain][city]:
            continue
        for next_city, dist in graph[city]:
            new_cost = cost + dist
            if new_cost < dists[remain][next_city]:
                heappush(heap, (new_cost, next_city, remain))
                dists[remain][next_city] = new_cost
            if remain > 0 and cost < dists[remain - 1][next_city]:
                heappush(heap, (cost, next_city, remain - 1))
                dists[remain - 1][next_city] = cost
    return -1


def main():
    stdin = sys.stdin
    N, M, K = [int(x) for x in stdin.readline().split()]
    edges = [[int(x) for x in stdin.readline().split()] for _ in range(M)]
    print(solve(N, M, K, edges))


if __name__ == "__main__":
    main()

from util import *
import pytest
import random


def gen_prob(N, M, K):
    edges = {}
    for i in range(1, N):
        edges[(i, i + 1)] = random.randint(1, 5)
    while len(edges) < M:
        fr, to = random.randint(1, N), random.randint(1, N),
        if fr != to and (fr, to) not in edges:
            edges[(fr, to)] = random.randint(1, 5)
    edges = [(fr, to, dist) for (fr, to), dist in edges.items()]
    return merge_to_lines([
        [N, M, K],
        merge_to_lines(edges),
    ])


def test_compare():
    compare_func_results(mock_io(main), ext_binary_to_func('p1162'), generate_probs(gen_prob, (5, 5, 1), count=10))


def test_time():
    random.seed(2)
    timeit_lp(mock_io(main), gen_prob(1000, 5000, 20), funcs=[solve])



@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
4 4 1
1 2 10
2 4 10
1 3 1
3 4 100
    '''.strip(),
     '''
1
     '''.strip()),
    ('''
1 1 0
1 1 1
    '''.strip(),
     '''
0
     '''.strip()),
    ('''
4 4 1
1 2 1
2 3 3
3 4 4
4 2 3
    '''.strip(),
     '''
1
     '''.strip()),
    ('''
4 5 1
1 2 5
2 3 5
3 4 4
2 1 2
4 1 1
    '''.strip(),
     '''
0
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
