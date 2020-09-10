from typing import List, Set, Dict
import pytest
from collections import deque


directions = ((1, 0), (-1, 0), (0, 1), (0, -1))


# 144ms, 14.6MB (84%, 97%)
class SolutionFirst:
    """
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(sr, sc, label):
            queue = deque()
            queue.append((sr, sc))
            labels[sr][sc] = label
            while queue:
                pr, pc = queue.popleft()
                for dr, dc in directions:
                    r, c = pr + dr, pc + dc
                    if not (0 <= r < R and 0 <= c < C) or labels[r][c] is not None or grid[r][c] == '0':
                        continue
                    labels[r][c] = label
                    queue.append((r, c))

        if not grid:
            return 0

        R, C = len(grid), len(grid[0])
        labels = [[None] * C for _ in range(R)]
        label = 0
        for row in range(R):
            for col in range(C):
                if grid[row][col] == '1' and labels[row][col] is None:
                    bfs(row, col, label)
                    label += 1
        return label


# 140ms, 14.9MB (90%, 59%)
class SolutionFineTune:
    """
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(sr, sc):
            queue = deque()
            queue.append((sr, sc))
            grid[sr][sc] = '#'
            while queue:
                pr, pc = queue.popleft()
                for dr, dc in directions:
                    r, c = pr + dr, pc + dc
                    if not (0 <= r < R and 0 <= c < C) or grid[r][c] != '1':
                        continue
                    grid[r][c] = '#'
                    queue.append((r, c))

        if not grid:
            return 0
        R, C = len(grid), len(grid[0])
        count = 0
        for row in range(R):
            for col in range(C):
                if grid[row][col] == '1':
                    bfs(row, col)
                    count += 1
        return count


Solution = SolutionFineTune


@pytest.mark.parametrize(['in_', 'out'], [
    ([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
], 1),
    ([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
], 3),
])
def test1(in_, out):
    assert Solution().numIslands(in_) == out
