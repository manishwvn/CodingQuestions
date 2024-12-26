class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        hm = Counter(tasks)
        maxFreq = 0
        maxCount = 0
        
        maxFreq = max(hm.values())
        
        for task, freq in hm.items():
            if freq == maxFreq:
                maxCount += 1
                
                
        partitions = maxFreq - 1
        available =  partitions * (n - (maxCount - 1))
        pending = len(tasks) - (maxFreq * maxCount)
        empty = max(0, available - pending)
        
        return len(tasks) + empty
        
        
        
        