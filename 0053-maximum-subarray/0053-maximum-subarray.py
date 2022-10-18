class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        
        maxm = -float("inf")
        i = 0
        maxm = nums[0]
        curr = nums[0]
        for j in range(1, n):
            curr += nums[j]
            curr = max(nums[j], curr)
            maxm = max(maxm, curr)
            
        return maxm
            
        
        