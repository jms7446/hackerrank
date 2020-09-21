from typing import List

DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


class Solution:

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def find(r, c):
            nonlocal num_space
            found = 0
            visited[r][c] = True
            num_space -= 1
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < R and 0 <= nc < C) or visited[nr][nc] or grid[nr][nc] == -1:
                    continue
                if grid[nr][nc] == 2 and num_space == 0:
                    found += 1
                else:
                    found += find(nr, nc)
            visited[r][c] = False
            num_space += 1
            return found

        if not grid:
            return 0

        R, C = len(grid), len(grid[0])
        num_space = 0
        start = (0, 0)
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    start = (r, c)
                if grid[r][c] == 0:
                    num_space += 1
        num_space += 1   # include starting position
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        return find(start[0], start[1])


def test():
    assert Solution().uniquePathsIII([[1,0,2]]) == 1
    assert Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]) == 2
    assert Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]) == 4
