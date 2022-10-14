class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        degrees = [0] * (n+1)
        
        for a, b in trust:
            degrees[a] -= 1
            degrees[b] += 1
            
        
        for i in range(1, len(degrees)):
            if degrees[i] == n - 1:
                return i
            
        return -1
            
        