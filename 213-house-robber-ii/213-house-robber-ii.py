class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            val1, val2 = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                temp = max(val2, val1 + nums[i])
                val1 = val2
                val2 = temp
            
            return val2
        
        if not nums:
            return 0
        
        if len(nums) <= 3:
            return max(nums)
        
        loot1 = helper(nums[0:len(nums) -1])
        loot2 = helper(nums[1:])
        return max(loot1, loot2)
        