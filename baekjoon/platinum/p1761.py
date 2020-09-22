# 정점들의 거리

import sys
from typing import List, Union
from dataclasses import dataclass


@dataclass(frozen=True)
class TreeNode:
    idx: int
    depth: int
    dist: int
    parent: Union['TreeNode', None]


def solve(N, edges, pairs):
    # build graph with edges
    graph: list = [[] for _ in range(N)]
    for v1, v2, d in edges:
        graph[v1].append((v2, d))
        graph[v2].append((v1, d))

    # build tree
    nodes: List[Union[TreeNode, None]] = [None] * N
    root = TreeNode(0, 1, 0, None)
    nodes[root.idx] = root
    stack = [root]
    while stack:
        node = stack.pop()
        for n_idx, dist in graph[node.idx]:
            if node.parent and n_idx == node.parent.idx:
                continue
            n_node = TreeNode(n_idx, node.depth + 1, node.dist + dist, node)
            nodes[n_node.idx] = n_node
            stack.append(n_node)

    # calc dist by find LCA
    res = []
    for idx1, idx2 in pairs:
        node1, node2 = nodes[idx1], nodes[idx2]
        dist = node1.dist + node2.dist
        if node1.depth < node2.depth:
            node1, node2 = node2, node1
        while node1.depth > node2.depth:
            node1 = node1.parent
        while node1 != node2:
            node1 = node1.parent
            node2 = node2.parent
        res.append(dist - node1.dist * 2)
    return res


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    edges = [[int(x) if i == 2 else int(x) - 1 for i, x in enumerate(stdin.readline().split())] for _ in range(N - 1)]
    M = int(stdin.readline())
    pairs = [[int(x) - 1 for x in stdin.readline().split()] for _ in range(M)]
    for d in solve(N, edges, pairs):
        print(d)


if __name__ == "__main__":
    main()


from util import *
import pytest
import random
from itertools import combinations, islice


def make_tree_edges(n):
    for i in range(1, n):
        yield random.randint(0, i - 1), i


def test_time():
    def gen_prob():
        N = 40000
        M = 10000

        edges = [(n1, n2, random.randint(1, 10000)) for n1, n2 in make_tree_edges(N)]
        pairs = [(random.randint(0, N - 1), random.randint(0, N - 1)) for _ in range(M)]
        return N, edges, pairs

    random.seed(2)
    timeit_lp(solve, gen_prob(), num_iter=10000, time_limit=1, funcs=[solve])
    # timeit(solve, gen_prob(), num_iter=10000, time_limit=1)


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
7
1 6 13
6 3 9
3 5 7
4 1 3
2 4 20
4 7 2
3
1 6
1 4
2 6
    '''.strip(),
     '''
13
3
36
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
