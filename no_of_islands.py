from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        indx_queue = deque()
        island = 0
        
        for i in range(row):
            for j in range(col):
                
                if grid[i][j] == '1':
                    
                    island += 1
                    
                    indx_queue.append((i, j))
                    
                    while indx_queue:
                        
                        i, j = indx_queue.popleft()
                        
                        grid[i][j] = '0'

                        if i + 1 < row and grid[i + 1][j] == '1':
                            indx_queue.append((i+1, j))
                            
                        if i - 1 >=0 and grid[i - 1][j] == '1':
                            indx_queue.append((i-1, j))

                        if j + 1 < col and grid[i][j+1] == '1':
                            indx_queue.append((i, j + 1))

                        if j - 1 >= 0  and grid[i][j-1] == '1':
                            indx_queue.append((i, j-1))

                
        return island