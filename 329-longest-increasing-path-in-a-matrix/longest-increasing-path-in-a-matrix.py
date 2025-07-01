class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m, n =len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]
            best = 1
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if (0 <= ni and ni < m) and (0 <= nj and nj < n) and matrix[ni][nj] > matrix[i][j]:
                    best = max(best, 1+dfs(ni,nj))
            dp[i][j] = best
            return best
        long = 0
        for i in range(m):
            for j in range(n):
                long = max(long, dfs(i,j))
        return long