class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        n, m = len(difficulty), len(worker)
        
        jobs = []
        
        for i in range(n):
            jobs.append([difficulty[i], profit[i]])
            
        jobs.sort()
        worker.sort()
        
        maxSoFar = [0] * n
        maxSoFar[0] = jobs[0][1]
        
        for i in range(n):
            maxSoFar[i] = max(maxSoFar[i-1], jobs[i][1])
            
        result = 0
        
        
        for i in range(m):
            curr = 0
            
            lo, hi = 0, n - 1
            idx = -1
            
            while lo <= hi:
                mid = (lo + hi) // 2
                
                if jobs[mid][0] <= worker[i]:
                    idx = mid
                    lo = mid + 1
                    
                else:
                    hi = mid - 1
                    
            if idx != -1:
                curr = maxSoFar[idx]
                
            result += curr
            
        return result
            
            
                
        