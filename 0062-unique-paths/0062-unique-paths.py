class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        
        def dfs(i, j, m, n):
            if i == m - 1 and j == n - 1:
                return 1
            
            if i < 0 or j < 0 or i == m or j == n:
                return 0
            
            if dp[i][j] == 0:
                dp[i][j] = dfs(i+1, j, m, n) + dfs(i, j+1, m, n)
                
            
            return dp[i][j]
            
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        return dfs(0, 0, m, n)
        
        
        
        