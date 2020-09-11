from typing import List, Set, Dict
import pytest
from heapq import heappop, heappush

INF = float('inf')


# 496ms, 15.5MB (75%, 69%)
class SolutionFirst:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        K = K - 1
        graph = [[] for _ in range(N)]
        for u, v, w in times:
            graph[u-1].append((v-1, w))

        visited = [False] * N
        dists = [INF] * N
        heap = [(0, K)]
        while heap:
            d, v = heappop(heap)
            if d >= dists[v]:
                continue
            dists[v] = d
            for u, w in graph[v]:
                if d + w < dists[u]:
                    heappush(heap, (d + w, u))
        res = max(dists)
        return res if res != INF else -1


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'n', 'k', 'out'], [
    # ([[2,1,1],[2,3,1],[3,4,1]], 4, 2, 2),
    ([[1,2,1]], 2, 1, 1),
])
def test1(in_, n, k, out):
    assert Solution().networkDelayTime(in_, n, k) == out
