class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        def double(nums):
            for i in range(len(nums) - 1):
                if nums[i] == nums[i+1]:
                    nums[i] = nums[i] * 2
                    nums[i+1] = 0
            return nums

        def shift(nums):
            j = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[j] = nums[i]
                    j += 1
            
            while j < len(nums):
                nums[j] = 0
                j += 1
            return nums



        return shift(double(nums))


        