class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = [-1] * len(nums)
        
        def helper(i):
            if i < 0: return 0
            
            if memo[i] >= 0:
                return memo[i]
            
            choose = nums[i] + helper(i-2)
            not_choose = helper(i-1)
            value = max(choose, not_choose)
            memo[i] = value
            
            return value
        
        return helper(len(nums) - 1)
        