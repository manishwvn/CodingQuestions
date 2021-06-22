class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            
            if nums[i] > 0:
                nums[i] = 1
                
            else:
                nums[i] = -1
                
                
        product = 1
        for num in nums:
            product *= num
            
        return product
        