class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) < 2: return True
        
        target = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= target:
                target = i
                
        return target == 0        
                
                
                
        
        