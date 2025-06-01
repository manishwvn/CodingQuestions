class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        memo = [0] * (n + 1)
        memo[1], memo[2] = 1, 2

        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]

        return memo[n]

        

        