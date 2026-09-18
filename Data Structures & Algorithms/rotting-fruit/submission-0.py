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
        
        level = len(q)
        res = 0
        while q:
            y,x = q.popleft()
            neighbors = [(y + 1, x), (y, x + 1), (y - 1, x), (y, x - 1)]
            for n in neighbors: 
                if n[0] >= 0 and n[0] < len(grid) and n[1] < len(grid[0]) and n[1] >= 0 and grid[n[0]][n[1]] == 1:
                    grid[n[0]][n[1]] = 2
                    freshCount -= 1
                    q.append(n)
            level -= 1
            if not level and q:
                level = len(q)
                res += 1
        return res if not freshCount else -1
            
