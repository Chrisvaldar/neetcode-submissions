from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        freshCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    freshCount += 1
        
        minutes = 0
        while q and freshCount:
            for _ in range(len(q)):
                i, j = q.popleft()
                neighbors = {(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)}
                for x, y in neighbors:
                    if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0 or grid[x][y] != 1:
                        continue
                    if grid[x][y] == 1:
                        grid[x][y] = 2
                        freshCount -= 1
                        q.append((x, y))
            minutes += 1
        return minutes if not freshCount else -1
