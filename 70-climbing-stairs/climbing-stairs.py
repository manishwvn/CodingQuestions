class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        return self._climb(n, memo)
    
    def _climb(self, n: int, memo: list) -> int:
        if n < 3:
            return n
        if memo[n] == 0:
            memo[n] = self._climb(n - 1, memo) + self._climb(n - 2, memo)
        return memo[n]
        