from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        while q:
            y,x = q.popleft()
            
            neighbors = [(y + 1, x), (y, x + 1), (y - 1, x), (y, x - 1)]

            for n in neighbors:
                if n[0] >= 0 and n[0] < len(grid) and n[1] < len(grid[0]) and n[1] >= 0 and grid[n[0]][n[1]] == 2147483647:
                    grid[n[0]][n[1]] = grid[y][x] + 1
                    q.append(n)
    
        # boxes = []
        # visited = []
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 0:
        #             boxes.append((i,j))

        # for box in boxes:
        #     q = deque()
        #     dist = 0
        #     counter = 1
        #     q.append(box)

        #     while q:
        #         y, x = q.popleft()
        #         if grid[y][x] == 2147483647:
        #             grid[y][x] = dist
        #         elif grid[y][x] == -1:
        #             continue
        #         q.append((y + 1, x))
        #         q.append((y, x + 1))
        #         q.append((y - 1, x))
        #         q.append((y, x - 1))
                
        #         counter -= 1
        #         if counter == 0:
        #             dist += 1
        #             counter = len(q)
        
        

