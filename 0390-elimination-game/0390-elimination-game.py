class Solution:
    def lastRemaining(self, n: int) -> int:
        N = n   
        fwd = True   
        m = 2  
        s = 0  

        while N > 1:
            if fwd or N % 2 == 1: 
                s += m // 2
            m *= 2
            N = N // 2
            fwd = not fwd   
        return s+1