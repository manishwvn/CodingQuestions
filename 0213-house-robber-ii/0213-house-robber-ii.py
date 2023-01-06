class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            val0, val1 = nums[0], max(nums[0], nums[1])
            for j in range(2, len(nums)):
                val0, val1 = val1, max(val0 + nums[j], val1)
                
            return val1
        
        if len(nums) < 3: return max(nums)

        loot1 = helper(nums[:-1])
        loot2 = helper(nums[1:])
        return max(loot1, loot2)
        