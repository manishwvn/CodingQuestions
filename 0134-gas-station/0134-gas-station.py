class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        
        curr, total = 0, 0 
        start = 0
        
        for i in range(n):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            
            if curr < 0:
                start = i + 1
                curr = 0
                
                
        return start if total >= 0 else -1
                
        