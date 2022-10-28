class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return 0
        
        prefix = [None] * len(nums)
        suffix = [None] * len(nums)
        
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            prefix[i] = sum_
            
        sum_ = 0
        for i in range(len(nums)-1, -1, -1):
            sum_ += nums[i]
            suffix[i] = sum_
        
        print(prefix)
        print(suffix)
        
        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                return i
            
        return -1