class Solution:
    def knightDialer(self, n: int) -> int:
        
        neighbors = {
            0:(4,6),
            1:(6,8),
            2:(7,9),
            3:(4,8),
            4:(0,3,9),
            5:(),
            6:(0,1,7),
            7:(2,6),
            8:(1,3),
            9:(2,4)
    }
        
        mod = 10 ** 9 + 7
        previous = [1] * 10
        
        for i in range(n - 1):
            current = [0] * 10
            
            for src in range(10):
                for dest in neighbors[src]:
                    current[dest] = (current[dest] + previous[src])
        
            previous = current
        
        
        
        
        return sum(previous) % mod
        