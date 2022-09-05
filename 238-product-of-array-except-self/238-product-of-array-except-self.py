class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * len(nums)
        left, right = 1, 1

        for i in range(len(nums)):
            result[i] *= left
            left *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result
        