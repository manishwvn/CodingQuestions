class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) < 2 and nums[0] in {0, 1}:
            return nums[0] + 1
        
        s = set(nums)
        start = 1
        
        for _ in nums:
            if start not in s:
                return start
            start += 1
            
        return start
        
        
        