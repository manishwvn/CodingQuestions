class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #in-place but more operations
        
        if len(nums) == 1:
            if nums[0] == 0:
                return [0]
            else:
                return nums[0]
            
        i, j = 0, 0
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1
                
        while i < len(nums):
            if nums[i] !=0:
                nums[j] = nums[i]
                j += 1
            i += 1
        
        if zeroes:
            for i in range(len(nums) - 1, -1, -1):
                nums[i] = 0 
                zeroes -= 1
                if zeroes == 0:
                    break
                
        
        
        
            
            
        