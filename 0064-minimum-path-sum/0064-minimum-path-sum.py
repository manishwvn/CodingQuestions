class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                
                if r == m - 1 and c != n - 1:
                    dp[r][c] = grid[r][c] + dp[r][c+1]
                    
                elif c == n - 1 and r != m - 1:
                    dp[r][c] = grid[r][c] + dp[r+1][c]
                    
                elif r != m - 1 and c != n - 1:
                    dp[r][c] = min(dp[r+1][c], dp[r][c+1]) + grid[r][c]
                else:
                    dp[r][c] = grid[r][c]
                    
        return dp[0][0]
        