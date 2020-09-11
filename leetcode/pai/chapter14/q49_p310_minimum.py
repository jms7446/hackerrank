from typing import List, Set, Dict
import pytest


# 240ms, 18.4MB (97%, 40%)
class SolutionFirst:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = {}
        for v, u in edges:
            graph.setdefault(v, set()).add(u)
            graph.setdefault(u, set()).add(v)

        leaves = [v for v in graph if len(graph[v]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                parent = graph[leaf].pop()
                graph[parent].remove(leaf)
                if len(graph[parent]) == 1:
                    new_leaves.append(parent)
            leaves = new_leaves

        return leaves


class SolutionLeetCode:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = [set() for i in range(n)]

        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in range(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)

                if len(adj[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves


Solution = SolutionFirst


@pytest.mark.parametrize(['n', 'edges', 'out'], [
    (4, [[1,0],[1,2],[1,3]], [1]),
    (6, [[3,0],[3,1],[3,2],[3,4],[5,4]], [3,4]),
    (1, [], [0]),
    (2, [[0, 1]], [0, 1]),
    (7, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]], [1,2])
])
def test1(n, edges, out):
    assert Solution().findMinHeightTrees(n, edges) == out
