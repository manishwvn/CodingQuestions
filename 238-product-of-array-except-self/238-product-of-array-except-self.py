class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = [1 for i in range(len(nums))]
        prefix, suffix = 1, 1
        
        for i in range(len(nums)):
            prod[i] = prefix
            # print(prod)
            prefix *= nums[i]
        
        
        for i in range(len(nums) - 1, -1, -1):
            prod[i] *= suffix
            # print(prod)
            suffix *= nums[i]
        
        
        return prod
        