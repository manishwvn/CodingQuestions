class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        a, b = 1, 2
        res = 0
        for _ in range(3, n+1):
            res = a + b
            a = b
            b = res

        return res

        

        