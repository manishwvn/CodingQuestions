class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums or len(nums) == 0: return 0            
        
        if len(nums) == 1: return 1
        
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)
        