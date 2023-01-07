class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        
        curr = maxm = nums[0]
        
        for i in range(1, len(nums)):
            curr += nums[i]
            curr = max(curr, nums[i])
            maxm = max(curr, maxm)
            
        return maxm
        