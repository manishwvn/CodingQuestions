#509. Fibonacci Number


class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        c = 0
        for i in range(0, n):
            c = a+b
            a = b
            b = c
      
        return a
