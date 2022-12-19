class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        sum_ = 0
        rsum = [0] * len(nums)
        
        for i in range(len(nums)):
            sum_ += nums[i]
            rsum[i] = sum_
            
        return rsum
        
        