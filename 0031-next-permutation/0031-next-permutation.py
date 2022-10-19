class Solution:
    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        #find the breach
        i = n - 2
        
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
            
        #find the digit to be swapped with
        
        if i != -1:
            j = n - 1
            while nums[i] >= nums[j]:
                j -= 1
                
            nums[i], nums[j] = nums[j], nums[i]
            
            
        self.reverse(nums, i + 1, n - 1)
        
        
        