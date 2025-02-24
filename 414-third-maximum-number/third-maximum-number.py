class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]

        first = -float('inf')

        for num in nums:
            first = max(first, num)
        
        second = -float('inf')

        for num in nums:
            if num > second and num != first:
                second = num

        third = -float('inf')
        for num in nums:
            if num > third and num != first and num != second:
                third = num

        return third if third != -float('inf') else first
        