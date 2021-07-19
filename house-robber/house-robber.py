class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
            
        second, first = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            current = max(first, second + nums[i])
            second = first
            first = current
            
        return first
        