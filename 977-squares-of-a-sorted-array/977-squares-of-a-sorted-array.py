class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 1:
            return [nums[0] ** 2]
        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = abs(nums[i])
        
        sqr_nums = [None] * len(nums)
        l, r = 0, len(nums) - 1
        
        for i in range(len(sqr_nums) - 1, -1, -1):
            if nums[r] > nums[l]:
                sqr_nums[i] = nums[r] ** 2
                r -= 1
                
            else:
                sqr_nums[i] = nums[l] ** 2
                l += 1
            
            if l > r:
                break
                
        return sqr_nums
            
                
        