class Solution:
    def fib(self, n: int) -> int:
        
        a, b = 0, 1
        
        for i in range(n):
            c = a + b
            a = b
            b = c
            
        return a
            
        