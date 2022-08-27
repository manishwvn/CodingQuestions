class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
    
        val1, val2 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = max(val2, val1 + nums[i])
            val1 = val2
            val2 = temp
            
        return val2
    
    
        
        
        