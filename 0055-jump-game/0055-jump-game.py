class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        #using bfs
        if len(nums) < 2: return True
        n = len(nums) - 1
        
        
        queue = deque()
        queue.append(0)
        visited = set()
        while queue:
            i = queue.popleft()
            
            for j in range(1, nums[i]+1):
                idx = i + j
                if idx >= n:
                    return True
                
                if idx not in visited:
                    visited.add(idx)
                    queue.append(idx)
                
        return False
            
        