class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2: return n
        # steps = [0] * (n+1)
        # steps[1], steps[2] = 1, 2

        # for i in range(3, n+1):
        #     steps[i] = steps[i-1] + steps[i-2]
        
        # return steps[n]

        a, b = 1, 2
        steps = 0
        for i in range(3, n+1):
            steps = a + b
            a = b
            b = steps
        
        return steps



