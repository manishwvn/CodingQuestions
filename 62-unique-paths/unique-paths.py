class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache = [1 for j in range(n)]

        for i in range(1, m):
            for j in range(1, n):
                cache[j] = cache[j] + cache[j-1]
        
        print(cache)

        return cache[-1]


        