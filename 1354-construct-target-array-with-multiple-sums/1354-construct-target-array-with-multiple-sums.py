class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
        if len(target) == 1: return target == [1]
        
        total = sum(target)
        
        target = [-num for num in target]
        heapify(target)
        
        while -target[0] != 1:
            top = -heappop(target)
            rest = total - top
            
            if rest == 1: return True
            
            val = top % rest
            
            if val == 0 or val == top: return False
            
            heappush(target, -val)
            total = total - top + val
            
        return True
            
            
        