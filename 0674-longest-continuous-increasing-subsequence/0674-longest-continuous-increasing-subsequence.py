class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return 1
        
        curr, maxm = 0, 0
        
        for i in range(len(nums)):
            if i == 0 or nums[i-1] >= nums[i]:
                curr = 1
            
            else:
                curr += 1
                
            maxm = max(curr, maxm)
            
        return maxm