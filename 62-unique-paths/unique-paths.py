class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def memoized(i, j, cache):
            if i == m or j == n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if cache[i][j] > 0:
                return cache[i][j]

            cache[i][j] = memoized(i+1, j, cache) + memoized(i, j+1, cache)

            return cache[i][j]

        
        cache = [[0 for j in range(n)] for i in range(m)]
        return memoized(0, 0, cache)


        