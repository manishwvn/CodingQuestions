class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) < 2 and nums[0] in {0, 1}:
            return nums[0] + 1
        
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
                
            else: 
                i += 1
        
        print(nums)
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
        
        
        