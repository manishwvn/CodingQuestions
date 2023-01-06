class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        
        if len(nums) == 2: return max(nums[0], nums[1])
        
        
        val0, val1 = nums[0], max(nums[0], nums[1])
        result = 0
        
        for i in range(2, len(nums)):
            result = max(val0 + nums[i], val1)
            val0 = val1
            val1 = result
            
        return result
            
        