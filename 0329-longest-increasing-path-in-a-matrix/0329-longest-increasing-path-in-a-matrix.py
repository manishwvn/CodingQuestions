class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        res = 0

        def dfs(i, j):

            nonlocal res
            if dp[i][j] != 0:
                return dp[i][j]
            dp[i][j] = 1
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dfs(x, y) + 1)
            res = max(res, dp[i][j])
            return dp[i][j]

        for i in range(m):
            for j in range(n):
                dfs(i, j)
        return res