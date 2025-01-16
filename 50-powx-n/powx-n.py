class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        
        isne = False
        if n < 0:
            isne = True
        n = abs(n)  
        res = 1

        while n > 0:
            if n % 2 == 1:
                res *= x
            x *=x
            n = n //2
        if isne:
            res = 1/res
        return res