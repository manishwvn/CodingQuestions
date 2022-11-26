class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        n, m = len(difficulty), len(worker)
        
        temp = []
        
        for i in range(n):
            temp.append([difficulty[i], profit[i]])
            
        temp.sort()
        worker.sort()
        
        max_, curr, i = 0, 0, 0
        
        for work in worker:
            while i < n and work >= temp[i][0]:
                curr = max(curr, temp[i][1])
                i += 1
                
            max_ += curr
            
        return max_
                
        