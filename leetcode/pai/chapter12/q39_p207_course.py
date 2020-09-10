from typing import List, Set, Dict
import pytest


# 96ms, 16.8MB (94%, 19%)
class SolutionFirst:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        visited = [False] * numCourses
        locked = set()

        def dfs(i):
            if visited[i]:
                return True

            if i in locked:
                return False
            locked.add(i)
            for p in graph[i]:
                if not dfs(p):
                    return False
            locked.remove(i)
            visited[i] = True
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


Solution = SolutionFirst


@pytest.mark.parametrize(['n', 'in_', 'out'], [
    (2, [[1,0]], True),
    (2, [[1,0],[0,1]], False),
])
def test1(n, in_, out):
    assert Solution().canFinish(n, in_) == out
