"""
Time/Space complexity = O(row*col)
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0
        
        row, col = len(grid), len(grid[0])
        dp = [[0]*col for _ in range(row)]
        
        for r in range(row):
            for c in range(col):
                if r-1 < 0 and c-1 < 0:
                    dp[r][c] = grid[r][c]
                elif r-1 < 0:
                    dp[r][c] = grid[r][c] + dp[r][c-1]
                elif c-1 < 0:
                    dp[r][c] = grid[r][c] + dp[r-1][c]
                else:
                    dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])
       
        return dp[row-1][col-1]