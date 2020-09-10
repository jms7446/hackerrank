from typing import List, Set, Dict
import pytest
from collections import defaultdict


# TODO 왜 동작하는지 이해는 되지만, 어떻게 이렇게 구성할 수 있는지 구성 방식을 정확히 이해 못함.
class SolutionFirst:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for fr, to in sorted(tickets, reverse=True):
            graph[fr].append(to)
        route = []

        def dfs(fr):
            while graph[fr]:
                dfs(graph[fr].pop())
            route.append(fr)

        dfs('JFK')
        return route[::-1]


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    ([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], ["JFK", "MUC", "LHR", "SFO", "SJC"]),
    ([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]], ["JFK","ATL","JFK","SFO","ATL","SFO"]),
    ([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]], ["JFK","NRT","JFK","KUL"]),
])
def test1(in_, out):
    assert Solution().findItinerary(in_) == out
