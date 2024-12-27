class Solution:
    def tribonacci(self, n: int) -> int:

        if n < 2: return n
        if n == 2: return 1

        a, b, c, result = 0, 1, 1, 0

        for i in range(3, n+1):
            result = a + b + c
            a = b
            b = c
            c = result
        
        return result
        